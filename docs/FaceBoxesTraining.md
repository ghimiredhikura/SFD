# FaceBoxes training with WIDER_FACE

First, download the files from this repo: 
https://github.com/OAID-ZhejiangUniversityARMClub/ZJU2017-face-faceless/tree/master/train-script/m10-final-8  <br />

Put these files with SSD code in the directory "model/Inception/FaceBoxes-m10" m10 here means that we use this version of FaceBoxes, we are not sure yet if it will work correctly, and we can need more modifications in the futuure.  <br />
Modify the file train.prototxt, next modifications are done:  <br />
-> source: "examples/WIDER_FACE/WIDER_FACE_train_lmdb"        <br />
-> label_map_file: "data/WIDER_FACE/labelmap_wider.prototxt"  <br />

Modify the file train.prototxt, next modifications are done:  <br />
-> source: "examples/WIDER_FACE/WIDER_FACE_val_lmdb"
-> label_map_file: "data/WIDER_FACE/labelmap_wider.prototxt"   <br />
-> output_directory: "~/data/Training_Out_wider/FaceBoxes-m10" <br />
-> name_size_file: "data/WIDER_FACE/val_name_size.txt"         <br />

Then run the script "start_training_m10.sh" to start training. <br />

# Notes
FaceBoxes use Inception as base network not VGG as SFD.  <br />
In this repo, they use umdfaces dataset for training "http://www.umdfaces.io/" but we used widerface.  <br />
Training parameters "in solver.prototxt" were all used exactly as they use it in this repo, except some modifications as follows:  <br />
-> The model will be evaluated with validation set each 5000 iterartions.  <br />
-> Snapshot of the model will be taken each 20000 iterations.  <br />
-> You need to prepare the datset first before doing previous modifications, All files should be generated during preperation of dataset as descriped in the file "Train-Instructions.md" and all scripts to prepare them exists in /scripts folder <br />
