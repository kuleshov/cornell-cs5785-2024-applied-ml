#LECTURES:=lecture1 lecture2 lecture3 lecture4 lecture5b lecture6

NOTEBOOKS:=$(wildcard *.ipynb)
SLIDES:=$(subst ipynb,slides.html,$(NOTEBOOKS))
HTML:=$(subst ipynb,html,$(NOTEBOOKS))
PDFS:=$(subst ipynb,pdf,$(NOTEBOOKS))
SPELLCHECKS:=$(subst ipynb,spellcheck.txt,$(NOTEBOOKS))

$(SLIDES): %.slides.html: %.ipynb
	jupyter nbconvert $< --to slides
	sed 's/\(Reveal\.initialize({\)/\1width: 1400,height: 788,center: false,/' $@ > t.html
	mv t.html $@ # sed -i doesn't seem to work on my OSX version, doing this move instead


$(HTML): %.html: %.ipynb
	jupyter nbconvert $< --to html_embed

$(PDFS): %.pdf: %.ipynb
	jupyter nbconvert $< --to pdf

%.spellcheck.txt: %.ipynb
	./extract-markdown.py $< | aspell --mode=tex list > $@

notes:
	make $(HTML)

slides:
	make $(SLIDES)

pdfs:
	make $(PDFS)

spellchecks:
	make $(SPELLCHECKS)

clean:
	rm -rf *.html *.pdf *spellcheck.txt *_files

all:
	make notes slides pdfs
