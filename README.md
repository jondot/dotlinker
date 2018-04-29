# dotlinker

Use [`dotrunner`](https://github.com/jondot/dotrunner) and [`dotlinker`](https://github.com/jondot/dotlinker) to build a fantastically aesthetic macOS dotfiles set up.

✅ Organize by topics (folder modules), i.e. 'nodejs', 'osx', and 'python'.  
✅ DAG (Directed Acyclic Graph) based runner for a powerful dependency system.  
✅ No shell scripts, gunk, yuck, and hairballs required

Here's an example dotfiles repo:

```
~/.dotfiles
    asdf/
    brew/
      install.yml
      Brewfile
    python/
    osx/
    nodejs/
      .npmrc.symlink
      install.yml
    fonts/
```

And here's an example `install.yml` taken from the `nodejs` module:

```yaml
script: npm i -g yarn
deps:
- asdf
```

## Quick Start

Install:

```
$ pip install dotrunner dotlinker
```

Dry run:

```
$ dotlinker ~/.dotfiles ~/ --dry-run
```

And finally, apply (this will obviously change your system!):

```
$ dotrunner ~/.dotfiles ~/
```

## Building a Dotfiles System with dotlinker

`dotlinker` is responsible for getting all of your configuration files from your `dotfiles` folder and linking them to their relevant places in the filesystem.

To see how to also _install_ things, look at [dotrunner](https://github.com/jondot/dotrunner).

This layout describes a few modules with their configuration:

```
fish/
  .config/
    fish/
      config.fish.symlink
npm/
  .npmrc.symlink
```

This system follows a few simple principles:

* Every directory is a _module_
* Any file or directory tree ending with the `symlink` extension will be symlinked.

Symlinking will take what ever directory path in the `dotfiles` folder and replicate it on top of the new root you've given `dotlinker` (remember: `dotlinker ~/.dotfiles ~/`) so:

* `~/.dotfiles/fish/.config/fish/config.fish.symlink` becomes `~/.config/fish/config.fish`
* `~/.dotfiles/npm/.npmrc.symlink` becomes `~/.npmrc`

# Contributing

Fork, implement, add tests, pull request, get my everlasting thanks and a respectable place here :).

### Thanks:

To all [Contributors](https://github.com/jondot/dotlinker/graphs/contributors) - you make this happen, thanks!

# Copyright

Copyright (c) 2018 [Dotan Nahum](http://gplus.to/dotan) [@jondot](http://twitter.com/jondot). See [LICENSE](LICENSE.txt) for further details.
