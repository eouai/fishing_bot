# fishing_bot

# Installation Instructions

Requires Microsoft Visual C++ 14.0+ build tools
https://visualstudio.microsoft.com/visual-cpp-build-tools/

clone or download this repo

These instructions are structured for operating in a Windows env.  Open an Anaconda prompt (run as administrator) and browse to the location of the cloned / downloaded repo.

create the virtual env by running the following command in the anaconda prompt:

```
conda env create -f environment.yml
```

Once the env is created, activate it:
```
conda activate fishing_bot
```

Next, clone the tensorflow models into this repo:
```
git clone --depth 1 https://github.com/tensorflow/models
```

If preferred, you can manually download the zip and save it into a "models" directory into this repo. These models are located at:
https://github.com/tensorflow/models

Next, before tensorflow object detection API can be used with Python, protobuf files need to be generated from the tensorflow models protos files. Run the script use_protofbuy.py in your Anaconda prompt:

```
python use_protofbuf.py
```

The protoc converter used is included in this repo but was sourced from:
https://github.com/protocolbuffers/protobuf/releases

Finally, we need to pip install the Object Detection API.  Run the following:
```
cd models/research/
pip install .
```

Next, to generate tfrecord data files from the training and test data-sets, run:
python generate_tfrecord.py --csv_input=images/data/train_labels.csv --image_dir=images/train --output_path=images/train.record
python generate_tfrecord.py --csv_input=images/data/test_labels.csv --image_dir=images/test --output_path=images/test.record

Finally, to train:
python model_main.py --logtostderr --train_dir=C:/Users/burtg/OneDrive/Documents/Git/fishing_bot/training --pipeline_config_path=C:/Users/burtg/OneDrive/Documents/Git/fishing_bot/training/faster_rcnn_inception_v2_pets.config

