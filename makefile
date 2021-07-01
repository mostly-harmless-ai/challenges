.PHONY: test
test:
	pytest tasks

.PHONY: deploy
deploy:
	python scripts/deploy.py

.PHONY: docs
docs:
	mkdocs gh-deploy --force