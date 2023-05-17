import random
import os

# Do a system command
def cmd(command):
    os.system(command)
# Read a file
def read(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return f.read().strip()
    else:
        return "Usefuldefs: File {} does not exists.".format(file)
# Write to a file
def write(file, value):
    if os.path.exists(file):
        with open(file, "w") as f:
            f.write(value)
    else:
        print("Usefuldefs: File {} does not exist".format(file))
