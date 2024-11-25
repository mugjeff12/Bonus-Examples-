import FreeSimpleGUI as sg
import functions
label1  = sg.Text("Select Files To Compress: ")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Choose The Destination Folder: ")
input2 = sg.Input()
button2 = sg.FolderBrowse("Browse", key='folder')
compress_button = sg.Button("Compress")

output_label = sg.Text(key='output')
window = sg.Window("Compressor",layout=[[label1,input1,button1],[label2,input2,button2]
    ,[compress_button,output_label]])


while True:
    event,values=window.read()
    print(event)
    print(values)
    filepaths = values["files"].split(';')
    folder = values["folder"]
    print(filepaths)
    print(folder)
    functions.make_archive(filepaths,folder)
    window['output'].update(value="Compression Successful")
window.close()