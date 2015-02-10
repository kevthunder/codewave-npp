from codewave import Codewave
import Npp

def _optKey(key,dict): 
	# optional Dictionary key
	return dict[key] if key in dict else None

class Command():
	def __init__(self,name,data=None,parent=None):
		self.name,self.data,self.parent = name,data,parent
		self.cmds = []
		self.resultStr = self.aliasOf = self.cls = self.fullName = None
		self.depth = 0
		self._parent, self._inited = None, False
	@property
	def parent(self):
			return self._parent
	@parent.setter
	def parent(self, value):
		if self._parent != value :
			self._parent = value
			self.fullName = (
				self._parent.name + ':' + self.name 
				if self._parent is not None and self._parent.name is not None 
				else self.name
			)
			self.depth = (
				self._parent.depth + 1
				if self._parent is not None
				else 0
			)
	def init(self):
		if not self._inited :
			self.parseData(self.data)
		return self
	def isExecutable(self):
		for p in ['resultStr','aliasOf','cls'] :
			if getattr(self, p) is not None:
				return True
		return False
	def resultIsAvailable(self):
		for p in ['resultStr'] :
			if getattr(self, p) is not None:
				return True
		return False
	def result(self,instance):
		if self.resultStr is not None:
			return self.resultStr
	def getExecutableObj(self,instance):
		if self.cls is not None :
			return self.cls(instance)
		aliassed = self.getAliassed(instance.codewave)
		if aliassed is not None :
			return aliassed.getExecutableObj(self.aliasOf)
		return self
	def getAliassed(self,codewave = None):
		if codewave is None :
			codewave = Codewave()
		if self.aliasOf is not None :
			return codewave.getCmd(cmd.aliasOf)
	def parseData(self,data):
		self.data = data
		if isinstance(data, str):
			self.resultStr = data
			return True
		elif isinstance(data,dict) :
			return self.parseDictData(data)
		return False
	def parseDictData(self,data):
		self.resultStr = _optKey('result',data)
		self.aliasOf = _optKey('aliasOf',data)
		self.cls = _optKey('cls',data)
		if 'help' in data :
			self.addCmd(self,Command('help',data['help'],self))
		if 'cmds' in data :
			self.addCmds(data['cmds'])
		return True
	def addCmds(self,cmds):
		for name, data in cmds.items() :
			self.addCmd(Command(name,data,self))
	def addCmd(self,cmd):
		cmd.parent = self
		self.cmds.append(cmd)
	def getCmd(self,name):
		for cmd in self.cmds:
			if cmd.name == name:
				return cmd
		
cmds = Command(None,{
  'cmds':{
    'hello':'Hello, World!'
  }
})