The middleMan.py automation to mszep/pandoc_resume - The Markdown Resume
===================

The middleMan.py acts as a "middle man" between a slightly modified 
pandoc_resume, (PR), and your own resume source file. It simply copies your resume source file into a temporary directory with the PR software, and once the software builds all of the output forms of the resume, they will be copied into an organized directory structure containing .pdf, .tex, .rtf, .docx, etc. outputs.

Instructions:

    git clone https://github.com/creedr/Resume
    cd Resume/[year]/src
    vim [yourResume].md   #insert your own resume info
	cd ../../
    make

When prompted for your resume name input, all you should need to do is type in the company name like:
	CompanyA  
that is if you resume file is named like myNameCompanyA.md

Note: middleMan.py does not yet recognize a general userName in the resume file.  It is still specific to my own name. You will need to modify middleMan.py to accommodate your own resume naming convention for the time being.

You may want to mkdir [year] with whatever year we are currently in.

You may need to run make twice to ensure that LaTex builds the .pdf output correctly.

#TODO
* generalize resume naming convention
* add feature to generate a user edited cover letter with same heading as in the resume.

Requirements:

 * ConTeXt
 * pandoc
