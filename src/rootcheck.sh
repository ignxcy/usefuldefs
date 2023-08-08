#!/usr/bin/sh

if [ $(id -u) -eq 0 ]; then
    echo "The current user is root."
else
    echo "The current user is not root."
fi
