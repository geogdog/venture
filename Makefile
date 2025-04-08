.DEFAULT_GOAL := help
SHELL := /bin/bash

##@ Setup
.PHONY: init
init: ## Initialise the environment
	@poetry install
	@eval $(poetry env activate)

.PHONY: info
info: ## Show poetry env info
	@poetry env info
	@poetry show --tree

##@ Building and Testing
.PHONY: test
test: ## Run the tests
	@nosetests --rednose tests

.PHONY: build
build: ## Poetry build dist
	@poetry build

.PHONY: dynamic-version
dynamic-version: ## Show poetry dynamic version
	poetry dynamic-versioning show

##@ Helpers
.PHONY: cloc help
cloc:	## Show Lines of Code analysis
	@cloc --vcs git --quiet

help:	## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
