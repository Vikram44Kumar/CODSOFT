import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.root.configure(bg='#ADD8E6')
        self.root.resizable(width=False, height=False)
        self.create_widgets()
        self.current = ''
        self.inp_value = True
        self.result = False

    def create_widgets(self):
        self.ent_field = tk.Entry(self.root, bg='#ADD8E6', fg='#000080', font=('Arial', 25),
                                  borderwidth=10, justify="right")
        self.ent_field.grid(row=0, columnspan=10, padx=10, pady=10,
                            sticky='n'+'s'+'e'+'w')
        self.ent_field.insert(0, '0')

        button_text = ['7', '8', '9', '/',
                       '4', '5', '6', '*',
                       '1', '2', '3', '-',
                       '0', '.', '=', '+']

        button = []
        i = 0
        for j in range(2, 6):
            for k in range(4):
                button.append(tk.Button(self.root, text=button_text[i], font=('Arial', 10, 'bold'),
                                        fg="red", width=6, height=2,
                                        highlightbackground='#ADD8E6', highlightthickness=2))
                button[i].grid(row=j, column=k, sticky='n' +
                               's'+'e' + 'w', padx=10, pady=10)
                button[i]["command"] = lambda x=button_text[i]: self.button_click(x)
                i += 1

    def button_click(self, text):
        if text == '=':
            try:
                self.current = str(eval(self.current))
                self.entry_field(self.current)
            except Exception as e:
                self.current = 'Error'
                self.entry_field(self.current)
        else:
            if self.current == 'Error':
                self.current = ''
            self.current += text
            self.entry_field(self.current)

    def entry_field(self, value):
        self.ent_field.delete(0, 'end')
        self.ent_field.insert(0, value)


if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
