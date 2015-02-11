import command
import codewave
import util
import Npp

core = command.cmds.addCmd(command.Command('core'))


# def no_execute(instance)
	# reg = re.compire("^"+util.escapeRegExp(instance.codewave.brakets) + util.escapeRegExp(instance.codewave.noExecuteChar))
  # return re.sub(reg, '', instance.str)
		
# core.addCmd(command.Command('no_execute',{
	# 'result' : no_execute
# }))

# def exec_parent(instance)
	# if instance.parent is not None:
		# return instance.parent.execute()
		
# core.addCmd(command.Command('exec_parent',{
	# 'execute' : exec_parent
# }))


class BoxCmd(command.BaseCommand):
	def __init__(self,instance):
		self.instance = instance
		if self.instance.content:
			bounds = self.textBounds(self.instance.content)
			self.width,self.height = bounds.width, bounds.height
		else:
			self.width = 50
			self.height = 3
		
		params = ['width']
		if len(self.instance.params) > 1 :
			params.append(0)
		self.width = self.instance.getParam(params,self.width)
			
		params = ['height']
		if len(self.instance.params) > 1 :
			params.append(1)
		elif len(self.instance.params) > 0:
			params.append(0)
		self.height = self.instance.getParam(params,self.height)
		
		self.cmd = self.instance.getParam(['cmd'])
		self.deco = self.instance.codewave.deco
		self.pad = 2
	def result(self,instance):
		return self.startSep() + "\n" + self.lines(self.instance.content) + "\n"+ self.endSep()
	def wrapComment(self,str):
		return self.instance.codewave.wrapComment(str)
	def separator(self):
		len = self.width + 2 * self.pad + 2 * len(self.deco)
		return self.wrapComment(self.decoLine(len))
	def startSep(self):
		cmd = ''
		if self.cmd is not None:
			cmd = self.instance.codewave.brakets+self.cmd+self.instance.codewave.brakets
		ln = self.width + 2 * self.pad + 2 * len(self.deco) - len(cmd)
		return self.wrapComment(cmd+self.decoLine(ln))
	def endSep(self):
		closing = ''
		if self.cmd is not None:
			closing = self.instance.codewave.brakets+self.instance.codewave.closeChar+self.cmd.split(" ")[0]+self.instance.codewave.brakets
		ln = self.width + 2 * self.pad + 2 * len(self.deco) - len(closing)
		return self.wrapComment(closing+self.decoLine(ln))
	def decoLine(self,len):
		return util.repeatToLength(self.deco, len)
	def padding(self): 
		return util.repeatToLength(" ", self.pad)
	def lines(self,text = ''):
		text = text or ''
		lines = text.replace('\r','').split("\n")
		return "\n".join([self.line(lines[x] if x < len(lines) else '') for x in range(0,self.height)]) 
	def line(self,text = ''):
		return self.wrapComment(
				self.deco + 
				self.padding() + 
				text + 
				util.repeatToLength(" ", self.width-len(self.instance.codewave.removeCarret(text))) + 
				self.padding() + 
				self.deco
			)
	def textBounds(self,text):
		return util.getTxtSize(self.instance.codewave.removeCarret(text))
		

core.addCmd(command.Command('box',{
	'cls' : BoxCmd
}))

# class CloseCmd(command.BaseCommand):
	# def __init__(self,instance):
		# self.instance = instance
		# self.deco = self.instance.codewave.deco
	# def startFind(self):
		# self.instance.codewave.wrapCommentLeft(self.deco + self.deco)
	# def endFind(self):
		# self.instance.codewave.wrapCommentRight(self.deco + self.deco)
	# def execute(self):
		# startFind = self.startFind()
		# endFind = self.endFind()
		# start = self.instance.codewave.findPrev(self.instance.pos, startFind)
		# end = self.instance.codewave.findNext(self.instance.getEndPos(), endFind) + len(endFind)
		# if start? and end?:
			# self.instance.codewave.editor.spliceText(start,end,'')
			# self.instance.codewave.editor.setCursorPos(start)
		# else:
			# self.instance.replaceWith('')


# core.addCmd(command.Command('close',{
	# 'cls' : CloseCmd
# }))

# class EditCmd(command.BaseCommand):
	# def __init__(self,instance):
		# self.instance = instance
		# self.cmdName = self.instance.getParam([0,'cmd'])
		# self.verbalize = self.instance.getParam([1]) in ['v','verbalize']
		# self.cmd = self.instance.codewave.getCmd(self.cmdName) if self.cmdName is not None else None
		# self.editable = self.cmd.isEditable() if self.cmd is not None else None
		# self.content = self.instance.content
	# def result(self,instance):
		# if self.cmd:
			# if self.content:
				# return self.resultWithContent()
			# else:
				# return self.resultWithoutContent()
	# def resultWithContent(self):
			# parser = codewave.Codewave(text_parser.TextParser(self.content))
			# parser.addNameSpace(self.instance.cmd.fullname)
			# parser.parseAll()
			# console.log(parser);
			# Codewave.setCmd(self.cmdName,command.Command(self.cmdName,{
				# 'result': parser.vars.source
			# }))
			# return ''
	# def resultWithoutContent(self):
		# if self.editable:
			# parser = codewave.Codewave(text_parser.Codewave.TextParser(
				# """~~box cmd:"%(cmd)"~~
				# ~~source~~
				# %(source)
				# ~~/source~~
				# ~~save~~ ~~!close~~
				# ~~/box~~""" % {'cmd': 'self.cmd.name', 'source': "self.cmd.result"}))
			# parser.checkCarret = no
			# return parser.getText() if self.verbalize else parser.parseAll()
		
# core.addCmd(command.Command('edit',{
	# 'cmds' : {
		# 'save':{
      # 'aliasOf': 'core:exec_parent'
		# }
	# },
	# 'cls' : EditCmd
# }))
