import tkinter as tk
import tkinter.ttk as ttk
import itertools


# Introduction to  the  ttk sub module
def samplettk():
    win = tk.Tk()

    button_tk = tk.Button(win, text='tk')
    button_ttk = ttk.Button(win, text='ttk')

    button_tk.pack(padx=10, pady=10)
    button_ttk.pack(padx=10, pady=10)

    win.mainloop()


# Styling a tk widget
def samplettk02():
    """
    A list of aspects and values for styling can be found online on
    http://effbot.org/tkinterbook/tkinter-widget-styling.htm
    """
    style_1 = {
        'fg': 'red',
        'bg': 'black',
        'activebackground': 'gold',
        'activeforeground': 'dim gray'
    }
    style_2 = {
        'fg': 'yellow',
        'bg': 'grey',
        'activebackground': 'chocolate',
        'activeforeground': 'blue4'
    }
    style_cycle = itertools.cycle([style_1, style_2])

    def switch_style():
        style = next(style_cycle)
        button.configure(**style)  # used to define the keywords as a dictionary is being passed

    win = tk.Tk()

    button = tk.Button(win, text='style switch', command=switch_style)
    button.pack(padx=50, pady=50)

    win.mainloop()


def samplettk03():
    """
    styling a ttk widget
    """
    win = tk.Tk()
    style = ttk.Style()
    style_1 = {
        'foreground': 'red',
        'background': 'grey'
    }
    style_2 = {
        'foreground': 'yellow',
        'background': 'grey'
    }

    mapping_1 = {
        'background': [('pressed', 'gold'), ('active', 'magenta')]
    }
    mapping_2 = {
        'background': [('pressed', 'chocolate'), ('active', 'blue4')]
    }

    style_cycle = itertools.cycle([style_1, style_2])
    mapping_cycle = itertools.cycle([mapping_1, mapping_2])

    def switch_style():
        style_choice = next(style_cycle)
        mapping_choice = next(mapping_cycle)
        style.configure('TButton', **style_choice)
        style.map('TButton', **mapping_choice)

    button = ttk.Button(win, text='style switch', command=switch_style, style='TButton')
    button.pack(padx=50, pady=50)

    win.mainloop()


def ttksample04():
    """
    ttk Style Inheritance
    A list of all of these can be found online at:
    http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-style-layer.html
    """
    win = tk.Tk()
    regular_button = ttk.Button(win, text='regular button')
    small_button = ttk.Button(win, text='small button', style='small.TButton')
    big_button = ttk.Button(win, text='big button', style='big.TButton')
    big_dangerous_button = ttk.Button(win, text='big dangerous button', style='danger.big.TButton')
    small_dangerous_button = ttk.Button(win, text='small dangerous button', style='danger.small.TButton')

    style = ttk.Style()

    style.configure('TButton', foreground="blue4")
    style.configure('small.TButton', font=(None, 7))
    style.configure('big.TButton', font=(None, 20))
    style.configure('danger.small.TButton', foreground="red")
    style.configure('danger.big.TButton', foreground="dark red")

    regular_button.pack(padx=50, pady=50)
    small_button.pack(padx=50, pady=50)
    big_button.pack(padx=50, pady=50)
    big_dangerous_button.pack(padx=50, pady=50)
    small_dangerous_button.pack(padx=50, pady=50)

    win.mainloop()


if __name__ == '__main__':
    ttksample04()
