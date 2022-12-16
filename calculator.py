import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)    #sg.theme('graygraygray')  instead of graygraygray you can type, sone rubish like - akujsjksajhfd, and that will give you some random color and the compiler will also give your the list of colors that are available and their names for accessing their color
    sg.set_options(font= 'Calibri 17', button_element_size = (6,3)) #here when i did not use the button_element_size, i got a problem in the ui button size, check it
    button_size = (6,3)
    layout = [
    [sg.Text('Output',
             font = 'Calibri 24',
             justification= 'right',
             expand_x= True,
             pad= (10,20),
             right_click_menu= theme_menu,
             key = '-TEXT-')], #---> here justification was used to adjust the place where you want to show output and expand to use the whole row for output
    #[sg.Push(),sg.Text('Output', font = 'Calibri 24')], ---> this will push the output to right side of the calculator
    [sg.Button('Enter', expand_x= True), sg.Button('Clear', expand_x= True)],
    [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('*', size = button_size)],
    [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('/', size = button_size)],
    [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', size = button_size)],
    [sg.Button(0, expand_x= True), sg.Button('.', size = button_size), sg.Button('+', size = button_size)]
    ]

    return sg.Window('Calculator', layout)

# in the above layout, taking a example---> [sg.Button(7)], to adjust the size of a botton and custimize it according to one's own wisch, we can write it as --->  [sg.Button(7, size (5,3)), but in the above we have given the size value to 'button_size' sinc we are using it for all the elemnts/buttons
# expand_x is a parameter through which we have expanded the size of button of 0, enter and clear. check its description online and paste it hear.
#also check the function of pad = (10,20), it was used here to give the gap betweent the output and button

# [1] sg.theme() --> if it is written here, then the color of buttorn/elemnts cannot be changed so we are using above.


theme_menu = ['Menu', ['LightGrey', 'dark', 'DarkGray8', 'random']]
window = create_window('dark')

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)


    if event in ['+', '-', '*', '/']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-TEXT-'].update('')

    if event == 'Enter':
        full_operation.append(''.join(current_num))
        result = eval(''.join(full_operation))
        window['-TEXT-'].update(result)
        full_operation = []


    if event == 'Clear':
        current_num = []
        full_operation = []
        window['-TEXT-'].update('')

window.close()


