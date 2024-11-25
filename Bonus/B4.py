import FreeSimpleGUI as sg
Feet_to_m =0.3048
Inch_to_m =0.0254

sg.theme('Black')
feet_label=sg.Text("Enter Feet: ")
feet_input = sg.Input(key='Feet')

Inches_label = sg.Text("Enter Inches: ")
inches_input = sg.Input(key='Inches')

button = sg.Button("Convert")
button2 = sg.Button("Exit",key='Exit')

output = sg.Text(key='output')
window=sg.Window("Convertor",layout=[[feet_label,feet_input],[Inches_label,inches_input],
                                     [button,button2,output]],)

while True:
    event,values = window.read()
    answer = float(values['Feet'])*Feet_to_m + float(values['Inches'])*Inch_to_m
    window['output'].update(value=str(answer)+' m')
    if event=="Exit":
        break
window.close()
