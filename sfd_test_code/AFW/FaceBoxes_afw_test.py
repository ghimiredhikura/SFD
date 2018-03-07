import numpy as np
import cv2


# Make sure that caffe is on the python path:
caffe_root = '../../../'  # this file is expected to be in {sfd_root}/sfd_test_code/AFW
import os
os.chdir(caffe_root)
import sys
sys.path.insert(0, 'python')
import caffe


caffe.set_device(0)
caffe.set_mode_gpu()
model_def = '/home/deep/Desktop/Projects/caffe/FaceBoxes/faceboxes_deploy.prototxt'
model_weights = '/home/deep/Desktop/Projects/caffe/FaceBoxes/FaceBoxes_1024x1024.caffemodel'
net = caffe.Net(model_def, model_weights, caffe.TEST)

def preprocess(src):
    img = cv2.resize(src, (1024,1024))
    img = img - 127.5
    img = img * 0.007843
    return img

def postprocess(img, out):   
    h = img.shape[0]
    w = img.shape[1]
    box = out['detection_out'][0,0,:,3:7] * np.array([w, h, w, h])

    cls = out['detection_out'][0,0,:,1]
    conf = out['detection_out'][0,0,:,2]
    return (box.astype(np.int32), conf, cls)

count = 0
Path = './FaceBoxes/AFW/'
f = open('./FaceBoxes/sfd_test_code/AFW/sfd_afw_dets.txt', 'wt')
for Name in open('./FaceBoxes/sfd_test_code/AFW/afw_img_list.txt'):
    Image_Path = Path + Name[:-1] + '.jpg'
    frame = caffe.io.load_image(Image_Path)
    heigh = frame.shape[0]
    width = frame.shape[1]

    #im_shrink = 640.0 / max(image.shape[0], image.shape[1])
    #image = cv2.resize(image, None, None, fx=im_shrink, fy=im_shrink, interpolation=cv2.INTER_LINEAR)

    res1 = cv2.resize(frame, (1024, 1024), 0.0, 0.0, interpolation=cv2.INTER_CUBIC)

    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2, 0, 1))
    transformer.set_mean('data', np.array([104, 117, 123]))  # mean pixel

    transformed_image = transformer.preprocess('data', frame)
      # print img
    net.blobs['data'].data[...] = transformed_image

    detections = net.forward()['detection_out']
    det_conf = detections[0, 0, :, 2]
    det_xmin = detections[0, 0, :, 3]
    det_ymin = detections[0, 0, :, 4]
    det_xmax = detections[0, 0, :, 5]
    det_ymax = detections[0, 0, :, 6]

    res = cv2.imread(Image_Path)

    for i in xrange(det_conf.shape[0]):
        xmin = int(round(det_xmin[i] * width))
        ymin = int(round(det_ymin[i] * heigh))
        xmax = int(round(det_xmax[i] * width))
        ymax = int(round(det_ymax[i] * heigh))
        
        p1 = (xmin, ymin)
        p2 = (xmax, ymax)    

        # simple fitting to AFW, because the gt box of training data (i.e., WIDER FACE) is longer than the gt box of AFW
        ymin += 0.2 * (ymax - ymin + 1)   
        score = det_conf[i]
        if score < 0:
            continue
        f.write('{:s} {:.3f} {:.1f} {:.1f} {:.1f} {:.1f}\n'.
                format(Name[:-1], score, xmin, ymin, xmax, ymax))
        
        cv2.rectangle(res, p1, p2, (0,255,0))
        
    cv2.imshow("FaceBoxes", res);

    cv2.imwrite("frame.jpg", res)

    cv2.waitKey(100)

    count += 1
    print('%d/205' % count)
