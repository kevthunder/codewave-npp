import os.path
import imp, sys
import Npp
# reload
import codewave_npp.codewave.codewave
import codewave_npp.npp_editor
reload(codewave_npp.npp_editor)
import codewave_npp.codewave.logger
import codewave_npp.codewave.storage

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
	codewave_npp.codewave.logger.WRITE_FUNCT = consoleWriteFunct
	codewave_npp.codewave.logger.log('init codewave');
	codewave_npp.codewave.storage.CONFIG_FOLDER = os.path.join(Npp.notepad.getPluginConfigDir(), 'codewave')
	codewave_npp.codewave.codewave.init()
	cw = codewave_npp.codewave.codewave.Codewave(codewave_npp.npp_editor.NppEditor())
	
cw.onActivationKey()




# codewave_npp.logger.log('expand: '+npp_emmet.ctx.js().locals.emmet.expandAbbreviation('ul>li*5>a'))
