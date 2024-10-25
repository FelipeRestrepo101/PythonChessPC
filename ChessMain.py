import tkinter as tk

#set up class that inherits from tk.Label class but sets the specified parameters to their specified values (it works but I still dont understand how)
class Square(tk.Label):
    def __init__(self, text):
        super().__init__(master=window, text=text, background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))

window = tk.Tk()
window.title('Chess Game')
window.geometry('900x600')

#instantiation of the created class that is meant to replace tk.Label
a1 = Square('1')




#define labels

# a1 = tk.Label(window, text='a1', background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))
a2 = tk.Label(window, text='a2', background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))
a3 = tk.Label(window, text='a3', background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))

b1 = tk.Label(window, text='b1', background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))
b2 = tk.Label(window, text='b2', background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))
b3 = tk.Label(window, text='b3', background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))

c1 = tk.Label(window, text='c1', background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))
c2 = tk.Label(window, text='c2', background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))
c3 = tk.Label(window, text='c3', background='white', anchor='center', borderwidth=2, relief="solid", font=('arial', 60))

# define grid columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

#define grid rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

#place labels within grid
a1.grid(row = 0, column = 0, sticky='nsew', padx=(100,0))
a2.grid(row = 1, column = 0, sticky='nsew', padx=(100,0))
a3.grid(row = 2, column = 0, sticky='nsew', padx=(100,0))

b1.grid(row = 0, column = 1, sticky='nsew')
b2.grid(row = 1, column = 1, sticky='nsew')
b3.grid(row = 2, column = 1, sticky='nsew')

c1.grid(row = 0, column = 2, sticky='nsew', padx=(0,100))
c2.grid(row = 1, column = 2, sticky='nsew', padx=(0,100))
c3.grid(row = 2, column = 2, sticky='nsew', padx=(0,100))

window.mainloop()