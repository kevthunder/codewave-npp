import storage
import logger
reload(storage)

def _optKey(key,dict,defVal = None): 
	# optional Dictionary key
	return dict[key] if key in dict else defVal

cmdIniters = set()
def initCmds():
	global cmds
	global cmdIniters
	cmds = Command(None,{
		'cmds':{
			'hello':'Hello, World!'
		}
	})
	for initer in cmdIniters:
		initer()

def saveCmd(fullname,data):
	global cmds
	cmds.setCmd(fullname,Command(fullname.split(':').pop(),data))
	savedCmds = storage.load('cmds')
	if savedCmds is None :
		savedCmds = {}
	savedCmds[fullname] = data
	storage.save('cmds',savedCmds)

def loadCmds():
	global cmds
	savedCmds = storage.load('cmds')
	if savedCmds is not None :
		for fullname, data in savedCmds.iteritems():
			cmds.setCmd(fullname,Command(fullname.split(':').pop(),data))

	
class Command():
	def __init__(self,name,data=None,parent=None):
		self.name,self.data = name,data
		self.cmds = []
		self.detectors = []
		self.executeFunct = self.resultFunct = self.resultStr = self.aliasOf = self.cls = None
		self.aliassed = None
		self.fullName = self.name
		self.depth = 0
		self._parent, self._inited = None, False
		self.setParent(parent)
		self.defaults = {}
		self.nameToParam = None
	@property
	def parent(self):
			return self._parent
	@parent.setter
	def parent(self, value):
		self.setParent(value)
	def setParent(self, value):
		if self._parent != value :
			self._parent = value
			self.fullName = (
				self._parent.fullName + ':' + self.name 
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
			self._inited = True
			self.parseData(self.data)
		return self
	def isEditable(self):
		return self.resultStr is not None
	def isExecutable(self):
		for p in ['resultStr','resultFunct','aliasOf','cls','executeFunct'] :
			if getattr(self, p) is not None:
				return True
		return False
	def resultIsAvailable(self,instance = None):
		if instance is not None and instance.cmdObj is not None:
			return instance.cmdObj.resultIsAvailable()
		for p in ['resultStr','resultFunct'] :
			if getattr(self, p) is not None:
				return True
		return False
	def getDefaults(self,instance = None):
		res = {}
		aliassed = self.getAliassed(instance.codewave)
		if aliassed is not None :
			res.update(aliassed.getDefaults(instance))
		res.update(self.defaults)
		if instance is not None and instance.cmdObj is not None:
			res.update(instance.cmdObj.getDefaults())
		return res;
	def result(self,instance):
		if instance.cmdObj is not None:
			return instance.cmdObj.result()
		aliassed = self.getAliassed(instance.codewave)
		if aliassed is not None :
			return aliassed.result(instance)
		if self.resultFunct is not None:
			return self.resultFunct(instance)
		if self.resultStr is not None:
			return self.resultStr
	def execute(self,instance):
		if instance.cmdObj is not None:
			return instance.cmdObj.execute()
		aliassed = self.getAliassed(instance.codewave)
		if aliassed is not None :
			return aliassed.execute(instance)
		if self.executeFunct is not None:
			return self.executeFunct(instance)
	def getExecutableObj(self,instance):
		self.init()
		if self.cls is not None :
			return self.cls(instance)
		aliassed = self.getAliassed(instance.codewave)
		if aliassed is not None :
			return aliassed.getExecutableObj(instance)
	def getAliassed(self,codewave = None):
		if self.aliasOf is not None :
			if self.aliassed is None :
				if codewave is None :
					from codewave import Codewave
					codewave = Codewave()
				self.aliassed = codewave.getCmd(self.aliasOf) or False
			return self.aliassed or None
	def parseData(self,data):
		self.data = data
		if isinstance(data, str):
			self.resultStr = data
			return True
		elif isinstance(data,dict) :
			return self.parseDictData(data)
		return False
	def parseDictData(self,data):
		res = _optKey('result',data)
		if hasattr(res, '__call__') :
			self.resultFunct = res
		else :
			self.resultStr = res
		execute = _optKey('execute',data)
		if hasattr(execute, '__call__') :
			self.executeFunct = execute
		self.aliasOf = _optKey('aliasOf',data)
		self.cls = _optKey('cls',data)
		self.defaults = _optKey('defaults',data,self.defaults)
		self.nameToParam = _optKey('nameToParam',data)
		if 'help' in data :
			self.addCmd(self,Command('help',data['help'],self))
		if 'fallback' in data :
			self.addCmd(self,Command('fallback',data['fallback'],self))
		if 'cmds' in data :
			self.addCmds(data['cmds'])
		return True
	def addCmds(self,cmds):
		for name, data in cmds.items() :
			self.addCmd(Command(name,data,self))
	def addCmd(self,cmd):
		exists = self.getCmd(cmd.name)
		if exists is not None :
			self.removeCmd(exists)
			# exists.name = 'super'
			# cmd.addCmd(exists)
		cmd.setParent(self)
		self.cmds.append(cmd)
		return cmd
	def removeCmd(self,cmd):
		self.cmds.remove(cmd)
		return cmd
	def getCmd(self,fullname):
		self.init()
		parts = fullname.split(':',1)
		name = parts.pop()
		if len(parts) > 0 :
			return self.getCmd(parts[0]).getCmd(name)
		for cmd in self.cmds:
			if cmd.name == name:
				return cmd
	def setCmd(self,fullname,cmd):
		parts = fullname.split(':',1)
		name = parts.pop()
		if len(parts) > 0 :
			next = self.getCmd(parts[0])
			if next is None :
				next = self.addCmd(Command(parts[0]))
			return next.setCmd(name,cmd)
		else:
			self.addCmd(cmd)
			return cmd
	def addDetector(self,detector):
		self.detectors.append(detector)
			
	
class BaseCommand():
	def __init__(self,instance):
		self.instance = instance
	def resultIsAvailable(self):
		return hasattr(self,"result")
	def getDefaults(self):
		return {}
				
				