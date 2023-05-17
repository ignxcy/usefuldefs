import random
import os

# Do a system command
def cmd(command):
    os.system(command)
def read(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return f.read().strip()
    else:
        print("Usefuldefs: File {} does not exists.".format(file))
