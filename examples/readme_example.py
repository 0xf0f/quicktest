from quicktest import TestList

example_tests = TestList('Example Tests')


@example_tests.test
def test_1():
    assert 1 == 1


@example_tests.test
def test_2():
    assert 1 + 1 == 3


@example_tests.test
def test_3():
    assert 2 == 2


example_tests.run()