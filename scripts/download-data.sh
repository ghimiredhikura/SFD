# this script download all training, validation, and test data for WIDER FACE, then unzip them. 

echo 'downloading training set'
python google-drive.py 0B6eKvaijfFUDQUUwd21EckhUbWs ./Training.zip
unzip Training.zip -d .

echo 'downloading testing set'
python google-drive.py 0B6eKvaijfFUDbW4tdGpaYjgzZkU ./Test.zip
unzip Test.zip -d .

echo 'downloading validation set'
python google-drive.py 0B6eKvaijfFUDd3dIRmpvSk8tLUk ./Validation.zip
unzip Validation.zip -d .

echo 'downloading annotations'
wget http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/support/bbx_annotation/wider_face_split.zip
wget http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/support/example/Submission_example.zip

unzip wider_face_split.zip -d .
 
