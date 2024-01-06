#!/bin/bash

# # Detecting the shell type
# if [[ $SHELL == */bash ]]; then
#     PROFILE_FILE="$HOME/.bashrc"
#     echo "Detected Bash shell. Modifying $PROFILE_FILE"
# elif [[ $SHELL == */zsh ]]; then
#     PROFILE_FILE="$HOME/.zshrc"
#     echo "Detected Zsh shell. Modifying $PROFILE_FILE"
# else
#     echo "Unsupported shell. Exiting script."
#     exit 1
# fi


SCRIPT_PATH=("./scripts/builder/builder.py")

# Build binary executables for scripts
for path in "${SCRIPT_PATH[@]}"; do
    echo poetry run pyinstaller $path --workpath='xc/build' --distpath='xc/dist' --specpath='xc' --log-level=WARN --noconfirm
    poetry run pyinstaller $path --workpath='xc/build' --distpath='xc/dist' --specpath='xc' --log-level=WARN --noconfirm
done

alias builder=./xc/dist/builder/builder
