# reload
import codewave.codewave
reload(codewave.codewave)
import codewave.npp_editor
reload(codewave.npp_editor)
import codewave.cmd_instance
reload(codewave.cmd_instance)


from codewave import *
from codewave.codewave import Codewave
from codewave.npp_editor import NppEditor

cw = Codewave(NppEditor())
cw.onActivationKey()
