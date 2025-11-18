# Basic knobs you can tweak if needed.
# ?= means “use this default unless you pass an override, e.g. make run HOST=0.0.0.0”
PYTHON ?= python3
VENV ?= .venv
UVICORN ?= uvicorn
APP ?= main:app
HOST ?= 127.0.0.1
PORT ?= 8000

# .PHONY tells make that these words are “commands”, not filenames.
.PHONY: help venv install run stop restart clean

# Show a quick cheat sheet without reading README.
help:
	@echo "Common backend commands:"
	@echo "  make venv     # create virtualenv ($(VENV))"
	@echo "  make install  # install dependencies into $(VENV)"
	@echo "  make run      # start FastAPI dev server with reload"
	@echo "  make stop     # stop any running uvicorn processes for this app"
	@echo "  make restart  # stop + run"
	@echo "  make clean    # remove virtualenv"

# Create the virtual environment only if it does not exist yet.
$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)

# Convenience alias so you can just type “make venv”.
venv: $(VENV)/bin/activate

# Install requirements inside the virtualenv.
install: venv
	. $(VENV)/bin/activate && pip install -r requirements.txt

# Main entrypoint: ensures deps are ready, then launches FastAPI with auto-reload.
run: install
	. $(VENV)/bin/activate && $(UVICORN) $(APP) --reload --host $(HOST) --port $(PORT)

# Stop anything previously launched with uvicorn main:app
stop:
	# pkill exits with non-zero when nothing is running, so “-” tells make to ignore that error
	- pkill -f "$(UVICORN) $(APP)"

# Restart is just stop + run.
restart: stop
	$(MAKE) run

# Blow away the virtualenv so you can start fresh (e.g., when deps change drastically).
clean:
	rm -rf $(VENV)

