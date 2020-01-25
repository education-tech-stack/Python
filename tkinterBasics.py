import tkinter as tk
import tkinter.messagebox as msgbox


# opening the main window for the first time
class Window01(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello Tkinter')

        label = tk.Label(self, text='Hello World')
        label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)


# adding interactivity to the main window with Tkinter-compatible variables
class Window02(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello Tkinter')

        self.label_text = tk.StringVar()
        self.label_text.set('Choose one')

        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)

        hello_button = tk.Button(self, text='Say Hello', command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        goodbye_button = tk.Button(self, text='say good bye', command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        # self.label.configure(text='HEllo World')
        # self.label_text.set('Hello World!')
        msgbox.showinfo('Hello', 'Hello World!')

    def say_goodbye(self):
        # self.label.configure(text='good bye! \n (Closing in 2 seconds)')
        '''self.label_text.set('GoodBye! \n (Closing in 2 seconds)')
        msgbox.showinfo('Goodbye!', 'Goodbye, its been fun!')
        self.after(2000, self.destroy)'''
        if msgbox.askyesno('Close Window?', 'would you like to close this window?'):
            self.label_text.set('window will close in 2 seconds')
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo('Not Closing', 'Great! This window will stays open')


class Window03(tk.Tk):
    """
    Getting text input
    """
    def __init__(self):
        super().__init__()
        self.title('Hello Tkinter')

        self.label_text = tk.StringVar()
        self.label_text.set('My Name is: ')

        self.name_text = tk.StringVar()

        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=10)

        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        hello_button = tk.Button(self, text='Say Hello', command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        goodbye_button = tk.Button(self, text='say good bye', command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        msgbox.showinfo('Hello', 'Hello '+self.name_entry.get())

    def say_goodbye(self):
        if msgbox.askyesno('Close Window?', 'would you like to close this window?'):
            self.label_text.set('window will close in 2 seconds - Goodbye! '+self.name_text.get())
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo('Not Closing', 'Great! This window will stays open')


if __name__ == '__main__':
    window = Window03()
    window.mainloop()
