#!/usr/bin/env bash

root_dir=$(git rev-parse --show-toplevel)
source $root_dir/scripts/data/datasets_utils.sh 

dst_dir=$1
output_dir=$(create_folder "$dst_dir" "PASCAL")

# We are going to user PJRedmon's mirrors
wget http://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar -O $output_dir/VOCtrainval_11-May-2012.tar
wget http://pjreddie.com/media/files/VOC2012test.tar -O $output_dir/VOC2012test.tar

cd $output_dir
# The structure of both archives is the same, so training and testing images should be
# inside VOCdevkit/VOC2012/JPEGImages after uncompressing the files
tar xfv VOCtrainval_11-May-2012.tar
tar xfv VOC2012test.tar
