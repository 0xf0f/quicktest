import sys
import time

from quicktest.test import Test
from quicktest.test_run import TestRun
from typing import Callable, Union


class TestList:
    def __init__(self, name='Unnamed Test List'):
        self.name = name
        self.tests = []

    def add_test(self, test: Test):
        self.tests.append(test)

    def test(self, name_or_method: Union[str, Callable]):
        if callable(name_or_method):
            new_test = Test()
            new_test.name = name_or_method.__name__
            new_test.method = name_or_method
            self.add_test(new_test)
            return name_or_method

        elif isinstance(name_or_method, str):
            def wrapper(func):
                new_test = Test()
                new_test.name = name_or_method
                new_test.method = func
                self.add_test(new_test)
                return func
            return wrapper

    def run(self, *args, out=sys.stdout, **kwargs):
        print(
            self.name, '-',
            time.strftime('%Y-%m-%d %H:%M:%S'),
            file=out
        )

        failed_tests = []

        for test in self.tests:
            test_run = TestRun(test)
            test_run.run(*args, **kwargs)

            if test_run.succeeded():
                result = 'succeeded'
            else:
                result = 'failed'
                failed_tests.append(test_run)
                print('*', end='', file=out)

            print(
                test.name, '-', result,
                # 'with return value', test_run.return_value,
                file=out
            )

        print(
            len(self.tests)-len(failed_tests),
            'out of', len(self.tests), 'tests succeeded.',
            file=out
        )

        if failed_tests:
            print(file=out)
            print('Failures:', file=out)

            for test_run in failed_tests:
                print(test_run.test.name, file=out)
                print(test_run.error, file=out)

        return bool(failed_tests)

