# ParseArgs

##### A simple, intuitive way to parse command line arguments. Simply make a function, and call parseargs on it.
* parses data types through annoations (annotations not required for string arguments)
* parses positional arguments into positional cli arguments with the same name
* parses optional keyword arguments by adding them as optional cli arguments
* parses annotated arguments and uses the native cli specification for types
* adds a description of the command by using the signature of the method.

## Example


in fun.py:
```python
from parseargs import parseargs



def fun(firstname, lastname:str, number:int = 5):
	print(f"Hello {firstname} {lastname}")
	print(f"Your number is {number}")
	number *= 2
	print(f"Twice your number is {number}")


parseargs(fun)
```

Now on the command line, you can do:

```shell
$ python fun.py ricky bobby --number 5
```

Notice how it will print out 10. If you remove the annotation declaring the number an int, it will instead print out 55, because it will interpret it as a string.


We can get the method signature with:
```
$ python fun.py -h
usage: fun.py [-h] [-n NUMBER] firstname lastname

signature = (firstname, lastname: str, number: int = 5)

positional arguments:
  firstname
  lastname

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
```
