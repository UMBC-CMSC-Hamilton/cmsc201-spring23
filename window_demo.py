import tkinter
import tkinter.ttk as ttk

"""
your code runs -> wait for an input -> more of your code runs -> wait on input -> repeat

graphical programming:
    our code is a big while loop
    
    in tkinter the while loop is hidden in a function called mainloop()
    while (we don't want to quit yet)
        get a messge if there is one
        we can execute a little bit of code to handle that message
        pass control back to the OS
"""


def button_press():
    print('The button has been pressed')


def create_button(the_window: tkinter.Tk):
    the_button = tkinter.Button(the_window, height=5, width=20, text='My First Button', command=button_press)
    the_button.pack()


def get_the_text(edit_box: tkinter.Text):
    print(edit_box.get("1.0", "end-1c"))


def create_edit_box(the_window: tkinter.Tk):
    # width is not in pixels it's in characters... weird
    text_box = tkinter.Text(the_window, width=20, height=10)
    text_box.pack()
    print_button = tkinter.Button(the_window, text="print me out", command=lambda: get_the_text(text_box))
    print_button.pack()
    return text_box


def check_combo(x, y, z):
    print(x, y, z)


def create_combo_box(parent: tkinter.Tk, options):
    combo_string = tkinter.StringVar(parent)
    my_combo = ttk.Combobox(parent, values=options, textvariable=combo_string)
    my_combo.pack()
    combo_string.trace('uw', check_combo)


def change_value(string_value):
    print('current value is', string_value.get())


def create_radio_buttons(parent, options):
    radio_select = tkinter.StringVar(parent)
    for i, x in enumerate(options):
        rb = ttk.Radiobutton(parent, text=x, value=x, variable=radio_select, command=lambda: change_value(radio_select))
        rb.pack()


main_window = tkinter.Tk()
main_window.geometry('800x600')
main_window.title('CMSC 201 Example')

create_button(main_window)
main_text = create_edit_box(main_window)
create_combo_box(main_window, ["201", "202", "341"])
create_radio_buttons(main_window, ['a', 'b', 'c'])

main_window.mainloop()

"""
Lambda expressions:
    creating a function that doesn't have a name
"""
