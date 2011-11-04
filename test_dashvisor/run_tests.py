#!/usr/bin/env python

'''
simple shortcut for running nosetests via python
replacement for *.bat or *.sh wrappers
'''

import os
import sys
from os import path, environ

import nose



environ['DJANGO_SETTINGS_MODULE'] = 'test_dashvisor.settings'


def run_all(argv=None):

    if argv is None:
        argv = [
            'nosetests',
            '--with-coverage', '--cover-package=dashvisor', '--cover-erase',
            '--nocapture', '--nologcapture',
            '--verbose',
        ]
    else:
        for p in ('--with-coverage', '--cover-package=dashvisor', '--cover-erase'):
            if p not in argv:
                argv.append(p)

    nose.run_exit(
        argv=argv,
        defaultTest=path.abspath(path.dirname(__file__))
    )

if __name__ == '__main__':
    run_all(sys.argv)

