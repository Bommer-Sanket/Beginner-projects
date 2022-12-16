import PySimpleGUI as sg

layout = [
    [
        sg.Input( key = '-INPUT-'),
        sg.Spin(['Km to Mile', 'Kg to Pound', 'sec to min', 'Mile to Km', 'Pound to KG', 'Min to sec'], key = '-UNITS-'),
        sg.Button('Convert', key = '-CONVERT-')],
    [sg.Text('Output', key = '-OUTPUT-')]

]

window = sg.Window('Converter', layout) #check for all the keyword on google

while True:
    event, values = window.read() #check for all the keyword on google

    if event == sg.WIN_CLOSED: #check for all the keyword on google
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'Km to Mile':
                    output = round(float (input_value) * 0.6124, 2)
                    output_string = f'{input_value} km are {output} miles.'
                case 'Kg to Pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg are {output} pounds.'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} sec are {output} min.'
                case 'Mile to Km':
                    output = round(float(input_value) / 0.6124, 2)
                    output_string = f'{input_value} mile are {output} km.'
                case 'Pound to KG':
                    output = round(float(input_value) / 2.20462, 2)
                    output_string = f'{input_value} Pound are {output} KG.'
                case 'Min to sec':
                    output = round(float(input_value) * 60, 2)
                    output_string = f'{input_value} Min are {output} sec.'

            window['-OUTPUT-'].update(output_string)

        else:
            window['-OUTPUT-'].update('Please enter a valid number. Thank You')

window.close()