import os
import sys

# args = sys.argv
# dir = args[1]
# protoc_path = args[2]
this_path = os.path.abspath(os.path.dirname(__file__))
print(this_path)
operating_dir = 'C:/Users/Burt/Documents/Git/fishing_bot/models/research/'
protos_abs = 'C:/Users/Burt/Documents/Git/fishing_bot/models/research/object_detection/protos/'
protos_rel = 'object_detection/protos/'
protoc_path = 'C:/Users/Burt/Documents/Git/fishing_bot/bin/protoc.exe'
sys.path.append("C:\\Users\\Burt\\Documents\\Git\\fishing_bot\\models\\research\\")
sys.path.append("C:\\Users\\Burt\\Documents\\Git\\fishing_bot\\models\\object_detection\\utils")
os.chdir(operating_dir)


for file in os.listdir(protos_abs):
    if file.endswith(".proto"):
        os.system(protoc_path+" "+protos_rel+file+" --python_out=.") #+" --proto_path="+protos_dir)
        print(protoc_path+" "+protos_rel+file+" --python_out=.") #+protos_dir+" --proto_path="+protos_dir)
