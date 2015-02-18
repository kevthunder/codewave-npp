# reload
import codewave_npp.codewave.codewave
reload(codewave_npp.codewave.codewave)
import codewave_npp.npp_editor
reload(codewave_npp.npp_editor)
import codewave_npp.codewave.logger
reload(codewave_npp.codewave.logger)

debug = True
if debug or 'cw' not in vars() or cw is None :
	codewave_npp.codewave.codewave.init()
	codewave_npp.codewave.logger.log('init codewave');
	cw = codewave_npp.codewave.codewave.Codewave(codewave_npp.npp_editor.NppEditor())
	
cw.onActivationKey()

# codewave_npp.logger.log('expand: '+npp_emmet.ctx.js().locals.emmet.expandAbbreviation('ul>li*5>a'))
