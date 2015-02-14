# reload
import codewave_npp.codewave
reload(codewave_npp.codewave)
import codewave_npp.npp_editor
reload(codewave_npp.npp_editor)
import codewave_npp.cmd_instance
reload(codewave_npp.cmd_instance)
import codewave_npp.logger
reload(codewave_npp.logger)


from codewave_npp.codewave import Codewave
from codewave_npp.npp_editor import NppEditor


if 'cw' not in vars() or cw is None :
	codewave_npp.logger.log('init codewave');
	cw = Codewave(NppEditor())
	
cw.onActivationKey()

# codewave_npp.logger.log('expand: '+npp_emmet.ctx.js().locals.emmet.expandAbbreviation('ul>li*5>a'))
