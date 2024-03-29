.DEFAULT_GOAL := build
SHELL := /bin/bash
# ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
MODSYS := $(HOME)/modsys
export MODSYS

# LINTS
lint-commit-messages:
	./scripts/lint-messages.sh


test-lint:
	pre-commit install
	pre-commit run --all-files


# BUILD
build-run:
	docker compose up -d
