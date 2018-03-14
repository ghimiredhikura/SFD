from sfd_detector import SFD_NET
import argparse
import cv2
import os.path
import progressbar
import sys
sys.path.insert(0, '../../python')
import caffe


def process_imgs_list(imgs_list_file, output_file, dataset_path, origin, device=0):
    net = SFD_NET(device=device)
    with open(imgs_list_file, 'r') as img_names:
        names = img_names.readlines()

    bar = progressbar.ProgressBar(max_value=len(names))
    with open(output_file, 'w') as f:
        for i, Name in enumerate(names):
            Image_Path = os.path.join(dataset_path, Name[:-1].replace('.jpg', '') + '.jpg')
            image = caffe.io.load_image(Image_Path)
            height = image.shape[0]
            width = image.shape[1]
        
            if origin in ['AFW', 'PASCAL']:
                im_shrink = 640.0 / max(height, width)
                image = cv2.resize(image, None, None, fx=im_shrink, fy=im_shrink, interpolation=cv2.INTER_LINEAR)
        
            detections = net.detect([image])
            processed_detections = net.process_detections(detections[0], width, height)
        

            # Specific format for FDDB dataset
            if origin == 'FDDB':
                f.write('{:s}\n'.format(Name[:-1]))
                f.write('{:d}\n'.format(len(processed_detections)))

            for det in processed_detections:
                score, xmin, ymin, xmax, ymax = det
                if origin in ['AFW', 'PASCAL']:
                    # Simple fitting to AFW/PASCAL, because the gt box of training
                    # data (i.e., WIDER FACE) is longer than the gt box of AFW/PASCAL
                    ymin += 0.2 * (ymax - ymin + 1)   

                if origin == 'FDDB':
                    # For FDDB, save rectangle in FDDB format as stated in
                    # https://github.com/zimenglan-sysu-512/fddb-eval-code
                    f.write('{:.6f} {:.6f} {:.6f} {:.6f} {:.2f}\n'.
                            format(xmin, ymin, (xmax-xmin+1), (ymax-ymin+1), score))
                else:
                    f.write('{:s} {:.3f} {:.1f} {:.1f} {:.1f} {:.1f}\n'.
                            format(Name[:-1], score, xmin, ymin, xmax, ymax))

            bar.update(i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test code for a SFD trained model.')
    parser.add_argument('-d', '--dataset', type=str, choices=['AFW', 'PASCAL', 'FDDB'],
        help='Dataset name to test. Options: AFW, PASCAL, FDDB', required=True)
    parser.add_argument('-p', '--path', type=str, help='Dataset path', required=True)
    parser.add_argument('--device', type=int, default=0, help="GPU device to use, default is 0")
    args = parser.parse_args()

    dataset_name = args.dataset
    dataset_path = args.path
    device = args.device

    imgs_list = '{}/{}_img_list.txt'.format(dataset_name, dataset_name.lower())
    dets_file = '{}/sfd_{}_dets.txt'.format(dataset_name, dataset_name.lower())
    process_imgs_list(imgs_list, dets_file, dataset_path, dataset_name, device)
