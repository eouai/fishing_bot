import os
import sys

args = sys.argv
directory = args[1]
protoc_path = args[2]
# dir = 'C:/Users/Burt/Documents/Git/fishing_bot/tensorflow/models/research/object_detection/protos/'
# protoc_path = 'C:/Users/Burt/Documents/Git/fishing_bot/bin/protoc.exe'

for file in os.listdir(directory):
    if file.endswith(".proto"):
        os.system(protoc_path+" "+directory+file+" --python_out=.")  # --proto_path="+directory)
