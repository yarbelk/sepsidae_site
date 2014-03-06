PROJECT=sepsidae_site

develop: setup-git
	pip install -r requirements.txt
	pip install -e .

setup-git:
	cd .git/hooks && ln -sf ../../hooks/* ./

lint-python:
	@echo "Linting Python files"
	PYFLAKES_NODOCTEST=1 flake8 src/$(PROJECT)
	@echo ""

install-test-requirements:
	pip install -r requirements.txt

test: install-test-requirements test-python

test-python:
	cd src/$(PROJECT) && python manage.py test --settings=conf.settings.test
