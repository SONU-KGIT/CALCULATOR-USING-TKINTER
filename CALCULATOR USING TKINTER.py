import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="#282c34") 

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_ui()

    def create_ui(self):
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 20), bd=10, insertwidth=2,
                                width=14, justify="right", bg="#dcdcdc", fg="#000000")
        result_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 15),
                               command=lambda t=text: self.on_button_click(t),
                               bg="#444c56", fg="#ffffff", activebackground="#3e444e", activeforeground="#ffffff",
                               relief="raised")
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if char == '=':
            try:
                result = eval(current_text)
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        else:
            if current_text == "Error":
                self.result_var.set(char)
            else:
                self.result_var.set(current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
