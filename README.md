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

Download the tensorflow models git repo. Save this tensorflow models repo to your fishing_bot folder:
https://github.com/tensorflow/models/archive/v1.13.0.zip

Next, before tensorflow object detection API can be used with Python, protobuf files need to be generated from the tensorflow/models repo.
The protoc converter is found at:
https://github.com/protocolbuffers/protobuf/releases
This converter is also included in this repo.  To generate the necessary protos files, from the anaconda prompt run:
python use_protobuf.py

Next, to generate tfrecord data files from the training and test data-sets, run:
python generate_tfrecord.py --csv_input=images/data/train_labels.csv --image_dir=images/train --output_path=images/train.record
python generate_tfrecord.py --csv_input=images/data/test_labels.csv --image_dir=images/test --output_path=images/test.record

Finally, to train:
python model_main.py --logtostderr --train_dir=C:/Users/burtg/OneDrive/Documents/Git/fishing_bot/training --pipeline_config_path=C:/Users/burtg/OneDrive/Documents/Git/fishing_bot/training/faster_rcnn_inception_v2_pets.config

