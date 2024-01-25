import os
from pathlib import Path


def genKey(path: str, fileName: str, overwrite: bool, createDir: bool):
    fullPath = os.path.join(path, fileName)
    if os.path.exists(fullPath):
        if not overwrite:
            print("Error: File exists and overwrite is not on.")
            return
    if not os.path.exists(path):
        if not createDir:
            print("Error: Directory does not exist and create path is not on.")
            return
        else:
            pathObj = Path(path)
            pathObj.mkdir()
    cmd = "bounce -g -o \"" + fullPath + "\""
    print("Executing: "+cmd)
    os.system(cmd)
