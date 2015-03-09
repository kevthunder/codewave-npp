import os.path
import imp, sys
import Npp

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path += [BASE_PATH]

import codewave_core.codewave
import npp_editor
reload(npp_editor)
import codewave_core.logger
import codewave_core.storage

def consoleWriteFunct(txt):
	Npp.console.write(txt)
		
debug = True


if debug :
	# reload
	try :
		for m in sys.modules.values() :
			try :
				if hasattr(m,'__file__') and "codewave" in m.__file__.lower() :
					Npp.console.write("reload :" + m.__name__)
					imp.reload(m)
			except Exception as e:
				Npp.console.write("reload failed :" + str(e))
	except Exception as e:
		Npp.console.write("reloads failed :" + str(e))
		
if debug or 'cw' not in vars() or cw is None :
	codewave_core.logger.WRITE_FUNCT = consoleWriteFunct
	codewave_core.logger.log('init codewave');
	codewave_core.storage.CONFIG_FOLDER = os.path.join(Npp.notepad.getPluginConfigDir(), 'codewave')
	codewave_core.codewave.init()
	cw = codewave_core.codewave.Codewave(npp_editor.NppEditor())
	
cw.onActivationKey()




# codewave_npp.logger.log('expand: '+npp_emmet.ctx.js().locals.emmet.expandAbbreviation('ul>li*5>a'))
