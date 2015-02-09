class Command():
	def __init__(self,name,data=None,parent=None):
		self.name,self.data,self.parent = name,data,parent
		self.cmds = []
		self.result = self.aliasOf = self.cls = self.fullName = None
		self.depth, self.executable = 0, False
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
	def parseData(self,data):
		self.data = data
		if isinstance(data, str):
			self.result = str
			self.executable = True
			return True
		elif isinstance(data,dict) :
			return parseDictData(data)
		return False
	def parseDictData(self,data):
		execProps = ['result','aliasOf','cls']
		for p in execProps :
			if p in self.data:
				setattr(self, p, self.data[p])
				self.executable = True
		if 'help' in self.data :
			self.addCmd(self,Command('help',self.data['help'],self))
		if 'cmds' in self.data :
			self.addCmds(self.data['cmds'])
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
		
cmds = Command(None)