from tkinter import *                   # import the needed libraries tkinter for this case


window = Tk()                           # we initialize a frame / window on which our app / GUI will be initiated - it can be given any name

window.title("Calculator")              # title to appear on the Gui

# Text entry screen:
text_entry = Entry(window,font="Serif 15"  )
text_entry.grid(row=0,column=0,columnspan=4)        # columnspan 4 means that the whole entry_text_window ill ocupy space equivalent to 4 buttons

indexing = 0                                # we predefine a global variable, it will be used in tracking the indecies gene the name "indexing"
#======= Opereational Functions:

    #============ displaying the clicked buttons

def click_button(value):                    # this will be function called everytime a button is clicked on the GUI calculator
    global indexing
    text_entry.insert(indexing,value)       # we insert meaning displaying the value mapped to the button clicked
    indexing += 1                           # we increase the index by one so as to accept more values / entries

    #============ clearing the clicked buttons

def clear_screen():
    global indexing
    text_entry.delete(0,END)                # using the delete method we clear the text_entry_window from(index"0", to "END)
    indexing = 0                            # we reset the index track and get it ready for a new entry

    # ============ calculating the operation using "eval" which is a python inbuilt method

def calculations():
    global indexing
    try:                                        # we cath any errors that may arise , for this case "ZeroDivisionError"
        operation = text_entry.get()
        results = eval(operation)
        text_entry.delete(0,END)
        text_entry.insert(0,f"{operation}={results}")
        indexing = 0
    except ZeroDivisionError:
        text_entry.delete(0,END)
        text_entry.insert(0,"ERROR")

# For buttons creation we need to specify several fields.
"""
1. text             --> what to be displayed on the button on the GUI / app
2. width & Height   --> dimensions for the button
3. command          --> using a lambda funtion we call the function that will be called upon button click
4. .grid(row)       --> row on which the button is to appear)
5. .grid(column)    --> column on which the button is to appear)
6. pady & paddx     --> padding for the button for y_axis and x_axis respectively


"""






# Buttons style,size,position & functions:

#====================== 1st Row =======================
button_AC = Button(window,text="Ac",width=4,height=1,command= lambda: clear_screen()).grid(row=1,column=0,pady= 5,padx= 5)
button_pareth1 = Button(window,text="(",width=4,height=1,command=lambda: click_button("(")).grid(row=1,column=1,pady= 5,padx= 5)
button_pareth2 = Button(window,text=")",width=4,height=1,command=lambda: click_button(")")).grid(row=1,column=2,pady= 5,padx= 5)
button_mult = Button(window,text="*",width=4,height=1,command= lambda: click_button("*")).grid(row=1,column=3,pady= 5,padx= 5)

#====================== 2st Row =======================
button_1 = Button(window,text="1",width=4,height=1,command= lambda: click_button(1)).grid(row=2,column=0,pady= 5,padx= 5)
button_2 = Button(window,text="2",width=4,height=1,command= lambda: click_button(2)).grid(row=2,column=1,pady= 5,padx= 5)
button_3 = Button(window,text="3",width=4,height=1,command= lambda: click_button(3)).grid(row=2,column=2,pady= 5,padx= 5)
button_div = Button(window,text="/",width=4,height=1,command= lambda: click_button("/")).grid(row=2,column=3,pady= 5,padx= 5)

#====================== 3st Row =======================
button_4 = Button(window,text="4",width=4,height=1,command= lambda: click_button(4)).grid(row=3,column=0,pady= 5,padx= 5)
button_5 = Button(window,text="5",width=4,height=1,command= lambda: click_button(5)).grid(row=3,column=1,pady= 5,padx= 5)
button_6 = Button(window,text="6",width=4,height=1,command= lambda: click_button(6)).grid(row=3,column=2,pady= 5,padx= 5)
button_add = Button(window,text="+",width=4,height=1,command= lambda: click_button("+")).grid(row=3,column=3,pady= 5,padx= 5)

#====================== 4st Row =======================
button_7 = Button(window,text="7",width=4,height=1,command= lambda: click_button(7)).grid(row=4,column=0,pady= 5,padx= 5)
button_8 = Button(window,text="8",width=4,height=1,command= lambda: click_button(8)).grid(row=4,column=1,pady= 5,padx= 5)
button_9 = Button(window,text="9",width=4,height=1,command= lambda: click_button(9),).grid(row=4,column=2,pady= 5,padx= 5)
button_sub = Button(window,text="-",width=4,height=1,command= lambda: click_button("-")).grid(row=4,column=3,pady= 5,padx= 5)

#====================== 5st Row =======================
button_decimal = Button(window,text=".",width=4,height=1,command= lambda: click_button(".")).grid(row=5,column=0,pady= 5,padx= 5)
button_0 = Button(window,text="0",width=12,height=1,command= lambda: click_button(0)).grid(row=5,column=1,columnspan= 2,pady= 5,padx= 5)
button_equals = Button(window,text="=",width=4,height=1,command= lambda: calculations()).grid(row=5,column=3,pady= 5,padx= 5)


window.mainloop()                       # we call the mainloop() function which allows our application to run until user terminates it by clicking close!!