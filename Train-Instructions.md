##Train Instructions:

- Setup of training machine on Amazon  <br />
-> Version of AMI (Deep Learning Base AMI (Ubuntu) Version 3.0 (ami-07c2a77e)  <br />
-> Version of Amazon Instance > p3.2xlarge  <br />

- SSD installation steps and notws can be found in the directory: docs/SSD-install.md

1. Follow the intruction of SSD to create the lmdb of WIDER FACE.  <br />

To start with wider face dataset, first we need to download it.  <br />
If you work on server, you will face problem to download the data from google drive directly to the server.  <br />
Therefore, in the "scripts" folder in this repo, we use the scripts "download-data.sh" and "google-drive.py" to solve this problem.  <br />
Just put these scripts in the directory: $HOME/data  <br />
then run the script like this: ./download-data.sh  <br />
the data will be downloaded and unziped.  <br />

TODO: prepare script to modify annotations as required for lmdb and put them in seperate files.  <br />
TODO: prepare script to put each image with the corresponding annotation file, and list all of them in text file.  <br />
TODO: modify the lmdb script in SSD to accept txt annotations files.  <br />

2. Modify the data augmentation code of SSD to make sure that it does not change the image ratio.
(Detail these steps here including which source files and what lines of code)  <br />

TODO: make sure to follow the data augmentation strategy in the paper.  <br />

3. Modify the anchor match code of SSD to implement the 'scale compensation anchor matching strategy'.
(Detail these steps here including which source files and what lines of code)  <br />

TODO: modify the 'MatchBBox' function in bbox_util.cpp by adding extra stage to implement the stage 2 of anchor matching strategy.  <br />
TODO: Make sure the implemaentation is as mentioned in the paper to avoid performance difference.  <br />
TODO: investigate more about "Max-out background label" mentioned in the paper!  <br />

4. Train the model.
(Provide train script including amount of training time and validation loss curves and anything else useful)  <br />

TODO: Prepare python script following SSD style that will include defining anchor box scales, stride, used VGG layers, augmentaion, and start training.  <br />
TODO: Check training details from the paper (learning rate, max iterations, etc)  <br />
TODO: Generate tarining loss and validation loss graphs after training.  <br />

 
