import os

# Uses the existing Git repo protoc.exe in the cloned \bin directory
# Assumes tensorflow models have been cloned into this repo, in a \models directory
# tensorflow models = https://github.com/tensorflow/models

this_path = os.path.abspath(os.path.dirname(__file__))
protoc_path = os.path.join(this_path, 'bin\\protoc.exe')
operating_dir = os.path.join(this_path, 'models\\research')
protos_abs = os.path.join(operating_dir, 'object_detection\\protos')
protos_rel = 'object_detection/protos/'
os.chdir(operating_dir)

for file in os.listdir(protos_abs):
    if file.endswith(".proto"):
        os.system(protoc_path+" "+protos_rel+file+" --python_out=.")
        # print(protoc_path+" "+protos_rel+file+" --python_out=.") #+protos_dir+" --proto_path="+protos_dir)
