# ParseArgs


Example:
```
from parseargs import parseargs



def fun(firstname, lastname:str, number:int = 5):
	print(f"Hello {firstname} {lastname}")
	print(f"Your number is {number}")
	number *= 2
	print(f"Twice your number is {number}")



parseargs(fun)
```

Now on the command line, you can do:

```
python fun.py ricky bobby --number 5
```

Notice how it will print out 10. If you remove the annotation declaring the number an int, it will instead print out 55.