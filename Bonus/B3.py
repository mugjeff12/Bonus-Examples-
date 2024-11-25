import FreeSimpleGUI as sg

label1 = sg.Text("Enter Feet: ")
input1 = sg.Input()

label2 = sg.Text("Enter Inches: ")
input2 = sg.Input()

window = sg.Window("Covertor",[[label1,input1],[label2,input2]])
window.read()
window.close()