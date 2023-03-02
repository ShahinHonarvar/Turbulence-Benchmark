Each question has its own directory.

In a question directory:

- README.md file in a directory explains the parameter values with
  which it is acceptable to instantiate a question.

- params.txt contains a series of parameter values with which the
  question should be instantiated when the benchmark is used in
  practice.

- Optionally, genparams.py, a script used to help generating the
  values in params.txt.

- question.txt.template provides the parameterised version of the
  question, ready to be instantiated.

- solution.py.template provides the parameterised version of the
  sample solution, ready to be instantiated.

- test_suite_generator.py is a per-question script that generates a
  test suite for a particular instantiation of the question.

To instantiate a question, do:

```
python3 instantiate.py [question-number]/question.txt.template [parameter-values] > /path/to/instantiated/question.txt
```

For example, to instantiate question 1 with parameter values 10 and 100, storing the result in `/data/temp/question.txt`, do:

```
python3 instantiate.py 1/question.txt.template 10 100 > /data/temp/question.txt
```

An instantiated question can then be passed to a large language model, and the output from the model should be captured in a file called `solution.py`.

To create the test suite for a particular question instantiation, do:

```
python3 [question-number]/test_suite_generator.py [parameter-values] > /path/to/instantiated/tests.py
```

For example, to instantiate the test suite for question 1 with parameter values 10 and 100, storing the result in `/data/temp/tests.py`, do:

```
python3 1/test_suite_generator.py 10 100 > /data/temp/tests.py
```

To generate the sample solution for a particular question instantiation, do:

```
python3 instantiate.py [question-number]/solution.py.template [parameter-values] > /path/to/instantiated/solution.txt
```

For example, to instantiate the solution for question 1 with parameter values 10 and 100, storing the result in `/data/temp/solution.py`, do:

```
python3 instantiate.py 1/solution.py.template 10 100 > /data/temp/solution.py
```

To run tests for an instantiated question against a solution generated
from a large language model, or the sample solution, make sure the
test suite and solution are in the same directory, named `tests.py`
and `solution.py`. Go to this directory, and run:

```
python3 -m unittest tests.py
```
