all: build/test.pdf

build/test.pdf: exercise.py | build
	python exercise.py

build:
	mkdir -p build

clean:
	rm -rf build
