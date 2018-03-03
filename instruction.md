# S³FD: Single Shot Scale-invariant Face Detector

By [Shifeng Zhang](http://www.cbsr.ia.ac.cn/users/sfzhang/)

### Introduction

S³FD is a real-time face detector, which performs superiorly on various scales of faces with a single deep neural network, especially for small faces. For more details, please refer to our [arXiv paper](https://arxiv.org/abs/1708.05237).

### Documentation

1. [Download of datasets](#download dataset)
2. [Compilation of Caffe](#caffe compilation)
3. [Running evaluation benchmarks](#running evaluation benchmark)
4. [Results](#results)
5. [Issues Encountered](#issues)




While testing on pascal dataset some images in "sfd_test_code/PASCAL_face/pascal_img_list.txt" can't not be found.
I used PASCAL dataset from VOCtrainval_11-May-2012.tar (VOCdevkit/VOC2012/JPEGImages).
for example "2008_000216.jpg" image in pascal_img_list.txt is not in dataset.

Solution: Mix training-validation-testing data from pascal 2012 cahallenge
After mixing training/validation date from 
http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html 
with test data from 
http://host.robots.ox.ac.uk:8080/eval/challenges/voc2012/, 
now all the pascal images listed in "sfd_test_code/PASCAL_face/pascal_img_list.txt" are present. 
