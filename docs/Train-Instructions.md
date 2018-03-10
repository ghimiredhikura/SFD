# Train Instructions:

- Setup of training machine on Amazon  <br />
-> Version of AMI (Deep Learning Base AMI (Ubuntu) Version 3.0 (ami-07c2a77e)  <br />
-> Version of Amazon Instance > p3.2xlarge  <br />

- SSD installation steps and notws can be found in the directory: docs/SSD-install.md, Make sure to include $CAFFE_ROOT/python to your PYTHONPATH

1. Follow the intruction of SSD to create the lmdb of WIDER FACE. [DONE]  <br />

-> To start with wider face dataset, first we need to download it. If you work on server, you will face problem to download the data from google drive directly to the server. Therefore, in the "scripts" folder in this repo, we use the scripts "download-data.sh" and "google-drive.py" to solve this problem. Just put these scripts in the directory: $HOME/data, then run the script like this: ./download-data.sh. the data will be downloaded and unziped.  <br />

-> Useful link: https://github.com/weiliu89/caffe/wiki/Train-SSD-on-custom-dataset <br />
- To prepare the data and genearte lmdb database, next steps are done: <br />
 1- prepared script to modify annotations as required for lmdb and put them in seperate files: The annotations should be in the format: "label_id xmin ymin xmax ymax" and exist inside text files with the same names as their corresponding images, these files contain all bounding boxes in the annotations related to this image. This script exists in the scripts/ folder with the name "generate-train-annotations.py". We need to run this script twice, one for training and one for validation set, in each time just uncomment the corresponding lines in the script.  <br />

 2- prepared script to put each image with the corresponding annotation file, and list all of them in one text file. This script take the directories of the files generated from previous step, and the directory of the images, then it generate the list. The script exists in the scripts folder under the name "generate-lists.py". We need to run it twice as previous step, in each time uncomment the necessary lines. The output of this step should be in $SSD_ROOT/data/WIDER_FACE, which contans "train.txt", "val.txt", and "val_name_size.txt"  <br />

 3- modified the lmdb script "$SSD_ROOT/data/WIDER_FACE/create_data.sh" in SSD to make it accept txt annotations files not json or xml files. Then run this script which generated the lmdb database susccessfully in $HOME/data/WIDER_FACE  <br />

 4- prepared the file "labelmap_wider.prototxt" which contains the labels of the training and testing, 0 is background and 1 is face.  <br />

2. Modify the data augmentation code of SSD to make sure that it does not change the image ratio.
(Detail these steps here including which source files and what lines of code)  [DONE] <br />
-> [DONE] The augmentation strategy in the paper of SFD is followed, and the image ration is not changing. The details of this part is implemented in the python script for training.  <br />

3. Modify the anchor match code of SSD to implement the 'scale compensation anchor matching strategy'.
(Detail these steps here including which source files and what lines of code)  [TODO] <br />

-> TODO: modify the 'MatchBBox' function in bbox_util.cpp by adding extra stage to implement the stage 2 of anchor matching strategy.  <br />
-> TODO: investigate more about "Max-out background label" mentioned in the paper!  <br />

4. Train the model.
(Provide train script including amount of training time and validation loss curves and anything else useful) [DONE] <br />

-> [DONE] Prepare python script following SSD style that will include defining anchor box scales, stride, used VGG layers, augmentaion, then start training.  <br />
-> [DONE] Check training details from the paper (learning rate, max iterations, etc)  <br />
-> TODO: Generate tarining loss and validation loss graphs after training is finished.  <br />
