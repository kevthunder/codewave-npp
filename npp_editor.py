import Npp

class NppEditor():
	def __init__(self):
		self.namespace = 'npp'
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