all: html pdf docx rtf coverPdf

pdf: resume.pdf
resume.pdf: resume.md
	pandoc --standalone --template style_chmduquesne.tex \
	--from markdown --to context \
	-V papersize=A4 \
	-o resume.tex resume.md; \
	context resume.tex

coverPdf: coverLetter.pdf
resume.pdf: coverLetter.md
	pandoc --standalone --template style_chmduquesne.tex \
	--from markdown --to context \
	-V papersize=A4 \
	-o coverLetter.tex CoverLetter.md; \
	context coverLetter.tex

html: resume.html
resume.html: style_chmduquesne.css resume.md
	pandoc --standalone -H style_chmduquesne.css \
        --from markdown --to html \
        -o resume.html resume.md

docx: resume.docx
resume.docx: resume.md
	pandoc -s -S resume.md -o resume.docx

rtf: resume.rtf
resume.rtf: resume.md
	pandoc -s -S resume.md -o resume.rtf

clean:
	rm resume.html
	rm resume.tex
	rm resume.tuc
	rm resume.log
	rm resume.pdf
	rm resume.docx
	rm resume.rtf
	rm coverLetter.tex
	rm coverLetter.tuc
	rm coverLetter.log
	rm coverLetter.pdf
