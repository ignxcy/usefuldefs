import random
import os
import subprocess

# Do a system command
def cmd(command):
    os.system(command)
# Read a file
def read(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return f.read().strip()
    else:
        return "Usefuldefs: File {} does not exist.".format(file)
# Get the output of a system command
def cmdOutput(command):
    return subprocess.getoutput(command)
# Get the time of executing a system command
def cmdTime(command):
    return subprocess.getoutput(f"time {command}")
# Write to a file
def write(file, value):
    if os.path.exists(file):
        with open(file, "w") as f:
            f.write(value)
    else:
        print("Usefuldefs: File {} does not exist".format(file))
# Randomize two variables
def randomize(a, b):
    return random.choice(a, b)
# Generate a random number
def randomInt(a, b):
    return random.randint(a, b)
# Check if a string can be converted into an int 
def canBeInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
# Check if a string can be converted into a float 
def canBeFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
# Make a file 
def touch(file):
    os.mknod(file)
# Make a folder
def mkdir(folder):
   os.mkdir(folder)
# Check if a user that is running the program is a root (Unix only)
def rootCheck():
    if subprocess.getoutput("./rootcheck.sh") == "yes":
        return True
    else:
        return False
