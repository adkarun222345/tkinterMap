from tkinter import *
from tkinter import ttk
import tkintermapview as tkmap


def show_location():
    addy = location.get()
    show_map.set_address(addy, marker=True)
    

root = Tk()
root.title("Interactive Map")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)

top_frame = Frame(root)
top_frame.grid(column=0, row=0, sticky=NSEW)

bottom_frame = Frame(root)
bottom_frame.grid(column=0, row=1, sticky=NSEW)

location = StringVar()
info_label = Label(top_frame, text="Enter City, State & Country:", font=("Helvetica", 12))
info_label.grid(column=0, row=0, padx=30, pady=15, sticky=E)

where_label = Entry(top_frame, width=50, font=("Helvetica", 12), textvariable=location)
where_label.grid(column=1, row=0, padx=10, pady=20, sticky=NSEW)

go_btn = Button(top_frame, text="Find on Map", font=("Helvetica", 12), command=show_location)
go_btn.grid(column=2, row=0, padx=20, pady=20, sticky=NSEW)

sep_stick = ttk.Separator(top_frame, orient=HORIZONTAL)
sep_stick.grid(column=0, row=1, columnspan=3, pady=5, padx=50, sticky=NSEW)


show_map = tkmap.TkinterMapView(bottom_frame, width=900, height=600, corner_radius=0)
show_map.grid(column=0, row=0, padx=30, pady=20, sticky=NSEW)

root.mainloop()
