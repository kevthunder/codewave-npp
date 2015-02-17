# reload
import codewave_npp.codewave
reload(codewave_npp.codewave)
import codewave_npp.npp_editor
reload(codewave_npp.npp_editor)
import codewave_npp.logger
reload(codewave_npp.logger)

debug = True
if debug or 'cw' not in vars() or cw is None :
	codewave_npp.codewave.init()
	codewave_npp.logger.log('init codewave');
	cw = codewave_npp.codewave.Codewave(codewave_npp.npp_editor.NppEditor())
	
cw.onActivationKey()

# codewave_npp.logger.log('expand: '+npp_emmet.ctx.js().locals.emmet.expandAbbreviation('ul>li*5>a'))
