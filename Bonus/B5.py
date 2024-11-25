import FreeSimpleGUI as sg
import B5Functions
Text1 = sg.Text("Select the Zip File to Extract: ")
data1=sg.Input()
button1 = sg.FileBrowse("Choose",key="Extract")

Text2 = sg.Text("Select the Destination: ")
data2=sg.Input()
button2 = sg.FolderBrowse("Choose",key="Folder")

button3=sg.Button("Extract",key='Final')
output = sg.Text(text_color='green',key='output')

window = sg.Window("Zip Extractor",layout=[[Text1,data1,button1],
                                           [Text2,data2,button2],
                                           [button3,output]])
while True:
    event,values=window.read()
    match event:
        case "Final":
            Data=values["Extract"]
            Destination=values["Folder"]
            B5Functions.extract_archive(Data,Destination)
            window['output'].update(value='Extraction is Successful.')
        case sg.WINDOW_CLOSED:
            break

window.close()