#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <day> <part>"
    exit 1
fi

day=$1
part=$2

file="solutions/day$day.py"

if [ -f "$file" ]; then
    clear
    echo "Running $file - Part $part"
    echo "-----------------------------------"
    python3 "$file" "$part"
else
    echo "Error: $file does not exist."
    exit 1
fi