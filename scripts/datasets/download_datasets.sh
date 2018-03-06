#!/usr/bin/env bash

root_dir=$(git rev-parse --show-toplevel)

function help_message {
    echo "Valid options:"
    echo "    -d    Directory where to download all the datasets"
}

function invalid_option {
    # $1 is the OPTARG that was wrong
    # $2 is the script name ($0)
    echo "Invalid option: -$1" >&2
    echo "Execute:"
    echo "$2 -h"
    echo "to read a list of valid parameters."
}

unset option
while getopts :d: option; do
    case $option in
        d)
          directory=$OPTARG
          ;;
        h)
          help_message
          exit 0
          ;;
        \?)
          invalid_option $OPTARG $0
          exit 1
          ;;
    esac
done

if [[ -z $directory ]]
then
    echo "You must provide a valid directory where to download the datasets with option -d"
fi

if [[ ! -d $directory ]]
then
    mkdir -p $directory
fi

for name in "afw" "fddb" # "pascal" "wider"
do
    $root_dir/scripts/datasets/download_${name}.sh $directory
done
