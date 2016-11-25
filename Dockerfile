FROM kaixhin/cuda-caffe-deps:7.0
MAINTAINER Kai Arulkumaran <design@kaixhin.com>
RUN apt-get install -y git
# Move into Caffe repo

RUN cd /root/caffe && \
 git remote add yosinski https://github.com/yosinski/caffe.git && \
 git fetch --all && \
 git checkout --track -b deconv-deep-vis-toolbox yosinski/deconv-deep-vis-toolbox && \
# Make and move into build directory
  mkdir build && cd build && \
# CMake
  cmake .. && \
# Make
  make -j"$(nproc)" all && \
  make install
RUN apt-get install -y python-opencv
# Add to Python path
ENV PYTHONPATH=/root/caffe/python:$PYTHONPATH

COPY . /root/deep
WORKDIR /root/deep
