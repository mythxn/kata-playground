# How to solve coding katas?
1. Gain comprehension of the problem.
2. Create a preliminary method that satisfies the correct method structure.
3. Construct tests to assess the preliminary method's functionality. (ideally 2 happy/sad flows)
4. Verify the accuracy of the tests in relation to your understanding.
5. Transform the preliminary method into actual functionality to make the tests pass.
6. Streamline the method for optimal performance through refactoring.


# How to initialize the kata?
```shell
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```


# How to run tests?
```shell
pytest --cov -s --disable-warnings
```


# How to set a breakpoint?
```python
import ipdb; ipdb.set_trace()
```