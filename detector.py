
class Detector():
	def __init__(self,data={}):
		self.data = data
	def detect(self,finder):
		pass
		

class LangDetector(Detector):
	def detect(self,finder):
		return finder.instance.codewave.editor.getLang().lower()