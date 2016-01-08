def fuc1(*arg):
	print arg

def run(f,*arg):
	f(arg)

if __name__=='__main__':
	run(fuc1)