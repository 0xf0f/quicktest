from traceback import format_exc
from quicktest.test import Test


class TestRun:
    def __init__(self, test: Test):
        self.test = test
        self.completed = False
        self.return_value = None
        self.error = None

    def succeeded(self):
        return self.completed and not self.error

    def run(self):
        try:
            self.return_value = self.test.method()
        except:
            self.error = format_exc()

        self.completed = True
