# Requirements for automating resume creation.

These automation requirements will layout the plan to simply 
1. open a resume in a text editor and make edits
2. simply run 'make' on the terminal and have the resume copied to the appropriate directory depending oon the file extension; and the name of the resume will be named after the company for which it will be submitted.

Directory Structure:
+-- ~/Resume
	+-- [year for which the resume is created]
		+-- src  - contains markdown source files
		+-- out
			+-- docx
			+-- rtf
			+-- pdf
			+-- tex
			+-- html
			+-- log  - to be removed
			+-- tuc  - to be removed
	+-- pandoc-resume  - software for creating the output resumes
	+-- tmp  - temporary directory to hold software and a copy of a resume
		pandoc-resume-copy
		resume.md
		middleMan.py


The tmp directory will hold a copy of the pandoc-resume software, and a copy of the resume from ~/Resume/[year]/src/uniqueResume.md.
In tmp, the resume will be created using 'make' and middleMan.py will copy
the final resume to the appropriate directory in ~/Resume/[year]/out/
and will also give it a useful name in the format of
RobinsonCoryResume[companyName].ext.  This useful naming convention will
be implemented by the user in the 'src' directory where the resume will be
initiated and edited.  Once resume editing is complete the automated software will take control upon the user entering the 'make' command.