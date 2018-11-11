import unittest
from pygeodesic import ConsoleApp

class MyConsoleApp(ConsoleApp):
    def __init__(self, expectedArg):
        ConsoleApp.__init__(self)
        self._expectedArg = expectedArg
        self.setupCalled = False
        self.runCalled = False
        self.tearDownCalled = False

    def _setUp(self):
        self._parser.description = 'A program that does something.'
        self._parser.add_argument('arg')
        self.setupCalled = True

    def _run(self):
        if self._args.arg != self._expectedArg:
            raise RuntimeError(
                'Incorrect argument supplied, expected'.format(
                    self._expectedArg
                )
            )
        self.runCalled = True

    def _tearDown(self):
        self.tearDownCalled = True

class TestConsoleApp(unittest.TestCase):
    def testConsoleApp(self):
        arg = 'testArg'
        app = MyConsoleApp(arg)
        self.assertFalse(app.setupCalled)
        self.assertFalse(app.runCalled)
        self.assertFalse(app.tearDownCalled)
        app.run([arg])
        self.assertTrue(app.setupCalled)
        self.assertTrue(app.runCalled)
        self.assertTrue(app.tearDownCalled)

    def testConsoleAppRaises(self):
        arg = 'testArg'
        otherArg = 'failArg'
        app = MyConsoleApp(arg)
        self.assertRaises(RuntimeError, app.run, [otherArg])
