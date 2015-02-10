import re
def trimEmptyLine(txt) :
	return re.sub(r'^\n', '', re.sub(r'\n$', '', txt,0,re.M),0,re.M)
def escapeRegExp(txt) :
	return re.escape(txt)
def repeatToLength(txt, length):
   return (txt * ((length/len(txt))+1))[:length]
		
class strPos():
	def __init__(self,pos,str):
		self.pos,self.str = pos,str
	def end(self) :
		self.pos + len(self.str)
