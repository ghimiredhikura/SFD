# S³FD: Single Shot Scale-invariant Face Detector

By [Shifeng Zhang](http://www.cbsr.ia.ac.cn/users/sfzhang/)

### Introduction

S³FD is a real-time face detector, which performs superiorly on various scales of faces with a single deep neural network, especially for small faces. For more details, please refer to our [arXiv paper](https://arxiv.org/abs/1708.05237).

### Documentation

1. [Preparation](#preparation)
2. [Download of datasets](#download)
3. [Compile and Run SFD detector](#compilation)
4. [Running evaluation benchmarks](#runningevaluationbenchmark)
5. [Results](#results)
6. [Issues encountered](#issues)

### Preparation

1. Get the [SSD](https://github.com/weiliu89/caffe/tree/ssd) code. We will call the directory that you cloned Caffe into `$CAFFE`
  ```Shell
  git clone https://github.com/weiliu89/caffe.git
  cd $CAFFE
  git checkout ssd
  ```
2. Build the code. Please follow [Caffe instruction](http://caffe.berkeleyvision.org/installation.html) to install all necessary packages and build it.
  ```Shell
  # Modify Makefile.config according to your Caffe installation.
  cp Makefile.config.example Makefile.config
  # use nproc to check how many cores you can use, in our case we used 8 cores
  make -j8 
  # Make sure python is installed correctly and environment path is set.
  make py
  make test -j8
  # (Optional)
  make runtest -j8
  ```
3. Download our [pre-trained model](https://drive.google.com/open?id=1CboBIsjcDQ-FC1rMES6IjTl6sYQDoD6u) and merge it with the folder `$CAFFE/models` in `$CAFFE/models/sfd_models/VGGNet/WIDER_FACE/SFD_trained`.

4. Get this git [SFD](https://github.com/bonseyes/SFD). We will call the directory that you cloned SFD into `$CAFFE/SFD`. Make sure that above sfd_test_code is in the folder `$CAFFE/SFD/sfd_test_code`

### Download of datasets

1. Download [AFW](http://www.ics.uci.edu/~xzhu/face/) dataset. We will call this directory `$CAFFE/SFD/AFW`.
2. Download [FDDB](http://vis-www.cs.umass.edu/fddb/index.html) dataset. We will call this directory `$CAFFE/SFD/FDDB`.
3. Download [PASCAL face (train/validataion)](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html) dataset and [PASCAL face (test)](http://host.robots.ox.ac.uk:8080/eval/challenges/voc2012/) dataset. Merge them into single directory. We call this directory `$CAFFE/SFD/PASCAL_FACE`.
4. Download [WIDER FACE](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/) datasets. We will call this directory `$CAFFE/SFD/WIDER_FACE`.

### Compile and Run SFD detector

1. Compile and Run SFD detector on AFW dataset.
  ```Shell
  cd $CAFFE/SFD/sfd_test_code/AFW
  # You must modify the "Path" in the afw_test.py to your AFW path if it is different then in this tutorial. 
  # It will creat sfd_afw_dets.txt.
  python afw_test.py
  ```
2. Compipe and Run SFD detector on PASCAL dataset.
  ```Shell
  cd $CAFFE/SFD/sfd_test_code/PASCAL_FACE
  # You must modify the "Path" in the pascal_test.py to your PASCAL_face path if it is different then in this tutorial. 
  # It will creat sfd_pascal_dets.txt.
  python pascal_test.py
  ```
3. Compile and Run SFD detector on FDDB dataset.
  ```Shell
  cd $SFD_ROOT/sfd_test_code/FDDB
  # You must modify the "Path" in the fddb_test.py to your FDDB path if it is different then in this tutorial.
  # It will creat sfd_fddb_dets.txt.
  python fddb_test.py
  # Fitting the dets from rectangle box to ellipse box.
  # It will creat sfd_fddb_dets_fit.txt and put it in the FDDB evalution code to evalute.
  cd fddb_from_rectangle_to_ellipse
  matlab -nodesktop -nosplash -nojvm -r "run fitting.m;quit;"
  # If you want to get the results of FDDB in our paper, you should use our 'FDDB_annotation_ellipseList_new.txt'
  ```

4. Compile and Run SFD detector on WIDER FACE dataset.
  ```Shell
  cd $SFD_ROOT/sfd_test_code/WIDER_FACE
  # You must modify the path in the wider_test.py to your WIDERFACE path. 
  # It will creat detection results in the "eval_tools_old-version" folder.
  python wider_test.py
  # If you want to get the results of val set in our paper, you should use the provided "eval_tools_old-version". 
  # Or you can use latest eval_tools of WIDER FACE.
  # There is a slight difference between them, since the annotation used for the evaluation is slightly change around March 2017.
  ```
### Running evaluation benchmarks

Download the [EVALUATION TOOLBOX](https://bitbucket.org/marcopede/face-eval) for evaluation. We call this directory `$CAFFE/SFD/face-eval`.

1. Evaluate our model on AFW dataset.
```Shell
# Put sfd_afw_dets.txt from `$CAFFE/SFD/sfd_test_code/AFW` to `$CAFFE/SFD/face-eval/detections/AFW`.
cd $CAFFE/SFD/face-eval
python plot_AP.py --dataset AFW
# The final evaulation ROC graph will be stored in `$CAFFE/SFD/face-eval/`.
```
2. Evaluate our model on PASCAL face dataset
```Shell
# Put sfd_pascal_dets.txt from `$CAFFE/SFD/sfd_test_code/PASCAL_face` to `$CAFFE/SFD/face-eval/detections/PASCAL`
cd $CAFFE/SFD/face-eval
python plot_AP.py 
# The final evaluation ROC graph will be stored in `$CAFFE/SFD/face-eval/.
```

### Results
1. AFW 
![Alt text](https://github.com/ghimiredhikura/SFD/blob/master/sfd_test_code/AFW/AFW_eval.png)
2. PASCAL face
![Alt text](https://github.com/ghimiredhikura/SFD/blob/master/sfd_test_code/PASCAL_face/PASCAL_eval.png)

#### Reference (results from original paper)

![Alt text](https://github.com/ghimiredhikura/SFD/blob/master/sfd_test_code/AFW-PASCAL.JPG)
![Alt text](https://github.com/ghimiredhikura/SFD/blob/master/sfd_test_code/FDDB.JPG)
![Alt text](https://github.com/ghimiredhikura/SFD/blob/master/sfd_test_code/WIDER.JPG)
![Alt text](https://github.com/ghimiredhikura/SFD/blob/master/sfd_test_code/Eval%20Table.JPG)

### Issues encountered

1. Problem: While testing on pascal dataset, some images listed in "sfd_test_code/PASCAL_face/pascal_img_list.txt" are not found.
I used PASCAL dataset from VOCtrainval_11-May-2012.tar (VOCdevkit/VOC2012/JPEGImages).
for example "2008_000216.jpg" image in pascal_img_list.txt is not in dataset. <br />
Solution: Mix training-validation dataset with test dataset from pascal 2012 cahallenge. After mixing [training/validation data](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html) with [test data](http://host.robots.ox.ac.uk:8080/eval/challenges/voc2012/), all the pascal images listed in "sfd_test_code/PASCAL_face/pascal_img_list.txt" are available in merged folder. 

2. Problem: After the AFW/PASCAL dataset evaluation of our detector and other detector present in EVALUATION TOOLBOX, the result of SFD detector is not as expected. Seems something wrong as ROC curve of our detector is very poor. <br />
Solution: Fixed. The detection result in AFW dataset is now exactly same as in the original paper. It was because of wrong linkag e of deploy.prototxt! <br />
The detection result in PASCAL_face is 97.60% where as in original paper it is 98.49%. Checking this if something wrong in testing.

I. AFW 
![Alt text](https://github.com/ghimiredhikura/SFD/blob/master/sfd_test_code/AFW/AFW_eval.png)
II. PASCAL
![Alt text](https://github.com/ghimiredhikura/SFD/blob/master/sfd_test_code/PASCAL_face/PASCAL_eval.png)
