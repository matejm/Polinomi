from Polinom import Polinom
from numerical_methods import Bisection as bisekcija


class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.wm_title('Polinomi')

        self.polinoms = []
        self.buttons = 0

        for i in range(11): self.polinoms.append(tk.Entry(self.window, relief=tk.FLAT))
        for i in range(2): self.addButton()

        tk.Button(self.window, text='+', command=self.addButton, relief=tk.FLAT).grid(row=11, column=1, padx=10, sticky='E')
        self.equation = tk.Entry(self.window, relief=tk.FLAT)
        self.equation.grid(row=12, column=1, padx=(0,10))
        tk.Button(self.window, text='Izračunaj', command=self.calc, relief=tk.FLAT).grid(row=13, column=1, padx=10, sticky='E')
        tk.Label(self.window, text='Izraz:').grid(row=12, padx=(10,0))
        self.result = tk.Label(self.window)
        self.result.grid(row=14, columnspan=2, pady=10)

    def addButton(self):
        if self.buttons < 11:
            self.polinoms[self.buttons].grid(row=self.buttons, column=1, padx=(0, 10), pady=(10,0))
            tk.Label(self.window, text=chr(ord('p')+self.buttons)+'(x) =').grid(row=self.buttons, padx=(10, 0), pady=(10,0))
            self.buttons += 1

    def calc(self):
        ps = [Polinom(i.get()) for i in self.polinoms if i.get()]
        ps = [p.coefficients[0] if p.degree == 0 else p for p in ps]
        eq = self.equation.get()
        if eq:
            for i in range(len(ps)):
                exec(chr(ord('p')+i)+' = ps[i]')    # eval doesn't support item asignment
            res = eval(eq)
            if isinstance(res, tuple) and len(res) == 2:
                self.result['text'] = 'Rezultat: ' + str(res[0]) + '\nOstanek: ' + str(res[1])
            else:
                self.result['text'] = str(res)


if __name__ == '__main__':
    import tkinter as tk
    gui = GUI()
    gui.window.mainloop()
