import os
import sys

# Assumes
this_path = os.path.abspath(os.path.dirname(__file__))
# this_path = 'C:\\Users\\Burt\\Documents\\Git\\fishing_bot'
protoc_path = os.path.join(this_path, 'bin\\protoc.exe')
operating_dir = os.path.join(this_path, 'models\\research')
protos_abs = os.path.join(operating_dir, 'object_detection\\protos')
protos_rel = 'object_detection/protos/'
os.chdir(operating_dir)

# sys.path.append(operating_dir)
# sys.path.append("C:\\Users\\Burt\\Documents\\Git\\fishing_bot\\models\\object_detection\\utils")



for file in os.listdir(protos_abs):
    if file.endswith(".proto"):
        os.system(protoc_path+" "+protos_rel+file+" --python_out=.") #+" --proto_path="+protos_dir)
        # print(protoc_path+" "+protos_rel+file+" --python_out=.") #+protos_dir+" --proto_path="+protos_dir)
