from tkinter import *

window = Tk()
window.title("Flow rate to velocity Converter")

window.geometry("500x300+500+350")

# globally declare measurement variables
measurement1 = ""
measurement2 = ""


def convert_SI(flow_rate, unit_in, unit_out, diameter):  # based on unitconverters.net
    si = {'ml/min': 1, 'ml/sec': 60, 'L/min': 1000, 'L/sec': 60000,
          'cm/sec': 1, 'cm/min': 60, 'm/sec': (1/100), 'm/min': (60/100)}
    multiplier = si[unit_in]
    velocity = ((10 * float(flow_rate) * si[unit_out] * multiplier) / (6 * 3.141592653589793 * ((float(diameter)) ** 2) / 4))
    return velocity


def helpsection():
    pass  # put helpful info text here (e.g. no entering in right entry box else error)


def selectedInput():
    global measurement1
    measurement1 = listbox.get(listbox.curselection())  # whatever is currently selected

def selectedOutput():
    global measurement2
    measurement2 = listbox1.get(listbox1.curselection())  # whatever is currently selected


def converter():
    try:
        global measurement1, measurement2
        result.set(str(convert_SI(float(inputEntry.get()), measurement1, measurement2, float(inputEntry2.get()))))
    except:
        result.set("Error")


"""title = Label(window, text="Flow rate to velocity Converter", font="Calibri 14")
title.grid(columnspan=3)"""
result = StringVar()  # initalize dispalyed output variable
# create a top-level menu
filemenu = Menu(window)
filemenu.add_command(label='Help', command=helpsection)
window.config(menu=filemenu)  # displays menu
# input and output entry fields
inputEntry = Entry(window)
inputEntry.grid(row=1, column=0)
inputEntry2 = Entry(window)
inputEntry2.grid(row=3, column=0)
title = Label(window, text="diameter (mm)", font="Calibri 13")
title.grid(column=0, row=2)
title = Label(window, text="flow rate    ", font="Calibri 13")
title.grid(column=0, row=0)
arrow = Label(window, text="--->", font="Calibri 20").grid(row=1, column=1)
outputEntry = Entry(window, textvariable=result).grid(row=1, column=2)

convertButton = Button(window, text='Convert!', command=converter).grid(row=2, column=1)

listbox = Listbox(window, exportselection=False)  # left listbox
# exportselection option in order to select 2 different listbox at same time
listbox.grid(row=4, column=0)

measurement_list = ['ml/min', 'ml/sec', 'L/min', 'L/sec']
measurement_list2 = ['cm/sec', 'm/sec', 'cm/min', 'm/min']
for measurement in measurement_list:
    listbox.insert(END, measurement)

listbox.bind("<<ListboxSelect>>", lambda x: selectedInput())  # this instead of command= option

listbox1 = Listbox(window, exportselection=False)  # right listbox
listbox1.grid(row=4, column=2)

for measurement in measurement_list2:
    listbox1.insert(END, measurement)
listbox1.bind("<<ListboxSelect>>", lambda x: selectedOutput())

# configure grid layout to adjust whenever window dimensions change
for i in range(3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)


window.mainloop()
