from parseargs import parseargs


def fun(firstname, lastname:str, number:int = 5):
	print(f"Hello {firstname} {lastname}")
	print(f"Your number is {number}")
	number *= 2
	print(f"Twice your number is {number}")


parseargs(fun)