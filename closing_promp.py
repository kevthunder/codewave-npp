import logger
import Npp
import util

class ClosingPromp():
	def __init__(self,codewave,start,end):
		self.codewave,self.start,self.end = codewave,start,end
		self.len = self.end - self.start
	def begin(self):
		Npp.editor.beginUndoAction()
		self.codewave.editor.insertTextAt("\n"+self.codewave.brakets+self.codewave.closeChar+self.codewave.brakets,self.end)
		self.codewave.editor.insertTextAt(self.codewave.brakets+self.codewave.brakets+"\n",self.start)
		Npp.editor.endUndoAction()
		p1 = self.start+len(self.codewave.brakets)
		p2 = self.end+len(self.codewave.brakets)*3+len(self.codewave.closeChar)+2
		self.codewave.editor.setCursorPos(p2)
		Npp.editor.addSelection(p1,p1)
		Npp.editor.callback(self.onAddChar, [Npp.SCINTILLANOTIFICATION.CHARADDED])
		return self
	def onAddChar(self,ch):
		# logger.log('added :'+str(ch))
		if ch['ch'] ==  32:
			logger.log('space added')
	def stop(self):
		if self.codewave.closingPromp == this :
			self.codewave.closingPromp = null
		Npp.editor.clearCallbacks(self.onAddChar)
	def cancel(self):
		openBounds = self.whithinOpenBounds(self.start+len(self.codewave.brakets))
		if openBounds is not None :
			closeBounds = self.whithinCloseBounds(openBounds)
			if closeBounds is not None :
				self.codewave.editor.spliceText(closeBounds.start-1,closeBounds.end,'')
				self.codewave.editor.spliceText(openBounds.start,openBounds.end+1,'')
				self.codewave.editor.setCursorPos(self.start,self.end)
		self.stop()
	def whithinOpenBounds(self,pos):
		innerStart = self.start+len(self.codewave.brakets)
		if self.codewave.findPrevBraket(pos) == self.start and self.codewave.editor.textSubstr(self.start,innerStart) == self.codewave.brakets :
			innerEnd = self.codewave.findNextBraket(innerStart)
			if innerEnd is not None :
				return util.wrappedPos( self.start, innerStart, innerEnd, innerEnd+len(self.codewave.brakets))
	def whithinCloseBounds(self,openBounds):
		start = openBounds.end+self.len+2
		innerStart = start+len(self.codewave.brakets)+len(self.codewave.closeChar)
		if self.codewave.editor.textSubstr(start,innerStart) == self.codewave.brakets+self.codewave.closeChar :
			innerEnd = self.codewave.findNextBraket(innerStart)
			if innerEnd is not None :
				return util.wrappedPos( start, innerStart, innerEnd, innerEnd+len(self.codewave.brakets))