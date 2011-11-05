#!/usr/bin/env python

from time import sleep

from test_dashvisor import setUp, tearDown

if __name__ == '__main__':
    try:
        setUp()
        while True:
            sleep(100)
    except (Exception, KeyboardInterrupt), e:
        tearDown()

