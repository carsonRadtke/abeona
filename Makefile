
.PHONY: docs
docs:
	sphinx-build docs docs/build

.PHONY: clean
clean:
	rm -rf build/*
	find . -name '__pycache__' -delete
	find . -name '*.pyc' -delete

.PHONY: test
test:
	pytest
