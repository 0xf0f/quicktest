import sys
import datetime

from quicktest.test import Test
from quicktest.test_run import TestRun


class TestList:
    def __init__(self, name='Unnamed Test List'):
        self.name = name
        self.tests = []

    def add_test(self, test: Test):
        self.tests.append(test)

    def add_test_from_method(self, method, name=None):
        if name is None:
            name = method.__name__

        new_test = Test()
        new_test.method = method
        new_test.name = name

        self.add_test(new_test)
        return method

    test = add_test_from_method

    def run(self, out=sys.stdout):
        print(
            datetime.datetime.now(),
            file=out
        )

        tests_succeeded = 0
        for test in self.tests:
            test_run = TestRun(test)
            test_run.run()

            if test_run.succeeded():
                result = 'succeeded'
                tests_succeeded += 1
            else:
                result = 'failed'

            print(
                self.name, '-', test.name, '-', result,
                # 'with return value', test_run.return_value,
                file=out
            )

            if test_run.error:
                print(
                    test_run.error,
                    file=out
                )

        print(
            self.name, '-',
            tests_succeeded, 'out of', len(self.tests),
            'tests succeeded.',
            file=out
        )

        if tests_succeeded == len(self.tests):
            return True
        else:
            return False
