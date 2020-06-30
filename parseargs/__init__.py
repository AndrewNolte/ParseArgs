import argparse
import inspect

def parseargs(f):
	argspec = inspect.getfullargspec(f)
	
	argnames = argspec[0]
	kwdefaults = list() if argspec[3] is None else argspec[3]
	poslen = len(argnames)-len(kwdefaults)
	kwnames = argnames[poslen:]
	posnames = argnames[:poslen]
	annotations = argspec[6]

	parser = argparse.ArgumentParser(description=('signature = ' + str(inspect.signature(f))))

	# add args, using defaults if provided
	for i in range(len(argnames)):
		name = argnames[i]
		tp = annotations.get(name, str)
		if i - poslen >= 0:
			default = kwdefaults[i-poslen]
			parser.add_argument(f'-{name[0]}', f'--{name}', required=False, type=tp, default=default)
		else:
			parser.add_argument(name, type=tp)

	# compile parser
	args = parser.parse_args()
	kwargs = vars(args).copy()
	posargs = [kwargs[name] for name in posnames]
	for name in posnames:
		del kwargs[name]


	f(*posargs, **kwargs)