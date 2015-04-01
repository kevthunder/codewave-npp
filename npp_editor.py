import Npp
import sys
import os.path
import codewave_core.editor
import codewave_core.util

class NppEditor(codewave_core.editor.Editor):
	def __init__(self):
		self.namespace = 'npp'
	@property
	def text(self):
		return Npp.editor.getText()
	def getCursorPos(self):
		return {'start':Npp.editor.getSelectionStart(), 'end':Npp.editor.getSelectionEnd()}
	def textSubstr(self,start,end):
		return Npp.editor.getTextRange(start,end)
	def textLen(self):
		return Npp.editor.getLength()
	def insertTextAt(self,text,pos):
		Npp.editor.insertText(pos,text)
	def setCursorPos(self,start,end = None):
		if end is None :
			end = start
		Npp.editor.setSelection(start,end)
	def spliceText(self,start, end, text):
		Npp.editor.setTarget(start, end)
		Npp.editor.replaceTarget(text)
	def beginUndoAction(self):
		Npp.editor.beginUndoAction()
	def endUndoAction(self):
		Npp.editor.endUndoAction()
	def getLang(self):
		try :
			return Npp.notepad.getCurrentLang().name
		except Exception as e:
			return Npp.editor.getLexerLanguage()
	def getEmmetContextObject(self):
		emmet_path = os.path.join(Npp.notepad.getNppDir(),'plugins','EmmetNPP')
		if emmet_path not in sys.path :
			sys.path.insert(0, emmet_path)
		import npp_emmet
		return npp_emmet.ctx
	def allowMultiSelection(self):
		return True
	def setMultiSel(self,selections):
		first = selections.pop(0)
		if first is not None :
			Npp.editor.setSelection(first.start, first.end)
		for sel in selections :
			Npp.editor.addSelection(sel.start, sel.end)
	def getMultiSel(self):
		selections = []
		for i in range(0,Npp.editor.getSelections()):
			selections.append(codewave_core.util.Pos(Npp.editor.getSelectionNStart(i), Npp.editor.getSelectionNEnd(i)))
		return selections
	def canListenToChange(self):
		return True
	def addChangeListener(self,callback):
		Npp.editor.callback(callback, [Npp.SCINTILLANOTIFICATION.CHARADDED])
	def removeChangeListener(self,callback):
		# Bug : Cant remove the callback only for some reason
		Npp.editor.clearCallbacks(callback)
		Npp.editor.clearCallbacks([Npp.SCINTILLANOTIFICATION.CHARADDED]) 
		