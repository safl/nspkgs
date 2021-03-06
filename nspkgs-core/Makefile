#
# This Makefile serves as convenient command-line auto-completion
#
PROJECT_NAME=nspkgs

define default-help
# invoke: 'make uninstall', 'make install'
endef
.PHONY: default
default: build
	@echo "## py: make default"
	@echo "## py: make default [DONE]"

define  all-help
# Do all: clean uninstall build install
endef
.PHONY: all
all: uninstall clean build install

define build-help
# Build the package (source distribution package)
endef
.PHONY: build
build:
	@echo "## py: make build-sdist"
	@python3 setup.py sdist
	@echo "## py: make build-sdist [DONE]"

define install-help
# install for current user
endef
.PHONY: install
install:
	@echo "## py: make install"
	@python3 -m pip install dist/*.tar.gz --user
	@echo "## py: make install [DONE]"

define uninstall-help
# uninstall
#
# Prefix with 'sudo' when uninstalling a system-wide installation
endef
.PHONY: uninstall
uninstall:
	@echo "## py: make uninstall"
	@python3 -m pip uninstall ${PROJECT_NAME} --yes || echo "Cannot uninstall => That is OK"
	@echo "## py: make uninstall [DONE]"

define install-system-help
# install system-wide
#
# install system-wide
endef
.PHONY: install-system
install-system:
	@echo "## py: make install-system"
	@python3 -m pip install dist/*.tar.gz
	@echo "## py: make install-system [DONE]"

define test-help
# Run pytest on tests/
endef
.PHONY: test
test:
	@echo "## py: make test"
	@python3 -m pytest --pyargs ${PROJECT_NAME}
	@echo "## py: make test [DONE]"

define clean-help
# clean the Python build dirs (build, dist)
endef
.PHONY: clean
clean:
	@echo "## py: clean"
	@rm -r build || echo "Cannot remove => That is OK"
	@rm -r dist || echo "Cannot remove => That is OK"
	@rm -r *.egg-info || echo "Cannot remove => That is OK"
	@echo "## py: clean [DONE]"
