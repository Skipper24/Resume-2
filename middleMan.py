import os
import datetime
import shutil



# get the system date.  only year is needed in the form 'yyyy'
now = datetime.datetime.now()
year = str(now.year)


# if path ~/Resume/[currentYear]/ doesn't exist, create it.
resDir = os.path.expanduser("~/Resume/" + year)
print resDir
if not os.path.exists(resDir):
	try:
		print "Creating new directory for year %s" % year
		os.makedirs(resDir)
	except OSError as exc: # guard against race condition
		if exc.errno != errno.EEXIST:
			raise

# create src and out directories with out's subdirectories within
# the [year] directory; i.e. if they do not already exist
srcDir = os.path.expanduser("~/Resume/" + year + "/src")
outDir = os.path.expanduser("~/Resume/" + year + "/out")
outDocx = os.path.expanduser(outDir + "/docx")
outPdf = os.path.expanduser(outDir + "/pdf")
outRtf = os.path.expanduser(outDir + "/rtf")
outTex = os.path.expanduser(outDir + "/tex")
outHtml = os.path.expanduser(outDir + "/html")
outLog = os.path.expanduser(outDir + "/log")
outTuc = os.path.expanduser(outDir + "/tuc")
places = [srcDir, outDir, outDocx, outPdf, outRtf,
	outTex, outHtml, outLog, outTuc]
for p in places:
	if not os.path.exists(p):
		try:
			print "Creating new directory -- %s" % p
			os.makedirs(p)
		except OSError as exc: # guard against race condition
			if exc.errno != errno.EEXIST:
				raise


# create the temporary directory... ~/Resume/tmp
# first check if tmp exists, and delete it if so
# then create a new tmp directory
tmpDir = os.path.expanduser("~/Resume/tmp")
if os.path.exists(tmpDir):
	print "Removing %s" % tmpDir
	shutil.rmtree(tmpDir)	# remove directory and all its contents
if not os.path.exists(tmpDir):
	try:
		print "Creating a temporary directory, %s" % tmpDir
		os.makedirs(tmpDir)
	except OSError as exc:
		if exc.errno != errno.EEXIST:
			raise


# copy pandoc-resume software to tmp
pdResDir = os.path.expanduser("~/Resume/pandoc-resume/pandoc_resume/")
for srcFiles in os.listdir(pdResDir):
	pathFileName = os.path.join(pdResDir, srcFiles)
	if (os.path.isfile(pathFileName)):
		if not srcFiles == 'resume.md':
			shutil.copy(pathFileName, tmpDir)


# get user input on which resume to copy from src to tmp
companyName = raw_input("Which resume do you want to build?  ")
resumeName = "CoryRobinsonResume" + companyName + ".md"


# assuming that resumeName is in the 'year' directory, copy it to tmp
# as resume.md
print "Copying %s from the %s directory" % (resumeName, year)
shutil.copy(srcDir + "/" + resumeName, tmpDir + "/resume.md")
open(tmpDir + "/CoryRobinsonResume" + companyName + ".blank", "w").close()