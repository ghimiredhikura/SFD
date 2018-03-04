To use SSD, first clone the SSD repo:
We will call the directory that you cloned Caffe into $CAFFE_ROOT

git clone https://github.com/weiliu89/caffe.git
cd caffe
git checkout ssd

For installation, you can follow the instructions in the SSD repo or use cmake with ccmake as it is easier to control and faster. 

First we need small change in Cmake file if you use cuda 9.0.
inside the folser "cmake" that exists in $CAFFE_ROOT, modify the file: "Cuda.cmake" as follows
remove this line: set(Caffe_known_gpu_archs "20 21(20) 30 35 50 52 61")
and put instead: set(Caffe_known_gpu_archs "30 35 50 52 61")

Then start installation with cmake as follows.
inside $CAFFE_ROOT write:

mkdir build
ccmake ..
then press "c" to configure and wait for a while
all dependancies and linking paths will appear, and you can change what you need. for us we change:
BLAS: Open
press "t" to see more options, and then change:
CUDA_ARCH_NAME:  All

then press "c" again, until this message appear in the instructions down: "Press [g] to generate and exit"
then press "g"

after that write "make -j8" and wait for the compilation to finish. 


