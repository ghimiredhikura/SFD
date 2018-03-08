#!/usr/bin/env bash

root_dir=$(git rev-parse --show-toplevel)
source $root_dir/scripts/data/datasets_utils.sh 

dst_dir=$1
output_dir=$(create_folder "$dst_dir" "WIDER")
drive=$root_dir/scripts/data/google-drive.py

python $drive 0B6eKvaijfFUDQUUwd21EckhUbWs $output_dir/Training.zip
python $drive 0B6eKvaijfFUDbW4tdGpaYjgzZkU $output_dir/Test.zip
python $drive 0B6eKvaijfFUDd3dIRmpvSk8tLUk $output_dir/Validation.zip
wget http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/support/bbx_annotation/wider_face_split.zip -O $output_dir/wider_face_split.zip 

cd $output_dir
for file in "Training" "Test" "Validation" "wider_face_split"
do
    unzip $file.zip -d .
done
