#!/bin/bash
# Manual deactivation script
unset VIRTUAL_ENV
if [ -n "$_OLD_VIRTUAL_PATH" ]; then
    PATH="$_OLD_VIRTUAL_PATH"
    export PATH
    unset _OLD_VIRTUAL_PATH
fi
if [ -n "$_OLD_VIRTUAL_PS1" ]; then
    PS1="$_OLD_VIRTUAL_PS1"
    export PS1
    unset _OLD_VIRTUAL_PS1
fi

echo "Virtual environment manually deactivated."
