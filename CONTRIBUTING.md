# Contributing Guidelines

Please follow these guidelines to ensure the quality of the code:

- Use tabs for indentation.
- Use `snake_case` for function names.
- Use `UpperCamelCase` for class names.
- Use `lowerCamelCase` for variable names.
- Use `CAPITAL_CASE` for constants.
- Leave 2 empty lines after imports.
- End every file with a single empty line.
- Use type annotations (e.g. `def foo(bar: int) -> None` or `def baz() -> int`) in function signatures.
- Use different types of comments:
	- Comments for more complicated code fragments.
	- Docstrings for functions, e.g.:
	```python
	def Add(a: int, b: int) -> int:
		"""
		Add two variables, that should be of type int, and return their sum
		"""
		return a+b
	```

	- Use tagging for incomplete code fragments and update the issue on Github, e.g.:
	```python
	def Add():
		# TODO: write body of function
		pass

	def Something():
		# FIXME: add type annotations
		return 1
	```

- Avoid wild code. Every executable element of code should be included in a function or a method.
- Only one file should be the executable file. It must contain the `main()` function, and the call to `main()` should be protected in the following way:

```python
if __name__ == "__main__":
	main()
```

- Every module should have an `__init__.py` file, in which we import all functions and classes from other files of this module:

```python
# file __init__.py located in folder foo
from foo.bar import qux, fred
from foo.baz import thud
```

- Never use `from package import *` because it can overwrite imported functions or objects. Instead, use `from package import thing1, thing2` or `import package` or `import package as p`.

- Python 3.10 allows you to use the following functionality to skip ugly if statements:

```python
match term:
	case pattern_1:
		action_1
	case pattern_2:
		action_2
	case pattern_3:
		action_3
	case _:
		action_default
```

- Use numpy for matrix and array operations, which is much faster than regular Python arrays.
