from tkinter import *

def miles_to_km():
    miles=float(miles_input.get())
    km=miles*1.609
    Kilometer_result_label.config(text=f"{km}")

window=Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

miles_input=Entry()
miles_input.grid(row=0,column=1)

miles_label=Label(text="Miles")
miles_label.grid(row=0,column=2)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(row=1,column=0)

Kilometer_result_label=Label(text="0")
Kilometer_result_label.grid(row=1,column=1)

Kilometer_label=Label(text="Km")
Kilometer_label.grid(row=1,column=2)

calculate_button=Button(text="Calculate",command=miles_to_km)
calculate_button.grid(row=2,column=1)

window.mainloop()
