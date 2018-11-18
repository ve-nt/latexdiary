main: main.tex entries.py
	python3 entries.py
	pdflatex main.tex

clean: 
	rm main.aux main.log main.out main.pdf entries.tex 
