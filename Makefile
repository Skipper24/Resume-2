all: pyResCreator html pdf move docx rtf pyResCleanup


pyResCreator:
	python middleMan.py

pdf: tmp/resume.pdf
tmp/resume.pdf: tmp/resume.md
	pandoc --standalone --template tmp/style_chmduquesne.tex \
	--from markdown --to context \
	-V papersize=A4 \
	-o tmp/resume.tex tmp/resume.md; \
	context tmp/resume.tex

move:
	mv resume.pdf resume.log resume.tuc tmp

html: tmp/resume.html
tmp/resume.html: tmp/style_chmduquesne.css tmp/resume.md
	pandoc --standalone -H tmp/style_chmduquesne.css \
        --from markdown --to html \
        -o tmp/resume.html tmp/resume.md

docx: tmp/resume.docx
tmp/resume.docx: tmp/resume.md
	pandoc -s -S tmp/resume.md -o tmp/resume.docx

rtf: tmp/resume.rtf
tmp/resume.rtf: tmp/resume.md
	pandoc -s -S tmp/resume.md -o tmp/resume.rtf

pyResCleanup:
	python cleanup.py

clean:
	rm -rf tmp
#	rm resume.html
#	rm resume.tex
#	rm resume.tuc
#	rm resume.log
#	rm resume.pdf
#	rm resume.docx
#	rm resume.rtf
