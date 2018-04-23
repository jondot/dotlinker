# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_glob_symlinks 1'] = [
    '/fixtures/glob-symlinks/atom/config2.symlink',
    '/fixtures/glob-symlinks/atom/config1.symlink',
    '/fixtures/glob-symlinks/atom/config3/foobar.symlink'
]
