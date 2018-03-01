Documentation

- Download of datasets
- Compilation of Caffe
- Running evaluation benchmarks
- Results
- Issues Encountered

PSCAL DATASET:
DOWNLOAD PASCAL 2012 dataset (VOCtrainval_11-May-2012.tar (VOCdevkit/VOC2012/JPEGImages)). 
Test image lists are in "sfd_test_code/PASCAL_face/pascal_img_list.txt". 
But all test images in "pascal_img_list.txt" are not present in "VOCtrainval_11-May-2012.tar". For example "2008_000216.jpg".

Correction: Mix training-validation-testing data from pascal 2012 cahallenge in a single DIR "PASCAL_DATASET".
After mixing training/validation date from http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html with test data from http://host.robots.ox.ac.uk:8080/eval/challenges/voc2012/, all the pascal images listed in "sfd_test_code/PASCAL_face/pascal_img_list.txt" are present in combined DIR "PASCAL_DATASET".
