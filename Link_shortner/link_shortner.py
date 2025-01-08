from tkinter import *
import pyshorteners

window = Tk()
window.title("URL Shortner")
window.minsize(width=500 , height=250)



# Label Names
long = Label(text = "Enter Long URL" )
long.pack()


# Entry

longurl_entry = Entry()
longurl_entry.pack()


# Label Names
short = Label(text = "Output Shortened URL" )
short.pack()


# Entry

shorturl_entry = Entry()
shorturl_entry.pack()


def  shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.delete(0, END)  # Clear the entry box
    shorturl_entry.insert(0, short_url)  # Insert the shortened URL
    # print(shorturl_entry.insert(0, short_url))

shorten_button = Button(text="Shorten URL" , command=shorten)
shorten_button.pack()













window.mainloop()
