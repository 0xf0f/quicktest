##### Installation
```commandline
pip install git+https://github.com/0xf0f/quicktest
```

##### Example
```python
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

# or to write results to a file:
with open('test_results.txt', 'w') as file:
	example_tests.run(out=file)

```

##### Output
```commandline
Example Tests - 2019-06-26 03:28:21
test_1 - succeeded
test_2 - failed
test_3 - succeeded
2 out of 3 tests succeeded.

Failures:
Traceback (most recent call last):
  File "C:\Users\admin\Documents\Projects\quicktest\quicktest\test_run.py", line 17, in run
    self.return_value = self.test.method(*args, **kwargs)
  File "C:/Users/admin/Documents/Projects/quicktest/examples/readme_example.py", line 13, in test_2
    assert 1 + 1 == 3
AssertionError
```