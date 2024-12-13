#!/bin/bash

get_input() {
    source .env

    if [ "$#" -ne 2 ]; then
        echo "Usage: $0 <year> <day>"
        return 1
    fi

    year=$1
    day=$2

    if ! [[ "$year" =~ ^[0-9]{4}$ ]]; then
        echo "Enter year properly (4 digits)"
        return 1
    fi

    if ! [[ "$day" =~ ^[0-9]{1,2}$ ]] || [ "$day" -lt 1 ] || [ "$day" -gt 31 ]; then
        echo "Enter day properly (1-31)"
        return 1
    fi

    urlPath="https://adventofcode.com/$year/day/$day/input"
    curl -s --cookie "$my_cookie" "$urlPath" > "./inputs/day$day.txt" 2>&1
    echo "Fetched the input at ./inputs/day$day.txt."
}

get_input "$@"

if [ $? -ne 0 ]; then
    echo "There was an error with the input."
fi
