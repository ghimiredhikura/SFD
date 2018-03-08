#!/usr/bin/env bash
root_dir=$(git rev-parse --show-toplevel)
source $root_dir/scripts/data/datasets_utils.sh 

output_dir="${root_dir}/../models/sfd_models/VGGNet/WIDER_FACE/"
drive=$root_dir/scripts/data/google-drive.py

mkdir -p $output_dir
python $drive 1CboBIsjcDQ-FC1rMES6IjTl6sYQDoD6u $output_dir/sfd_models.zip

cd $output_dir
unzip sfd_models.zip
