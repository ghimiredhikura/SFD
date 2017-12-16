

import numpy as np
import cv2


import os
import sys
sys.path.insert(0, 'python')
import caffe


caffe.set_device(0)
caffe.set_mode_gpu()
model_def = './model/deploy.prototxt'
model_weights = './model/SFD.caffemodel'
net = caffe.Net(model_def, model_weights, caffe.TEST)

def Do():
    Image_Path = '/home/xyz/test/vvvL.jpg'
    image = caffe.io.load_image(Image_Path)
    heigh = image.shape[0]
    width = image.shape[1]

    net.blobs['data'].reshape(1, 3, image.shape[0], image.shape[1])
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2, 0, 1))
    transformer.set_mean('data', np.array([104, 117, 123]))
    transformer.set_raw_scale('data', 255)
    transformer.set_channel_swap('data', (2, 1, 0))
    transformed_image = transformer.preprocess('data', image)
    net.blobs['data'].data[...] = transformed_image

    detections = net.forward()['detection_out']
    det_conf = detections[0, 0, :, 2]
    det_xmin = detections[0, 0, :, 3]
    det_ymin = detections[0, 0, :, 4]
    det_xmax = detections[0, 0, :, 5]
    det_ymax = detections[0, 0, :, 6]

    keep_index = np.where(det_conf >= 0)[0]
    det_conf = det_conf[keep_index]
    det_xmin = det_xmin[keep_index]
    det_ymin = det_ymin[keep_index]
    det_xmax = det_xmax[keep_index]
    det_ymax = det_ymax[keep_index]


    frame = cv2.imread(Image_Path)
    for i in xrange(det_conf.shape[0]):
        xmin = det_xmin[i] * width
        ymin = det_ymin[i] * heigh
        xmax = det_xmax[i] * width
        ymax = det_ymax[i] * heigh
        score = det_conf[i]
        pt1 = int(xmin),int(ymin)
        pt2 = int(xmax),int(ymax)
        clr = (0, 0, 255)
        cv2.rectangle(frame, pt1, pt2, clr, 1)

    cv2.imwrite("frame.jpg", frame)
    #cv2.waitKey()



Do()












