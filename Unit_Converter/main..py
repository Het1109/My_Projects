from tkinter import *

window = Tk()
window.title("My GUI ")
window.minsize(width=500 , height=300)

# Label
my_label = Label(text = "I Am a Label" , font=("Arial" , 24 , "bold"))
my_label.pack()


my_label["text"] = "New Text 1"
my_label.config(text="New Text 2")

# buttons
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = Button(text="Het Patel" , command=button_clicked)
button.pack()

# Entry

input = Entry()
input.pack()
print(input.get())

# text box
text = Text(height=5 , width=30)
text.focus()
text.insert(END , "Example of multiline text entry.")
print(text.get("1.0" , END))
text.pack()


# spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command= spinbox_used)  # Use lambda to call the function
spinbox.pack()


# scale
def scale_used(value):
    print(value)

scale = Scale(from_=0 , to= 100 , command=scale_used)
scale.pack()


# checkbox
def checkbox_used():
#     1 --> checkbox checked else 0
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?" , variable=checked_state , command=checkbox_used)
checked_state.get()
checkbutton.pack()



# Radio Button
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1" , value= 1 , variable=radio_state , command=radio_used)
radiobutton2 = Radiobutton(text="Option 2" , value= 2 , variable=radio_state , command=radio_used)
radiobutton3 = Radiobutton(text="Option 3" , value= 3 , variable=radio_state , command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()



# List box
def listbox_used():
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple" , "Pear" , "Orange", "Banana" ]
for item in fruits:
    listbox.insert(fruits.index(item) , item)

listbox.bind("<<ListboxSelect>>" , listbox_used)
listbox.pack()











window.mainloop()
