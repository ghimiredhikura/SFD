# -*- coding: utf-8 -*
import numpy as np  
import sys,os  
import cv2
caffe_root = '../../../'
sys.path.insert(0, caffe_root + 'python')  
import caffe  
import time;  

count = 0

net_file= '../../faceboxes_deploy.prototxt'  
caffe_model='../../FaceBoxes_1024x1024.caffemodel'  
test_dir = "../../AFW/"

if not os.path.exists(caffe_model):
    print("FaceBoxes_deploy.caffemodel does not exist,")
    print("use merge_bn.py to generate it.")
    exit()
caffe.set_mode_gpu()
net = caffe.Net(net_file,caffe_model,caffe.TEST)  

CLASSES = ('background',
           'face')

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))
transformer.set_mean('data', np.array([104, 117, 123]))  # mean pixel
#transformer.set_raw_scale('data', 255)
#transformer.set_channel_swap('data', (2, 1, 0))

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

def detect(imgfile):

    #print imgfile

    frame = cv2.imread(imgfile)
    
    #videoCapture = cv2.VideoCapture(0)
    #videoCapture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640)  
  
    #videoCapture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480)  

    #success, frame = videoCapture.read()
    #while success :
      #success, frame = videoCapture.read()
    
    res = cv2.resize(frame, (1024, 1024), 0.0, 0.0, interpolation=cv2.INTER_CUBIC)
    #frame = preprocess(frame)
    transformed_image = transformer.preprocess('data', frame)
    # print img
    net.blobs['data'].data[...] = transformed_image

    time_start=time.time()
    out = net.forward()  
    time_end=time.time()
    print time_end-time_start,  
    print "s"
    
    box, conf, cls = postprocess(frame, out)

    for i in range(len(box)):
      p1 = (box[i][0], box[i][1])
      p2 = (box[i][2], box[i][3])

      xmin = p1[0]
      ymin = p1[1]
      xmax = p2[0]
      ymax = p2[1]

      # simple fitting to AFW, because the gt box of training data (i.e., WIDER FACE) is longer than the gt box of AFW
      ymin += 0.2 * (ymax - ymin + 1)   
      score = conf[i]
      if score < 0:
        continue
      f.write('{:s} {:.3f} {:.1f} {:.1f} {:.1f} {:.1f}\n'.
              format(Name[:-1], score, xmin, ymin, xmax, ymax))

      cv2.rectangle(frame, p1, p2, (0,255,0))
      p3 = (max(p1[0], 15), max(p1[1], 15))
      title = "%s:%.2f" % (CLASSES[int(cls[i])], conf[i])
      cv2.putText(frame, title, p3, cv2.FONT_ITALIC, 0.6, (0, 255, 0), 1)
    
    cv2.imshow("SSD", frame)
    cv2.waitKey(1)
    #if cv2.waitKey(100) & 0xFF == ord('q'):
    #  break
    #Exit if ESC pressed
    #if k == 27 : return False

    return True

f = open('sfd_afw_dets.txt', 'wt')
for Name in open('afw_img_list.txt'):
  Image_Path = test_dir + Name[:-1] + '.jpg'
  detect(Image_Path)

  count += 1
  print('%d/205' % count) 

#  detect("18489332.jpg")