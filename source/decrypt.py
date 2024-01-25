import os

def decryptFile(src: str, dest: str, key: str, outFileName: str, overwrite: bool, createPath: bool):
    fullPath = os.path.join(dest, outFileName)
    if os.path.exists(fullPath):
        if not overwrite:
            print("Error: File exists and overwrite is not on.")
            return
    if not os.path.exists(os.path.dirname(dest)):
        if not createPath:
            print("Error: Directory does not exist and create path is not on.")
            return
        else:
            pathObj = Path(dest)
            pathObj.mkdir()
    cmd = "bounce -d -k \"" + key + "\" -i \"" + src + "\" -o \"" + fullPath + "\""
    print("Executing command: " + cmd)
    os.system(cmd)
