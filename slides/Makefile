#LECTURES:=lecture1 lecture2 lecture3 lecture4 lecture5b lecture6

NOTEBOOKS:=$(wildcard *.ipynb)
SLIDES:=$(subst ipynb,slides.html,$(NOTEBOOKS))
SLIDES_DECKTAPE:=$(subst ipynb,slides.pdf,$(NOTEBOOKS))
HTML:=$(subst ipynb,html,$(NOTEBOOKS))
PDFS:=$(subst ipynb,pdf,$(NOTEBOOKS))
SPELLCHECKS:=$(subst ipynb,spellcheck.txt,$(NOTEBOOKS))

$(SLIDES): %.slides.html: %.ipynb
	jupyter nbconvert $< --to slides
	# sed 's/\(Reveal\.initialize({\)/\1width: 1400,height: 788,center: false,/' $@ > t.html
	sed 's/\(Reveal\.initialize({\)/\1width: 1400,height: 788,center: false,navigationMode: "linear",/' $@ > t.html
	mv t.html $@ # sed -i doesn't seem to work on my OSX version, doing this move instead

# alternative slides via local reveal clone and decktape:
reveal.js:
	git clone git@github.com:hakimel/reveal.js.git

%.slides-for-decktape.html: %.ipynb reveal.js
	jupyter nbconvert $< --to slides --reveal-prefix reveal.js --output t
	cp t.slides.html $@
    # sed -i doesn't seem to work on my OSX version, using these temp files instead
    #
    # remove the imports Jupyter puts after the title
	sed '/<title>.*<\/title>/s/<script[^>]*><\/script>//g' t.slides.html > t1.html
    #
    # remove the last script initializing Reveal
	tac t1.html | sed '1,/<script>/d' | tac > t2.html
    #
    # put in our custom Reveal initialization
	cat reveal-footer >> t2.html
    #
	mv t2.html $@
	rm t.slides.html t1.html

$(SLIDES_DECKTAPE): %.slides.pdf: %.slides-for-decktape.html
	decktape reveal $< $@

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

slides-decktape:
	make $(SLIDES_DECKTAPE)

pdfs:
	make $(PDFS)

spellchecks:
	make $(SPELLCHECKS)

all-spellchecks.txt: spellchecks
	tail -n 10000 $(SPELLCHECKS) > $@

clean:
	rm -rf *.html *.pdf *spellcheck.txt *_files

all:
	make notes slides pdfs
