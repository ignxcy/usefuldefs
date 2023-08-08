#!/usr/bin/sh

if [ $(id -u) -eq 0 ]; then
    echo "yes"
else
    echo "no"
fi
