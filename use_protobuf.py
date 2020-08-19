import os
import sys

current_path = os.getcwd()
# sys.path.append(current_path)
# sys.path.append(current_path + "\\tensorflow\\models\\research\\")
# sys.path.append(current_path + "\\tensorflow\\models\\research\\object_detection\\utils")
os.chdir(current_path + '/tensorflow/models/research/')
print(os.getcwd())

# args = sys.argv
# directory = args[1]
# protoc_path = args[2]
directory = 'object_detection/protos/'
protoc_path = current_path + '/bin/protoc'

for file in os.listdir(directory):
    if file.endswith(".proto"):
        os.system(protoc_path+" "+directory+file+" --python_out=.")  # --proto_path="+directory)

print('protos files successfully generated')
