import tkinter as tk

#set up class that inherits from tk.Label class but sets the specified parameters to their specified values 
class Square(tk.Label):
    def __init__(self, text):
        super().__init__(master=window, text=text, background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 30))

window = tk.Tk()
window.title('Chess Game')
window.geometry('900x600')




#using instantiation of the Square class to define labels
a1 = Square('a1')
a2 = Square('a2')
a3 = Square('a3')
a4 = Square('a4')
a5 = Square('a5')
a6 = Square('a6')
a7 = Square('a7')
a8 = Square('a8')

b1 = Square('b1')
b2 = Square('b2')
b3 = Square('b3')
b4 = Square('b4')
b5 = Square('b5')
b6 = Square('b6')
b7 = Square('b7')
b8 = Square('b8')

c1 = Square('c1')
c2 = Square('c2')
c3 = Square('c3')
c4 = Square('c4')
c5 = Square('c5')
c6 = Square('c6')
c7 = Square('c7')
c8 = Square('c8')

d1 = Square('d1')
d2 = Square('d2')
d3 = Square('d3')
d4 = Square('d4')
d5 = Square('d5')
d6 = Square('d6')
d7 = Square('d7')
d8 = Square('d8')

e1 = Square('e1')
e2 = Square('e2')
e3 = Square('e3')
e4 = Square('e4')
e5 = Square('e5')
e6 = Square('e6')
e7 = Square('e7')
e8 = Square('e8')

f1 = Square('f1')
f2 = Square('f2')
f3 = Square('f3')
f4 = Square('f4')
f5 = Square('f5')
f6 = Square('f6')
f7 = Square('f7')
f8 = Square('f8')

g1 = Square('g1')
g2 = Square('g2')
g3 = Square('g3')
g4 = Square('g4')
g5 = Square('g5')
g6 = Square('g6')
g7 = Square('g7')
g8 = Square('g8')

h1 = Square('h1')
h2 = Square('h2')
h3 = Square('h3')
h4 = Square('h4')
h5 = Square('h5')
h6 = Square('h6')
h7 = Square('h7')
h8 = Square('h8')


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

#place labels within grid
a1.grid(row = 0, column = 0, sticky='nsew', padx=(100,0))
a2.grid(row = 1, column = 0, sticky='nsew', padx=(100,0))
a3.grid(row = 2, column = 0, sticky='nsew', padx=(100,0))
a4.grid(row = 3, column = 0, sticky='nsew', padx=(100,0))
a5.grid(row = 4, column = 0, sticky='nsew', padx=(100,0))
a6.grid(row = 5, column = 0, sticky='nsew', padx=(100,0))
a7.grid(row = 6, column = 0, sticky='nsew', padx=(100,0))
a8.grid(row = 7, column = 0, sticky='nsew', padx=(100,0))

# Column b
b1.grid(row=0, column=1, sticky='nsew')
b2.grid(row=1, column=1, sticky='nsew')
b3.grid(row=2, column=1, sticky='nsew')
b4.grid(row=3, column=1, sticky='nsew')
b5.grid(row=4, column=1, sticky='nsew')
b6.grid(row=5, column=1, sticky='nsew')
b7.grid(row=6, column=1, sticky='nsew')
b8.grid(row=7, column=1, sticky='nsew')

# Column c
c1.grid(row=0, column=2, sticky='nsew')
c2.grid(row=1, column=2, sticky='nsew')
c3.grid(row=2, column=2, sticky='nsew')
c4.grid(row=3, column=2, sticky='nsew')
c5.grid(row=4, column=2, sticky='nsew')
c6.grid(row=5, column=2, sticky='nsew')
c7.grid(row=6, column=2, sticky='nsew')
c8.grid(row=7, column=2, sticky='nsew')

# Column d
d1.grid(row=0, column=3, sticky='nsew')
d2.grid(row=1, column=3, sticky='nsew')
d3.grid(row=2, column=3, sticky='nsew')
d4.grid(row=3, column=3, sticky='nsew')
d5.grid(row=4, column=3, sticky='nsew')
d6.grid(row=5, column=3, sticky='nsew')
d7.grid(row=6, column=3, sticky='nsew')
d8.grid(row=7, column=3, sticky='nsew')

# Column e
e1.grid(row=0, column=4, sticky='nsew')
e2.grid(row=1, column=4, sticky='nsew')
e3.grid(row=2, column=4, sticky='nsew')
e4.grid(row=3, column=4, sticky='nsew')
e5.grid(row=4, column=4, sticky='nsew')
e6.grid(row=5, column=4, sticky='nsew')
e7.grid(row=6, column=4, sticky='nsew')
e8.grid(row=7, column=4, sticky='nsew')

# Column f
f1.grid(row=0, column=5, sticky='nsew')
f2.grid(row=1, column=5, sticky='nsew')
f3.grid(row=2, column=5, sticky='nsew')
f4.grid(row=3, column=5, sticky='nsew')
f5.grid(row=4, column=5, sticky='nsew')
f6.grid(row=5, column=5, sticky='nsew')
f7.grid(row=6, column=5, sticky='nsew')
f8.grid(row=7, column=5, sticky='nsew')

# Column g
g1.grid(row=0, column=6, sticky='nsew')
g2.grid(row=1, column=6, sticky='nsew')
g3.grid(row=2, column=6, sticky='nsew')
g4.grid(row=3, column=6, sticky='nsew')
g5.grid(row=4, column=6, sticky='nsew')
g6.grid(row=5, column=6, sticky='nsew')
g7.grid(row=6, column=6, sticky='nsew')
g8.grid(row=7, column=6, sticky='nsew')

# Columnh
h2.grid(row=1, column=7, sticky='nsew', padx=(0, 100))
h3.grid(row=2, column=7, sticky='nsew', padx=(0, 100))
h4.grid(row=3, column=7, sticky='nsew', padx=(0, 100))
h5.grid(row=4, column=7, sticky='nsew', padx=(0, 100))
h6.grid(row=5, column=7, sticky='nsew', padx=(0, 100))
h7.grid(row=6, column=7, sticky='nsew', padx=(0, 100))
h8.grid(row=7, column=7, sticky='nsew', padx=(0, 100))
h1.grid(row=0, column=7, sticky='nsew', padx=(0, 100))

window.mainloop()