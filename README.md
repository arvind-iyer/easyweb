# Easy Web #
#### Simple tool for prototyping web applications. ####

## Installation ##
To install Easy Web run

`pip install easyweb`

## Usage ##

You can call Easy Web on any Python class whose methods expect primitive arguments like strings, numbers.

Here's an example of calling Easy Web on a class.

```python
import easyweb

class Calculator(object):
  """A simple calculator class."""

  def add(self, a, b):
    return a + b

c = Calculator()

if __name__ == '__main__':
  easyweb.run(c)
```

Then, you can make requests like this:
*http://localhost:5000/calculator/add?a=5&b=6*
 
And get a json response:
*{'result': 11}*


And a Flask file would be generated like so:

```python
import calculator
calculator_instance = calculator.Calculator()

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/calculator/add")
def add():
    a = request.args.get('a')
    b = request.args.get('b')
	result = calculator_instance.add(a, b)
	return jsonify(result)
```
