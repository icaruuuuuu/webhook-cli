APP_PATH := $(shell pwd)/app/webhook-cli.py

ifeq ($(findstring fish,$(SHELL)),fish)
	fish_add_path ~/bin
endif

install:
	mkdir -p ~/bin
	cp $(APP_PATH) ~/bin/webhook-cli

uninstall:
	rm ~/bin/webhook-cli
