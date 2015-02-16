import Npp

last_log = None

def log(*arguments):
	global last_log
	out = ''
	for msg in arguments:
		last_log = msg
		if(hasattr(msg,"__class__") and hasattr(msg,"__dict__")):
			msg = '<'+msg.__class__.__module__+'.'+msg.__class__.__name__+' '+str(vars(msg))+'>'
		out += str(msg)+' '
	Npp.console.write(out+'\n')

def step(prop):
	global last_log
	if last_log is not None and hasattr(last_log,prop):
		next = getattr(last_log,prop)
		log(next)
		return next