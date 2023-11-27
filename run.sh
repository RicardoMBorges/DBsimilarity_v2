#!/bin/bash

# Get the directory path where the shell script is located
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if the virtual environment already exists in the script's directory
if [ -f "$script_dir/dbsimilarity_env/bin/activate" ]; then
    echo "dbsimilarity_env already exists. Activating..."
    source "$script_dir/dbsimilarity_env/bin/activate"
else
    echo "Creating virtual environment in $script_dir/dbsimilarity_env..."
    python3.11 -m venv "$script_dir/dbsimilarity_env"
    source "$script_dir/dbsimilarity_env/bin/activate"

    echo "Installing the requirements..."
    "$script_dir/dbsimilarity_env/bin/python" -m pip install -r requirements.txt

    echo "Installing Jupyter Notebook..."
    "$script_dir/dbsimilarity_env/bin/python" -m pip install jupyter notebook==6.5.2
    "$script_dir/dbsimilarity_env/bin/python" -m pip install traitlets==5.9.0
fi

# Start Jupyter Notebook
jupyter notebook

# You may add 'read' command here to pause the script before exiting
# read -p "Press Enter to exit..."
