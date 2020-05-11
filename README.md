# fishing_bot

# Installation Instructions

Requires Microsoft Visual C++ 14.0+ build tools
https://visualstudio.microsoft.com/visual-cpp-build-tools/

clone or download this repo

open an anaconda prompt and browse to the location of the cloned / downloaded repo

create the virtual env by running the following command in the anaconda prompt:
conda env create -f tensorflow.yml

Once the env is created, activate it:
conda activate fishing_bot

Install pycocotools:
pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"

Download the tensorflow models git repo:
https://github.com/tensorflow/models

Next, before tensorflow object detection API can be used with Python, protobuf files need to be generated from the tensorflow/models repo.
The protoc converter is found at:
https://github.com/protocolbuffers/protobuf/releases
This converter is also included in this repo.  To generate the necessary protos files, from the anaconda prompt run:
python use_protobuf.py

save this tensorflow models repo to your fishing_bot folder



