import tkinter as tk

#set up class that inherits from tk.Label class but sets the specified parameters to their specified values 
class Square(tk.Label):
    def __init__(self, text, background='white'):
        super().__init__(master=window, text=text, background=background, anchor='center', borderwidth=2, relief="solid", font=('arial', 30))
        self.text = text
        self.background = background

window = tk.Tk()
window.title('Chess Game')
window.geometry('900x600')

# dictionary where square objects can be accessed
squares = {

#using instantiation of the Square class within a dictionary to define labels
'a1' : Square('a1'), #, background='saddle brown')
'a2' : Square('a2'), #, background='sandy brown')
'a3' : Square('a3'),
'a4' : Square('a4'),
'a5' : Square('a5'),
'a6' : Square('a6'),
'a7' : Square('a7'),
'a8' : Square('a8'),

'b1' : Square('b1'),
'b2' : Square('b2'),
'b3' : Square('b3'),
'b4' : Square('b4'),
'b5' : Square('b5'),
'b6' : Square('b6'),
'b7' : Square('b7'),
'b8' : Square('b8'),

'c1' : Square('c1'),
'c2' : Square('c2'),
'c3' : Square('c3'),
'c4' : Square('c4'),
'c5' : Square('c5'),
'c6' : Square('c6'),
'c7' : Square('c7'),
'c8' : Square('c8'),

'd1' : Square('d1'),
'd2' : Square('d2'),
'd3' : Square('d3'),
'd4' : Square('d4'),
'd5' : Square('d5'),
'd6' : Square('d6'),
'd7' : Square('d7'),
'd8' : Square('d8'),

'e1' : Square('e1'),
'e2' : Square('e2'),
'e3' : Square('e3'),
'e4' : Square('e4'),
'e5' : Square('e5'),
'e6' : Square('e6'),
'e7' : Square('e7'),
'e8' : Square('e8'),

'f1' : Square('f1'),
'f2' : Square('f2'),
'f3' : Square('f3'),
'f4' : Square('f4'),
'f5' : Square('f5'),
'f6' : Square('f6'),
'f7' : Square('f7'),
'f8' : Square('f8'),

'g1' : Square('g1'),
'g2' : Square('g2'),
'g3' : Square('g3'),
'g4' : Square('g4'),
'g5' : Square('g5'),
'g6' : Square('g6'),
'g7' : Square('g7'),
'g8' : Square('g8'),

'h1' : Square('h1'),
'h2' : Square('h2'),
'h3' : Square('h3'),
'h4' : Square('h4'),
'h5' : Square('h5'),
'h6' : Square('h6'),
'h7' : Square('h7'),
'h8' : Square('h8')

}






# define grid columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)
window.columnconfigure(7, weight=1)


#define grid rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)

#place labels within grid, calls each label by accessing the Square object inside the dictionary
squares['a1'].grid(row = 0, column = 0, sticky='nsew', padx=(100,0))
squares['a2'].grid(row = 1, column = 0, sticky='nsew', padx=(100,0))
squares['a3'].grid(row = 2, column = 0, sticky='nsew', padx=(100,0))
squares['a4'].grid(row = 3, column = 0, sticky='nsew', padx=(100,0))
squares['a5'].grid(row = 4, column = 0, sticky='nsew', padx=(100,0))
squares['a6'].grid(row = 5, column = 0, sticky='nsew', padx=(100,0))
squares['a7'].grid(row = 6, column = 0, sticky='nsew', padx=(100,0))
squares['a8'].grid(row = 7, column = 0, sticky='nsew', padx=(100,0))

#Column b
squares['b1'].grid(row=0, column=1, sticky='nsew')
squares['b2'].grid(row=1, column=1, sticky='nsew')
squares['b3'].grid(row=2, column=1, sticky='nsew')
squares['b4'].grid(row=3, column=1, sticky='nsew')
squares['b5'].grid(row=4, column=1, sticky='nsew')
squares['b6'].grid(row=5, column=1, sticky='nsew')
squares['b7'].grid(row=6, column=1, sticky='nsew')
squares['b8'].grid(row=7, column=1, sticky='nsew')

#Column c
squares['c1'].grid(row=0, column=2, sticky='nsew')
squares['c2'].grid(row=1, column=2, sticky='nsew')
squares['c3'].grid(row=2, column=2, sticky='nsew')
squares['c4'].grid(row=3, column=2, sticky='nsew')
squares['c5'].grid(row=4, column=2, sticky='nsew')
squares['c6'].grid(row=5, column=2, sticky='nsew')
squares['c7'].grid(row=6, column=2, sticky='nsew')
squares['c8'].grid(row=7, column=2, sticky='nsew')

#Column d
squares['d1'].grid(row=0, column=3, sticky='nsew')
squares['d2'].grid(row=1, column=3, sticky='nsew')
squares['d3'].grid(row=2, column=3, sticky='nsew')
squares['d4'].grid(row=3, column=3, sticky='nsew')
squares['d5'].grid(row=4, column=3, sticky='nsew')
squares['d6'].grid(row=5, column=3, sticky='nsew')
squares['d7'].grid(row=6, column=3, sticky='nsew')
squares['d8'].grid(row=7, column=3, sticky='nsew')

#Column e
squares['e1'].grid(row=0, column=4, sticky='nsew')
squares['e2'].grid(row=1, column=4, sticky='nsew')
squares['e3'].grid(row=2, column=4, sticky='nsew')
squares['e4'].grid(row=3, column=4, sticky='nsew')
squares['e5'].grid(row=4, column=4, sticky='nsew')
squares['e6'].grid(row=5, column=4, sticky='nsew')
squares['e7'].grid(row=6, column=4, sticky='nsew')
squares['e8'].grid(row=7, column=4, sticky='nsew')

#Column f
squares['f1'].grid(row=0, column=5, sticky='nsew')
squares['f2'].grid(row=1, column=5, sticky='nsew')
squares['f3'].grid(row=2, column=5, sticky='nsew')
squares['f4'].grid(row=3, column=5, sticky='nsew')
squares['f5'].grid(row=4, column=5, sticky='nsew')
squares['f6'].grid(row=5, column=5, sticky='nsew')
squares['f7'].grid(row=6, column=5, sticky='nsew')
squares['f8'].grid(row=7, column=5, sticky='nsew')

#Column g
squares['g1'].grid(row=0, column=6, sticky='nsew')
squares['g2'].grid(row=1, column=6, sticky='nsew')
squares['g3'].grid(row=2, column=6, sticky='nsew')
squares['g4'].grid(row=3, column=6, sticky='nsew')
squares['g5'].grid(row=4, column=6, sticky='nsew')
squares['g6'].grid(row=5, column=6, sticky='nsew')
squares['g7'].grid(row=6, column=6, sticky='nsew')
squares['g8'].grid(row=7, column=6, sticky='nsew')

#Columnh
squares['h2'].grid(row=1, column=7, sticky='nsew', padx=(0, 100))
squares['h3'].grid(row=2, column=7, sticky='nsew', padx=(0, 100))
squares['h4'].grid(row=3, column=7, sticky='nsew', padx=(0, 100))
squares['h5'].grid(row=4, column=7, sticky='nsew', padx=(0, 100))
squares['h6'].grid(row=5, column=7, sticky='nsew', padx=(0, 100))
squares['h7'].grid(row=6, column=7, sticky='nsew', padx=(0, 100))
squares['h8'].grid(row=7, column=7, sticky='nsew', padx=(0, 100))
squares['h1'].grid(row=0, column=7, sticky='nsew', padx=(0, 100))

window.mainloop()