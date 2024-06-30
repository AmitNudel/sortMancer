#!/bin/bash

VENV_DIR="../venv"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$SCRIPT_DIR"
cd "$PROJECT_ROOT"


#Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment..."
  python3 -m venv "$VENV_DIR"
else
  echo "Virtual environment already exists."
fi

source "$VENV_DIR/bin/activate"

source ./scripts/update_requirements.sh

echo "Virtual environment is activated. You can now start working on your project."

exec "$SHELL"
