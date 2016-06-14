import os
import datetime
import shutil



# get the system date.  only year is needed in the form 'yyyy'
now = datetime.datetime.now()
year = str(now.year)

# name the output directories
tmpDir = os.path.expanduser("~/Resume/tmp/")
resDir = os.path.expanduser("~/Resume/" + year)
outDir = os.path.expanduser(resDir + "/out/")
outDocx = os.path.expanduser(outDir + "/docx/")
outPdf = os.path.expanduser(outDir + "/pdf/")
outRtf = os.path.expanduser(outDir + "/rtf/")
outTex = os.path.expanduser(outDir + "/tex/")
outHtml = os.path.expanduser(outDir + "/html/")


# find name of the real output file's name... .blank file
for srcFile in os.listdir(tmpDir):
	ext = os.path.splitext(srcFile)[1]
	if ext == '.blank':
		outFileName = os.path.splitext(srcFile)[0]


for srcFile in os.listdir(tmpDir):
	ext = os.path.splitext(srcFile)[1]
	if ext == '.docx':
		shutil.copy(tmpDir + srcFile, outDocx + outFileName + ".docx")
	elif ext == '.pdf':
		shutil.copy(tmpDir + srcFile, outPdf + outFileName + ".pdf")
	elif ext == '.rtf':
		shutil.copy(tmpDir + srcFile, outRtf + outFileName + ".rtf")
	elif ext == '.tex':
		shutil.copy(tmpDir + srcFile, outTex + outFileName + ".tex")
	elif ext == '.html':
		shutil.copy(tmpDir + srcFile, outHtml + outFileName + ".html")