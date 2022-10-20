from tkinter.ttk import *
from tkinter import *
from tkinter.filedialog import askopenfile
import time
from VaRGUIHelper import *

ws = Tk()
ws.title('VaR Calculator')
ws.geometry('400x200')


Upload_Label = Label(
    ws,
    text='Upload excel file '
)
Upload_Label.grid(row=0, column=0, padx=10)

Upload_Button = Button(
    ws,
    text='Choose File',
    command=lambda:select_file()
)
Upload_Button.grid(row=0, column=1)


ws.mainloop()