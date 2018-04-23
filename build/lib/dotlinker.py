from docopt import docopt
from os.path import expanduser, join, splitext, isdir
import os.path
from toolz.curried import pipe, filter, map, get, concat, mapcat
from os import symlink


class FileSystemIO(object):
    def link(self, source, target):
        try:
            symlink(source, target)
            print("{} -> {}".format(source, target))
        except:  # noqa
            print("(exists) {}".format(target))

    def ls(self, dir):
        return os.listdir(dir)

    def glob(self, root, recursive=True):
        # walk: root [dirs] [files] -> for each dir (tup.2), for
        # each file (tup.1), we need to join with root
        return pipe(
            os.walk(expanduser(root)),
            mapcat(lambda tup:
                map(lambda f: join(tup[0], f))(concat([tup[2], tup[1]]))),
            list) # noqa


class DryRunIO(FileSystemIO):
    def link(self, source, target):
        print("[dry-run] {} -> {}".format(source, target))


def glob_symlinks(root, io):
    return pipe(
        io.glob(root), filter(lambda f: splitext(f)[1] == '.symlink'), list)


def symlinkify(s, source='', target=''):
    (f, e) = splitext(s)
    if e != '.symlink':
        return None

    return f.replace(source, target)


def make_targets(src, target, symlinkfiles):
    return pipe(symlinkfiles, map(lambda p: (p, symlinkify(p, src, target))),
                             filter(lambda tup: tup[1]),
                             list) # noqa yapf: disable


def dirs(dir, io):
    return pipe(io.ls(dir), filter(lambda d: not d.startswith('-')),
                            map(lambda d: join(dir, d)),
                            filter(isdir),
                            list) # noqa yapf: disable


def perform_link(source, target, io):
    return pipe(make_targets(source, target, glob_symlinks(source, io)),
                        map(lambda tup: io.link(tup[0], tup[1])),
                        list) # noqa yapf: disable


def link(src, target, io):
    (abs_src, abs_tgt) = (expanduser(src), expanduser(target))
    return pipe(dirs(abs_src, io), map(lambda d: perform_link(d, abs_tgt, io)),
                                   list) # noqa yapf: disable


def main():
    doc = """dotfiles-link
        Usage:
        dotfiles-link <from> <to> [--dry-run]
        dotfiles-link --version

        Options:
        -d --dry-run     Perform dry run (don't apply changes to filesystem)
        --version        Show version.
        -h --help        Show this screen.
        """
    args = docopt(doc, version="dotfiles 1.0")
    (source, target, dry_run) = get(['<from>', '<to>', '--dry-run'])(args)
    IO = DryRunIO if dry_run else FileSystemIO
    link(source, target, IO())


if __name__ == '__main__':
    main()
