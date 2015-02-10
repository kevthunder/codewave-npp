# reload
import codewave_npp.codewave
reload(codewave_npp.codewave)
import codewave_npp.npp_editor
reload(codewave_npp.npp_editor)
import codewave_npp.cmd_instance
reload(codewave_npp.cmd_instance)


from codewave_npp.codewave import Codewave
from codewave_npp.npp_editor import NppEditor

cw = Codewave(NppEditor())
cw.onActivationKey()
