install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here

generate_and_push:
	python main.py 
	git config --local user.email "jay.liu011016@gmail.com"
	git config --local user.name "jayliu1016"
	git add .
	@if ! git diff --cached --quiet; then \
		git commit -m "Auto-generated commit"; \
		git push; \
	else \
		echo "No changes to commit"; \
	fi

all: install lint test format generate_and_push
