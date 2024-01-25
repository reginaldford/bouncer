import PySimpleGUI as g
import os
from encrypt import encryptFile
from decrypt import decryptFile
from genKey import genKey

g.theme("DarkBlack 1")
g.set_options(font=('San Serif', 14))

defaultKeyDir = os.path.expanduser("~/.config/bouncer/")
defaultKeyName = "k"
pathJoin = os.path.join
defaultKeyPath = pathJoin(defaultKeyDir, defaultKeyName)

genkey_tab_layout = [
    [g.Text("Use this tab to generate a new key.")],
    [g.Text("Key Destination:"), g.Input(defaultKeyDir, key="GENPATH", size=20), g.FolderBrowse("Browse",
                                                                                                initial_folder=defaultKeyDir)],
    [g.Text("Key File name:"), g.Input(
        defaultKeyName, key="GENFILE", size=20)],
    [g.Checkbox("Overwrite Existing File", default=False, key="GENOVERWRITE"),
     g.Checkbox("Create Path if Necessary", default=False, key="GENCREATEPATH")],
    [g.Button("Generate Key", key="GENKEY")]
]

encrypt_tab_layout = [
    [g.Text("Key:"), g.Input(defaultKeyPath, size=20, key="ENCKEY"), g.FileBrowse("Select Key",
                                                                                  initial_folder=defaultKeyDir)],
    [g.Text("Use this tab to Encrypt a file.")],
    [g.Text("Source:"), g.Input(os.path.expanduser("~"), key="ENCSRC", size=20), g.FileBrowse("Select File",
                                                                                              initial_folder=os.path.expanduser("~"))],
    [g.Text("Output path:"), g.Input(os.path.expanduser("~"),
                                     key="ENCDEST", size=20), g.FolderBrowse("Select Path")],
    [g.Text("File Name:"), g.Input("out.b", key="ENCOUTFILENAME", size=20)],
    [g.Checkbox("Overwrite Existing File", default=False, key="ENCOVERWRITE")],
    [g.Checkbox("Create Path if Necessary",
                default=False, key="ENCCREATEPATH")],
    [g.Button("Encrypt", key="ENC")]
]

decrypt_tab_layout = [
    [g.Text("Key:"), g.Input(defaultKeyPath, size=20, key="DECKEY"), g.FileBrowse("Select Key",
                                                                                  initial_folder=os.path.expanduser("~"))],
    [g.Text("Use this tab to Decrypt a file.")],
    [g.Text("Source:"), g.Input(os.path.expanduser("~"),
                                key="DECSRC", size=20), g.FileBrowse("Select File")],
    [g.Text("Output path:"), g.Input(os.path.expanduser("~"),
                                     key="DECDEST", size=20), g.FolderBrowse("Select Path")],
    [g.Text("File Name:"), g.Input("out", key="DECOUTFILENAME", size=20)],
    [g.Checkbox("Overwrite Existing File", default=False, key="DECOVERWRITE")],
    [g.Checkbox("Create Path if Necessary",
                default=False, key="DECCREATEPATH")],
    [g.Button("Decrypt", key="DEC")]
]

# Define the tabs
tabs_layout = [
    [g.Tab("Gen Key", genkey_tab_layout)],
    [g.Tab("Encrypt", encrypt_tab_layout)],
    [g.Tab("Decrypt", decrypt_tab_layout)],
]

# Main layout
layout = [
    [g.Image("bouncer.png")],
    [g.TabGroup(tabs_layout, expand_x=True, expand_y=True)],
    [g.StatusBar("Initialized", relief="sunken", key="STATUS")],
]

# The Window
window = g.Window("Bouncer", layout, size=(
    800, 800), background_color="#000000", resizable=True, margins=(20, 20))
while True:
    event, values = window.read()
    print("Event: " + str(event))
    match event:
        case "GENKEY":
            genKey(values["GENPATH"], values["GENFILE"],
                   values["GENOVERWRITE"], values["GENCREATEPATH"])
        case "ENC":
            encryptFile(values["ENCSRC"], values["ENCDEST"], values["ENCKEY"],
                        values["ENCOUTFILENAME"], values["ENCOVERWRITE"], values["ENCCREATEPATH"])
        case "DEC":
            decryptFile(values["DECSRC"], values["DECDEST"], values["DECKEY"],
                        values["DECOUTFILENAME"], values["DECOVERWRITE"], values["DECCREATEPATH"])
        case g.WIN_CLOSED:
            break
    window.refresh()
# Event loop completed
window.close()
