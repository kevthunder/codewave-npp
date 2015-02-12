import command
import core_cmds

reload(command)
reload(core_cmds)



import Npp


class CmdFinder():
	def __init__(self,name,namespaces):
		Npp.console.write('namespaces: '+str(namespaces)+'\n')
		self.name,self.namespaces = name,namespaces
		self.path = self.name.split(":");
		self.baseName = self.path.pop()
		self.root = command.cmds
	def find(self):
		self.cmd = self.findIn(self.root)
		return self.cmd
	def findIn(self,cmd,path = None):
		if cmd is None:
			return None
		if path is None:
			path = list(self.path)
		cmd.init()
		best = self.bestInPosibilities(self.findPosibilitiesIn(cmd,path))
		if best is not None:
			return best
		elif len(path) <= 0:
			direct = cmd.getCmd(self.baseName)
			if direct is not None and direct.init().isExecutable():
				return direct
	def findPosibilitiesIn(self,cmd,path):
		posibilities = []
		if len(path) > 0:
			pos = self.findIn(cmd.getCmd(path[0]),path[1:])
			if pos is not None:
				posibilities.append(pos)
		for nspc in self.namespaces:
			nspcPath = nspc.split(":");
			nspcName = nspcPath.pop()
			pos = self.findIn(cmd.getCmd(nspcName),nspcPath + path)
			if pos is not None:
				posibilities.append(pos)
		return posibilities
	def bestInPosibilities(self,poss):
		if len(poss) > 0:
			best = None
			for p in poss:
				if best is None or p.depth >= best.depth:
					best = p
			return best;