import inspect

class Default():
	enabled = True
	extension = "default"
	
	whitespace = [
		" ",
		"\t",
		"\n",
		"\r"
	]
	
	singleLineComment = [
		"//"
	]
	
	multiLineCommentOpen = [
		"/*"
	]
	
	multiLineCommentClose = [
		"*/"
	]
	
	ignore = [
		"{",
		"}",
		"[",
		"]",
		"(",
		")"
	]
	
class Java(Default):
	enabled = True
	extension = "java"
	
class CSharp(Default):
	enabled = True
	extension = "cs"
	
class JavaScript(Default):
	enabled = True
	extension = "js"
	
class CPlusPlus(Default):
	enabled = True
	extension = "cpp"
	
class HTML(Default):
	enabled = True
	extension = "html"
	
	singleLineComment = []
	
	multiLineCommentOpen = [
		"<!--"
	]
	
	multiLineCommentClose = [
		"-->"
	]
	
class CSS(Default):
	enabled = True
	extension = "css"
	
	singleLineComment = []
	
class Python(Default):
	enabled = True
	extension = "py"
	
	singleLineComment = [
		"#"
	]
	
	multiLineCommentOpen = [
		'"""'
	]
	
	multiLineCommentClose = [
		'"""'
	]
	
class Yaml(Default):
	enabled = True
	extension = "yml"
	
	whitespace = [
		" ",
		"\n"
	]
	
	singleLineComment = [
		"#"
	]
	
	multiLineCommentOpen = []
	
	multiLineCommentClose = []
	
def getLanguage(extension):
	for subclass in Default.__subclasses__():
		# print("  Subclass: " + str(subclass))
		if subclass.extension == extension:
			return subclass
	return Default