A python module for writing and running tests.
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
with open('test_results.txt') as file:
	example_tests.run(out=file)

```

output:
```commandline
2019-06-22 13:55:01.382579
Example Tests - test_1 - succeeded
Example Tests - test_2 - failed
Traceback (most recent call last):
  File "C:\Users\admin\Documents\Projects\quicktest\quicktest\test_run.py", line 17, in run
    self.return_value = self.test.method()
  File "C:/Users/admin/Documents/Projects/quicktest/examples/readme_example.py", line 13, in test_2
    assert 1 + 1 == 3
AssertionError

Example Tests - test_3 - succeeded
Example Tests - 2 out of 3 tests succeeded.

```