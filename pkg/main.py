import argparse
import inspect

def parseargs(f):
	argspec = inspect.getfullargspec(f)
	
	argnames = argspec[0]
	kwdefaults = list() if argspec[3] is None else argspec[3]
	poslen = len(argnames)-len(kwdefaults)
	kwnames = argnames[poslen:]
	annotations = argspec[6]

	parser = argparse.ArgumentParser(description=('signature = ' + str(inspect.signature(f))))

	#add arglist for positional args
	parser.add_argument('arglist', nargs=poslen)
	#add optional args
	for option, default in zip(kwnames, kwdefaults):
		parser.add_argument(f'--{option}', required=False, default=default)

	# compile parser
	args = parser.parse_args()
	# get a copy of args, delete arglist, use as kwargs


	kwargs = vars(args).copy()
	del kwargs['arglist']

	# parse the arguments as the correct type
	for argname, func in annotations.items():
		idx = argnames.index(argname)
		if idx < len(args.arglist):
			args.arglist[idx] = func(args.arglist[idx])
		else:
			kwargs[argname] = func(kwargs[argname])

	f(*(args.arglist), **kwargs)