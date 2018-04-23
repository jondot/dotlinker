from dotlinker import glob_symlinks, symlinkify, make_targets, dirs, \
                      FileSystemIO, perform_link, link
from os.path import realpath, dirname, join, expanduser


class FakeIO(FileSystemIO):
    def __init__(self, globbed=None):
        self.globbed = globbed

    def link(self, source, target):
        return (True, source, target)

    def glob(self, dir, recursive=True):
        if (self.globbed):
            return self.globbed
        return super(FakeIO, self).glob(dir, recursive)


def fixture(p):
    return realpath(join(dirname(__file__), 'fixtures', p))


def sanitize(ps):
    return list(
        map(lambda p: str(p).replace(realpath(dirname(__file__)), ''), ps))


def test_glob_symlinks(snapshot):
    snapshot.assert_match(
        sanitize(glob_symlinks(fixture('glob-symlinks'), FileSystemIO())))


def test_symlinkify():
    assert symlinkify("/foo/bar.symlink") == "/foo/bar"
    assert symlinkify("foo/bar.symlink") == "foo/bar"
    assert symlinkify("bar.symlink") == "bar"
    assert symlinkify(
        "/users/foo/.dotfiles/hello/foo.symlink",
        source='/users/foo/.dotfiles/hello',
        target='/users/foo') == '/users/foo/foo'
    assert symlinkify(
        "/users/foo/.dotfiles/hello/config/foo.symlink",
        source='/users/foo/.dotfiles/hello',
        target='/users/foo') == '/users/foo/config/foo'
    assert not symlinkify("bar")


def test_dirs():
    assert sanitize(dirs(fixture('glob-symlinks'),
                         FileSystemIO())) == ['/fixtures/glob-symlinks/atom']


def test_perform_link():
    lns = perform_link(
        '/Users/jondoe/.dotfiles/git',
        '/Users/jondoe',
        FakeIO(globbed=['/Users/jondoe/.dotfiles/git/foo.symlink']))
    assert len(lns) == 1
    assert lns == [(True, '/Users/jondoe/.dotfiles/git/foo.symlink',
                    '/Users/jondoe/foo')]


def test_make_targets():
    assert make_targets('/users/foo/.dotfiles/hello', '/users/foo', [
        "/users/foo/.dotfiles/hello/foo.symlink",
        "/users/foo/.dotfiles/hello/config/hello.symlink"
    ]) == [("/users/foo/.dotfiles/hello/foo.symlink", "/users/foo/foo"),
           ("/users/foo/.dotfiles/hello/config/hello.symlink",
            "/users/foo/config/hello")]


def test_glob_symlinks_doesnt_exist():
    p = fixture('doesnt-exist')
    print(p)
    assert glob_symlinks(p, FileSystemIO()) == []


def test_link():
    map(lambda t: str(t[2]).replace(expanduser('~'), ''),
        link(fixture('glob-symlinks'), '~',
             FakeIO())) == ['/config2', '/config1', 'config3/foobar']
