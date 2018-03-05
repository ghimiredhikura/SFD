#!/bin/bash


export LD_LIBRARY_PATH=/usr/local/cuda-8.0-cudnn6.0/lib64/:$LD_LIBRARY_PATH
echo $LD_LIBRARY_PATH


export LD_LIBRARY_PATH=/home/xyz/code1/caffe-ssd/distribute/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/xyz/code1/caffe-ssd/distribute/python:$PYTHONPATH
echo "PYTHONPATH:"$PYTHONPATH


NPATH=${PATH/\/home\/xyz\/anaconda3\/bin:/}
echo $PATH
echo -----------
echo $NPATH
export PATH=$NPATH


python r.py
