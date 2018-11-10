from geodesic import ConsoleApp

import argparse

class EchoApp(ConsoleApp):
    def _setUp(self):
        self._parser.add_argument('input', nargs=argparse.REMAINDER)

    def _run(self):
        print ' '.join(self._args.input[1:])

if __name__ == '__main__':
    app = EchoApp()
    app.run()
