# Geodesic Framework
# Copyright 2018 Isaac Waldron. See LICENSE for details

import argparse
import sys

class ConsoleApp(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser()

    def run(self, args = None):
        self._setUp()
        self.__parse(args)
        self._run()
        self._tearDown()

    def _setup(self):
        pass

    def _run(self):
        pass

    def _tearDown(self):
        pass

    def __parse(self, args = None):
        if args == None:
            args = sys.argv
        self._args = self._parser.parse_args(args)