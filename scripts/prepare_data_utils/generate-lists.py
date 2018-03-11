# This script generate a list with image relative path and corresponding relative path of annotation text file.
# This format is needed to generate the lmdb database to train SSD

import numpy as np
import os
import math
import argparse
import glob
import scandir
from scandir import scandir # python 2.7
from PIL import Image

#AnnotPath = "/home/ubuntu/data/WIDER_train_annotations_ssd"
#ImagesPath = "/home/ubuntu/data/WIDER_train/images"
#OutputTxtFile = "/home/ubuntu/SSD/data/WIDER_FACE/train.txt"
# list generated need to be relative path with respect to general directory
#images_path = ImagesPath[ImagesPath.find("WIDER_train") : ]   # split the path from this directory
#annot_path = AnnotPath[AnnotPath.find("WIDER_train_annotations_ssd") : ] # split the path from this directory


# Validation path
ValFlag = True 
AnnotPath = "/home/ubuntu/data/WIDER_val_annotations_ssd" 
ImagesPath = "/home/ubuntu/data/WIDER_val/images"
# list generated need to be relative path with respect to general directory
images_path = ImagesPath[ImagesPath.find("WIDER_val") : ]   # split the path from this directory
annot_path = AnnotPath[AnnotPath.find("WIDER_val_annotations_ssd") : ] # split the path from this directory
OutputTxtFile = "/home/ubuntu/SSD/data/WIDER_FACE/val.txt"

f = open(OutputTxtFile, "w")
if ValFlag:
	fts = open("/home/ubuntu/SSD/data/WIDER_FACE/val_name_size.txt", "w")

for DirName in os.listdir(AnnotPath):
	print(DirName)
	annotations_path = os.path.join(AnnotPath, DirName)
	#if os.path.isdir(annotations_path):
	annotations_path = os.path.abspath(annotations_path)
	print(annotations_path)
	#images_path =  os.path.join(ImagesPath, DirName)
	for files in scandir(annotations_path):
		if files.is_file() and (files.name.endswith('.txt')):
			annot_relative_path = os.path.join(annot_path, DirName + "/" +files.name)
			images_relative_path = os.path.join(images_path , DirName + "/" +os.path.splitext(files.name)[0] + ".jpg" )
			
			f.write(str(images_relative_path) + " " + str(annot_relative_path) + "\n" )
			
			if ValFlag:
				im = Image.open(os.path.join(ImagesPath, DirName + "/" +os.path.splitext(files.name)[0] + ".jpg" ) )
				width, height = im.size
				fts.write(os.path.splitext(files.name)[0] + " " + str(height) + " " + str(width) + "\n")
f.close()


