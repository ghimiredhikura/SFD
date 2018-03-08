#!/usr/bin/env bash

root_dir=$(git rev-parse --show-toplevel)
source $root_dir/scripts/data/datasets_utils.sh 

dst_dir=$1
output_dir=$(create_folder "$dst_dir" "FDDB")

wget http://tamaraberg.com/faceDataset/originalPics.tar.gz -O $output_dir/originalPics.tar.gz
wget http://vis-www.cs.umass.edu/fddb/FDDB-folds.tgz -O $output_dir/FDDB-folds.tgz

cd $output_dir
tar xzfv originalPics.tar.gz
tar xzfv FDDB-folds.tgz
