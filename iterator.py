# imports

# imports for GUI(Tkinter)
from tkinter import *
from tkinter import ttk
import tkinter as tk  

# imports for background
from system_hotkey import SystemHotkey
import pyautogui
import time
import threading

# import for notifications
from plyer import notification

#------------------------------------------------------------------------------
#------------------------------------Tkinter-----------------------------------
#------------------------------------------------------------------------------

global dictionary
global hotkey

root = Tk()
root.geometry('500x265')
root.resizable(False, False)
root.title("Iterator")
root.iconbitmap(r'icon.ico')

#------------------------------------------------------------------------------

# frames used in this application

# window frame
window = Frame(root, highlightbackground="green", highlightcolor="green",\
               highlightthickness=1, width=500, height=265, bd= 0).pack()

# hotkey frame
hotkey_frame = Frame(root, width=245, height= 75, bd= 0, relief =  RIDGE,\
                     background="gray87",borderwidth=1)\
                     .place(x = 250,y = 5)

# iterate notify frame
iterate_notify_frame = Frame(root, width=490, height= 60, bd= 0,\
                             relief =  RIDGE,\
                             background="gray87",borderwidth=1)\
                     .place(x = 5, y = 80)

# save as frame
save_as_frame = Frame(root, width=490, height= 60, bd= 0,\
                      relief =  RIDGE, background="gray87",borderwidth=1)\
                     .place(x = 5, y = 140)
# buttons frame
buttons_frame = Frame(root, width=490, height= 60, bd= 0,\
                      relief =  RIDGE, background="gray87",borderwidth=1)\
                     .place(x = 5, y = 200)

#------------------------------------------------------------------------------

#these lines used to place the image in the application

photo = PhotoImage(file="image.PNG")
photo_label = Label(root, image= photo).place(x = 50, y = 5)

#------------------------------------------------------------------------------

# Hotkeys label
hotkey_label = Label(hotkey_frame, text = " HotKey ",relief=RIDGE)\
               .place(x = 310,y = 30)

# ComboBox select
combo_values = [ "ctrl+1",
                 "alt+1",
                 "ctrl+F2",
                 "alt+F2",
                 "shift+F2"
]
hotkey_select = ttk.Combobox(hotkey_frame,width=10, values= combo_values,\
                             state=NORMAL)
hotkey_select.set("ctrl+1")
hotkey_select.place(x = 370,y = 30)

#------------------------------------------------------------------------------

# Iterate label
iterate_label = Label(root, text = " Iterate from ",relief=RIDGE)\
                .place(x =50, y = 102)

# Iterate from CheckBox
iterate_checkbox_variable = IntVar()
iterate_checkbox = Checkbutton(root, variable = iterate_checkbox_variable,\
                               onvalue = 1, offvalue = 0, relief=RIDGE,\
                               state=NORMAL)
iterate_checkbox.place(x =20, y = 100)

# Iterate from entry
iterate_entry_textvariable = IntVar()
iterate_entry = Entry(root,width=10,textvariable = iterate_entry_textvariable,\
                      state= NORMAL)

    
iterate_entry_textvariable.set("1")
iterate_entry.place(x = 130,y = 103)

#------------------------------------------------------------------------------

# notify
notify_label = Label(root, text = "  Notify  ",relief=RIDGE)\
               .place(x = 310,y = 102)

# notify checkbox
notify_checkbox_variable = IntVar()
notify_checkbox = Checkbutton(root, variable=notify_checkbox_variable,\
                              onvalue = 1, offvalue = 0, relief=RIDGE)
notify_checkbox.place(x =280, y = 100)

# notify entry
notify_entry = Entry(root, width=10)
notify_entry.place(x = 370,y = 103)

#------------------------------------------------------------------------------

# text prefix label
save_as_label = Label(root, text = " Save as ",relief=RIDGE)\
                .place(x =50, y = 162)

# text prefix_checkbox
save_as_checkbox_variable = IntVar()
save_as_checkbox = Checkbutton(root, variable=save_as_checkbox_variable,\
                               onvalue = 1, offvalue = 0, relief=RIDGE)
save_as_checkbox.place(x =20, y = 160)

# text prefix  entry
save_as_entry = Entry(root, width=40)
save_as_entry.place(x = 110,y = 163)

#------------------------------------------------------------------------------

#buttons

# target fucntion for start button
def start_button_command():
    thread_start()
    start_button.config(state="disabled")
    start_button.config(bg="gray72")
    pause_button.config(state="normal")
    update_button.config(state="disabled")
    pause_button.config(bg="gray93")
    select_generator_initialization()
    iterate_entry.config(state="disabled")
    iterate_checkbox.config(state="disabled")
    hotkey_select.config(state="disabled")
    root.iconify()
   
# start button
start_button = Button(root,text = " Start ", borderwidth=2, relief=RAISED,\
                      activeforeground="blue",activebackground="gray68",\
                      width=8, height=2,command = start_button_command,\
                      state=NORMAL)
start_button.place(x= 20, y=210)


# target function for update button
def update_button_command():
    pause_button.config(state="normal")
    update_button.config(state="disabled")
    hot_key_variable = hotkey_select.get()
    set_hotkey_register(hot_key_variable)
    update_button.config(bg="gray68")
    pause_button.config(bg="gray93")
    iterate_entry.config(state="disabled")
    iterate_checkbox.config(state="disabled")
    select_generator_initialization_update()
    hotkey_select.config(state="disabled")
   
# update button
update_button = Button(root,text = " Update ", borderwidth=2, relief=RAISED,\
                      activeforeground="green",activebackground="gray68",\
                      width=8, height=2, command = update_button_command,\
                       state=DISABLED,bg="gray72")
update_button.place(x= 100, y=210)                    

# target function for pause button
def pause_button_command():
    hot_key_variable = hotkey_select.get()
    hotkey_un_register(hot_key_variable)
    pause_button.config(state="disabled")
    update_button.config(state="normal")
    pause_button.config(bg="gray68")
    update_button.config(bg="gray93")
    iterate_entry.config(state="normal")
    iterate_checkbox.config(state="normal")
    hotkey_select.config(state="normal")

# pause button    
pause_button = Button(root,text = " Pause ", borderwidth=2, relief=RAISED,\
                      activeforeground="red",activebackground="gray68",\
                      width=8, height=2, command = pause_button_command,\
                      state=DISABLED,bg="gray72")
pause_button.place(x= 180, y=210)


# roshan stark label
roshanstark_label = Label(hotkey_frame, text = " Developer: Roshan Stark ")\
                    .place(x = 350,y = 235)



#------------------------------------------------------------------------------
#------------------------------------Background--------------------------------
#------------------------------------------------------------------------------

# this function returns the notify interger 
def get_notify_value():
    if notify_checkbox_variable.get() == 1:
        notify_entry_variable = int(notify_entry.get())
        return notify_entry_variable

# start button command function calls this function
# used to start get the starting value of iteration
def select_generator_initialization():
    global received_generator_numbers
    if iterate_checkbox_variable.get() == 1:
        received_iterate_entry = iterate_entry.get()        
        received_generator_numbers = number_generator(received_iterate_entry)
    else:
        received_generator_numbers = number_generator(1)

# update button command function calls this function
# used to update iterate value
def select_generator_initialization_update():
    if iterate_checkbox_variable.get() == 1:
        received_iterate_entry = iterate_entry.get()        
        received_generator_numbers = number_generator(received_iterate_entry)


# this function generates numbers
def number_generator(j):
    global i
    i = int(j)
    while True:
        yield i
        i += 1


# dictionary used to create comboselect keys and appropriate values
dictionary = { 'ctrl+1':('control', '1'),
               'alt+1':('alt', '1'),
               'ctrl+F2':('control', 'f2'),
               'alt+F2':('alt', 'f2'),
               'shift+F2':('shift', 'f2')
              }


# function used for creating notification
def notify_function(received_notify_value):
    received_notify_value_tostring = str(received_notify_value)
    string_value = 'reached '+ received_notify_value_tostring
    notification.notify(
    title='Iterator Notification',
    message=string_value,
    app_icon='icon.ico',    # e.g. 'C:\\icon_32x32.ico'
    timeout=10,         # seconds
    )


# save as function (i.e it returns the name of the file to be saved)
def save_as(i):
    string_value_of_received = str(i)
    if save_as_checkbox_variable.get() == 1:
        received_save_as_entry = save_as_entry.get()
        received_save_as_entry_tostring = received_save_as_entry
        return received_save_as_entry_tostring+"_"+string_value_of_received
    else:
        received_save_as_entry = save_as_entry.get()
        received_save_as_entry_tostring = received_save_as_entry
        return 'save'+'_'+string_value_of_received
         
# this function gets executed when hotkey is pressed   
def execute(x, y, z):
    print('execute executed')
    print(next(received_generator_numbers))
    received_notify_value = get_notify_value()
    if received_notify_value == i:
        notify_function(received_notify_value)
    time.sleep(1)
    pyautogui.hotkey('ctrl','s')
    save_as_string_variable = save_as(i)
    time.sleep(1)
    pyautogui.typewrite(save_as_string_variable)
    pyautogui.press('enter')


# defining hotkey
hotkey = SystemHotkey(consumer = execute)

# registering a hotkey
def set_hotkey_register(hot_key_variable):
    for key_reg, value_reg in dictionary.items():
        if hot_key_variable == key_reg:
            hotkey.register(value_reg, callback=lambda:print("Easy!"))


# unregistering a hotkey
def hotkey_un_register(hot_key_variable):
    for key_unreg, value_unreg in dictionary.items():
        if hot_key_variable == key_unreg:
            hotkey.unregister(value_unreg)


# target function of thread (i.ethread starts from here)
def execute_thread():
    time.sleep(1)
    print('executed')
    hot_key_variable = hotkey_select.get()
    set_hotkey_register(hot_key_variable)
    
# this line creates a thead     
thread_variable = threading.Thread(target=execute_thread)

# this function used to start a thread when start button is pressed
def thread_start():
    thread_variable.start()

#------------------------------------------------------------------------------
# main loop of tkinter

root.mainloop()

#------------------------------------------------------------------------------





