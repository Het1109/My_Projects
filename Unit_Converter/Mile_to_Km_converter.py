from tkinter import *

from sympy.physics.units import kilometer


def miles_toKm():
    miles = float(miles_input.get())
    kilometer = round(1.60934 * miles , 3)
    result.config(text=f"{kilometer}")





window = Tk()
window.title("Mile to Km converter.")
window.minsize(width=500 , height=300)
window.config(padx = 20 , pady = 20)



miles_input = Entry(width=7)
miles_input.grid(column = 1, row = 0)
print(miles_input.get())




# Label Names
mile = Label(text = "Miles" )
mile.grid(column = 2 , row = 0)


is_equal_to = Label(text = "is equal to")
is_equal_to.grid(column = 0 , row = 1)

result = Label(text = "0")
result.grid(column = 1, row = 1)



km = Label(text = " Km" )
km.grid(column = 2 , row = 1)

# buttons

Calculate = Button(text="Calculate" , command= miles_toKm)
Calculate.grid(column = 1 , row = 2)















































window.mainloop()
