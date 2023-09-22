from  tkinter import *

window = Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)

# label

my_label =Label(text= "I am a label", font=("Arial", 24, "bold"),)
my_label.pack(side="left")



my_label["text"] = "New text"
my_label.config(text = "New text")


# button
def button_clicked():
	print("I got clicked")
	new_text = input.get()
	my_label.config(text=new_text)



button = Button(text= "click me", command=button_clicked)
button.pack()

# entry
input= Entry(width=10)
input.pack()
print(input.get())


window.mainloop()