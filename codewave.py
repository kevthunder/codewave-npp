import Npp
from cmd_instance import CmdInstance


class Codewave():
	def __init__(self,editor):
		self.editor = editor
		self.brakets = '~~'
		self.deco = '~'
		self.closeChar = '/'
		self.noExecuteChar = '!'
		self.carretChar = '|'
		self.nameSpaces = []
		self.checkCarret = True
		self.vars = {}
    
	def onActivationKey(self):
		Npp.console.write('activation key\n')
		cmd = self.commandOnCursorPos()
		if cmd is not None :
			Npp.console.write(str(vars(cmd)))
			# cmd.execute()
		else:
			cpos = self.editor.getCursorPos()
			if cpos['start'] == cpos['end'] :
				self.addBrakets(cpos['start'],cpos['end'])
			else:
				self.promptClosingCmd(cpos['start'],cpos['end'])
	def commandOnCursorPos(self):
		cpos = self.editor.getCursorPos()
		return self.commandOnPos(cpos['end'])
	def commandOnPos(self,pos):
		prev = (
			pos-len(self.brakets)
			if self.editor.textSubstr(pos-len(self.brakets),pos) == self.brakets 
			else self.findPrevBraket(pos if self.isEndLine(pos) else pos+1)
		)
		if prev is None :
			return None 
		if prev > pos-len(self.brakets) :
			pos = prev
			prev = self.findPrevBraket(pos)
		next = self.findNextBraket(pos)
		if next is None or self.countPrevBraket(prev) % 2 != 0 :
			return None
		return CmdInstance(self,prev,self.editor.textSubstr(prev,next+len(self.brakets)))
	# def nextCmd(self,start = 0):
		# pos = start
		# while f = self.findAnyNext(pos ,[self.brakets,"\n"])
			# pos = f.pos + len(f.str)
			# if f.str == self.brakets
				# if beginning?
					# return new Codewave.CmdInstance(self,beginning,self.editor.textSubstr(beginning,f.pos+len(self.brakets)))
				# else
					# beginning = f.pos
			# else
				# beginning = None
		# None
	# def getEnclosingCmd(self,pos = 0):
		# cpos = pos
		# closingPrefix = self.brakets + self.closeChar
		# while (p = self.findNext(cpos,closingPrefix))?
			# if cmd = self.commandOnPos(p+len(closingPrefix))
				# cpos = cmd.getEndPos()
				# if cmd.pos < pos
					# return cmd
			# else
				# cpos = p+len(losingPrefix)
		# None
	def countPrevBraket(self,start):
		i = 0
		start = self.findPrevBraket(start)
		while start is not None :
			start = self.findPrevBraket(start)
			i += 1
		return i
	def isEndLine(self,pos):
		return self.editor.textSubstr(pos,pos+1) == "\n" or pos + 1 >= self.editor.textLen()
	# def findLineStart(self,pos):
		# p = self.findAnyNext(pos ,["\n"], -1)
		# if p then p.pos+1 else 0
	def findPrevBraket(self,start):
		return self.findNextBraket(start,-1)
	def findNextBraket(self,start,direction = 1):
		f = self.findAnyNext(start ,[self.brakets,"\n"], direction)
		if f is not None and f['str'] == self.brakets :
			return f['pos']
	# def findPrev(self,start,string) -> 
		# self.findNext(start,string,-1)
	# def findNext(self,start,string,direction = 1):
		# f = self.findAnyNext(start ,[string], direction)
		# f.pos if f
	def findAnyNext(self,start,strings,direction = 1):
		pos = start
		while True :
			if 0 > pos or pos >= self.editor.textLen() :
				return None
			for stri in strings :
			
				start, end = pos, pos + len(stri) * direction
				if end < start :
					start, end = end, start
				if stri == self.editor.textSubstr(start,end) :
					return {
						'str': stri,
						'pos': pos-len(stri) if direction < 0 else pos,
					}
			pos += direction
	# def findMatchingPair(self,startPos,opening,closing,direction = 1):
		# pos = startPos
		# nested = 0
		# while f = self.findAnyNext(pos,[closing,opening],direction)
			# pos = f.pos + (if direction > 0 then len(f.str) else 0)
			# if f.str == (if direction > 0 then closing else opening)
				# if nested > 0
					# nested--
				# else
					# return f
			# else
				# nested++
		# None
	def addBrakets(self,start, end):
		if start == end :
			self.editor.insertTextAt(self.brakets+self.brakets,start)
		else :
			self.editor.insertTextAt(self.brakets,end)
			self.editor.insertTextAt(self.brakets,start)
		self.editor.setCursorPos(end+len(self.brakets))
	# def promptClosingCmd(self,start, end) ->
		# self.closingPromp.stop() if self.closingPromp?
		# self.closingPromp = new Codewave.ClosingPromp(self,start, end)
	# def parseAll(self,recursive = True):
		# pos = 0
		# while cmd = self.nextCmd(pos)
			# pos = cmd.getEndPos()
			# self.editor.setCursorPos(pos)
			# if recursive && cmd.content? 
				# parser = new Codewave(new Codewave.TextParser(cmd.content))
				# cmd.content = parser.parseAll()
			# if cmd.init().execute()?
				# if(cmd.replaceEnd?)
					# pos = cmd.replaceEnd
				# else
					# pos = self.editor.getCursorPos().end
		# self.getText()
	# def getText(self):
		# self.editor.text()
	# def getNameSpaces(self):
		# ['core'].concat(self.nameSpaces)
	# def addNameSpace(self,name):
		# self.nameSpaces.push(name)
	# def removeNameSpace(self,name):
		# self.nameSpaces = self.nameSpaces.filter (n) -> n isnt name
	# def getCmd: (cmdName,nameSpaces = []) ->
		# self.getCmdFrom(cmdName,Codewave,self.getNameSpaces().concat(nameSpaces))
	# def uniformizeCmd(self,cmd):
		# if typeof(cmd) == "function"
				# if cmd.prototype.execute? or cmd.prototype.result?
					# (cls:cmd)
				# else
					# (result:cmd)
			# else if typeof cmd == 'string'
				# (result:cmd)
			# else
				# cmd
	# def prepCmd(self,cmd,path=[]):
		# if(cmd?)
			# cmd = self.uniformizeCmd(cmd)
			# cmd.fullname = path.join(':')
			# if cmd.aliasOf? && (aliassed = self.getCmd(cmd.aliasOf))?
				# cmd = Codewave.util.merge(cmd,aliassed)
				# cmd.aliassed = aliassed 
			# cmd
	# def getCmdFrom(self,cmdName,space,nameSpaces,path = []):
		# if space? and space.cmd?
			# if (p = cmdName.indexOf(':')) > -1
				# cmdNameSpc = cmdName.substring(0,p)
				# cmdNameAfter = cmdName.substring(p+1)
			# for nspc in nameSpaces.reverse()
				# spc = Codewave.getNameSpace(nspc,space)
				# if cmd = self.getCmdFrom(cmdName,spc,nameSpaces,path.concat([nspc]))
					# return cmd
			# if cmdNameSpc? 
				# if cmd = self.getCmdFrom(cmdNameAfter,space.cmd[cmdNameSpc],nameSpaces,path.concat([cmdNameSpc]))
					# return cmd
			# else if space.cmd[cmdName]?
				# self.prepCmd(space.cmd[cmdName],path.concat([cmdName]))
	# def getCommentChar(self):
		# '<!-- %s -->'
	# def wrapComment(self,str):
		# cc = self.getCommentChar()
		# if cc.indexOf('%s') > -1
			# cc.replace('%s',str)
		# else
			# cc + ' ' + str + ' ' + cc
	# def wrapCommentLeft(self,str = ''):
		# cc = self.getCommentChar()
		# console.log()
		# if (i = cc.indexOf('%s')) > -1
			# cc.substr(0,i) + str
		# else
			# cc + ' ' + str
	# def wrapCommentRight(self,str = ''):
		# cc = self.getCommentChar()
		# if (i = cc.indexOf('%s')) > -1
			# str + cc.substr(i+2)
		# else
			# str + ' ' + cc
	# def removeCarret(self,str):
		# re = new RegExp(Codewave.util.escapeRegExp(self.carretChar), "g")
		# str.replace(re,'')