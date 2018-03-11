cd ../../..

./build/tools/caffe train \
--solver=models/Inception/FaceBoxes/solver.prototxt \
--gpu=0 2>&1 | tee models/Inception/FaceBoxes/logs/train_faceboxes_widerface.logs
