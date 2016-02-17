import os
import languages

# # # # #
# Make sure this is set before starting. You can change it from os.getCwd()
# to whatever directory you want to start in
directory = os.getCwd()
# # # # #

def getSlocInFile(filepath):
	
	bits = filename.split(".")
	if len(bits) > 0:
		format = languages.getLanguage(bits[len(bits) - 1])
		if format != languages.Default:
			infile = open(dirName + "\\" + filename, "r")
			
			fileSloc = 0
			
			inMLC = False
			
			for line in infile:
				# print("Examining line: " + line.replace("\n",""))
				if not inMLC:
					# print("Not in MLC")
					inSLC = False
					for w in format.whitespace: line = line.replace(w, "")
					# print("Trimmed Line: " + line)
					if len(line) > 0:
						for m in format.multiLineCommentOpen:
							if line.find(m) == 0:
								inMLC = True
								# print("Found multi-line comment start: " + m)
								break
						if len(line) == 1:
							if line[0] in format.ignore or line[0] in format.singleLineComment:
								# print("Ignore or SLC found, skipping: " + line[0])
								continue
						for s in format.singleLineComment:
							if line[0] == s:
								# print("Found SLC: " + line[0])
								inSLC = True
								break
						if not inSLC and not inMLC:
							# print("not in any comment")
							fileSloc = fileSloc + 1
							for m in format.multiLineCommentOpen:
								if m in line:
									# print("MLC start found: " + m)
									inMLC = True
									break
				else:
					# print("in MLC")
					for m in format.multiLineCommentClose:
						if m in line:
							# print("MLC close found: " + m)
							inMLC = False
							break
			
			infile.close()
			return fileSloc
	return 0


totalSloc = 0
maxFileSloc = 0
maxSlocFile = ""
slocByLanguage = {}

for dirName, subdirList, fileList in os.walk(directory):
	try:
		if (dirName.find(".git") > -1): continue
		print("Found dirName: " + dirName)
	except:
		print("Found a directory that pyton can't print")
	for subdir in subdirList: 
		try:
			print("Found subdir: " + str(subdir))
		except:
			print("Found a subdir that python can't print.")
	for filename in fileList:
		try:
			print("Found file: " + filename)
		except:
			print("Found a file that python can't print")
		#try:
		if filename != "sloccer.py" and filename != "languages.py":
			path = dirName + "\\" + filename
			if "." in filename:
				extension = filename.split(".")[1]
				fileSloc = getSlocInFile(path)
				print("fileSloc: " + str(fileSloc))
				if fileSloc > 0:
					totalSloc = totalSloc + fileSloc
					if languages.getLanguage(extension).extension in slocByLanguage:
						slocByLanguage[extension] = slocByLanguage[extension] + fileSloc
					else:
						slocByLanguage[extension] = fileSloc
					if fileSloc > maxFileSloc:
						maxFileSloc = fileSloc
						maxSlocFile = path
		else: print("Skipping the files for this script.")
		"""except:
			print("Couldn't parse " + dirName + "\\" + filename)"""
			

messages = [
	"",
	"=" * 15,
	"| RESULTS",
	"| Total Sloc: " + str(totalSloc),
	"| Most Sloc in a file: " + str(maxFileSloc),
	"| File: " + maxSlocFile
]

for m in messages: print(m)

print("| Sloc By Language: ")
for l in slocByLanguage:
	print("|    " + l + ": " + str(slocByLanguage[l]))
print("=" * 15)