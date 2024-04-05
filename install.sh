#!/bin/bash

# Get the current directory where PredictBind is cloned
PREDICTBIND_DIR="$(pwd)"

# Define the path to PredictBind Main.py
MAIN_SCRIPT="$PREDICTBIND_DIR/PredictBind/Main.py"

# Check if the PredictBind directory exists
if [ ! -d "$PREDICTBIND_DIR" ]; then
    echo "PredictBind directory not found. Please clone PredictBind repository first."
    exit 1
fi

# Check if Main.py exists
if [ ! -f "$MAIN_SCRIPT" ]; then
    echo "Main.py not found in PredictBind directory. Please ensure PredictBind is set up correctly."
    exit 1
fi

# Define the destination directory for the wrapper script
BIN_DIR="/usr/local/bin"  # Change this to /usr/bin if preferred

# Create the wrapper script
WRAPPER_SCRIPT="$BIN_DIR/PredictBind"
echo "#!/bin/bash" > "$WRAPPER_SCRIPT"
echo "python $MAIN_SCRIPT \"\$@\"" >> "$WRAPPER_SCRIPT"

# Make the wrapper script executable
chmod +x "$WRAPPER_SCRIPT"

echo "PredictBind wrapper script has been installed to $BIN_DIR"
