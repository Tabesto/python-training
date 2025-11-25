POETRY ?= poetry

GREEN := \033[32m
BLUE := \033[34m
RESET := \033[0m

.PHONY: help install run shell clean

help:
	@printf "$(BLUE)Available targets:$(RESET)\n"
	@printf "$(GREEN)  install$(RESET)  Install project dependencies via Poetry\n"
	@printf "$(GREEN)  run$(RESET)      Start the Flask dev server with Poetry\n"
	@printf "$(GREEN)  shell$(RESET)    Spawn a Poetry-managed shell\n"
	@printf "$(GREEN)  clean$(RESET)    Remove Python cache artifacts\n"

install:
	$(POETRY) install

run:
	$(POETRY) run flask --app app run

shell:
	$(POETRY) shell

clean:
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
	find . -name '*.pyc' -delete

