.DEFAULT_GOAL := help
SHELL := /bin/bash

init:
	@pipenv install
	@pipenv shell

##@ Building and Testing
test:
	@nosetests --rednose tests

build:
	@python setup.py build

##@ Docs
.PHONY: docs
docs: ## Build the sphinx docs
	@$(MAKE) -C docs html

##@ Helpers
.PHONY: cloc help
cloc:	## Show Lines of Code analysis
	@cloc --vcs git --quiet

help:	## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
