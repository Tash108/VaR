from tkinter import filedialog as fd
import tkinter as tk
#from VaRgui import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd
from tkinter.ttk import *
from tkinter import *
import math
import os
def select_file():
   
   filetypes = (
      ('excel files', '*.xl*'),
      ('All files', '*.*')
   )
   filename = fd.askopenfilename(
      title='Open a file',
      initialdir='/',
      filetypes=filetypes)
   ws1 = Tk()
   ws1.title('VaR Calculator---Inputs')
   ws1.geometry('400x200')
   df = pd.read_excel(filename, index_col=[0])
   df_list = list(df.columns)
   Column_label = Label(
      ws1,
      text='Choose the column to be calculated '
   )
   Column_label.grid(row=2, column=0, padx=10)
   var = StringVar()
   column_b = Combobox(ws1, textvariable=var)
   column_b['values']=df_list
   column_b['state']='readonly'
   column_b.place(x=60, y=150)
   column_b.grid(row=2, column=1, padx=10)
   def columnbb(column_b):
      val=column_b.get()
      return val
  # get_column=Button(ws1,text="Calc",command=lambda :columnbb(column_b))
  # get_column.grid(row=4,column=1,padx=33)
   NameNewFile = Label(ws1,text="Enter the name of the file you want to save to")
   NameNewFile.grid(row=3,column=0,padx=20)

   NameNewFileEntry= tk.Entry(ws1)
   NameNewFileEntry.place(x=50,y=70)
   NameNewFileEntry.grid(row=3,column=1,padx=10)
   calculate_VaR = Button(
      ws1,
      text='Calculate VaR',
      command=lambda :VaR(df[columnbb(column_b)],0.95,510,str(NameNewFileEntry.get())+'.xlsx')
   )
   calculate_VaR.grid(row=4, columnspan=1, pady=10)

def VaR(column, Percentile, days,fileN):
   column = column.sort_values(ignore_index=True)
   postion_in_column = round(days * (1 - Percentile), 2)
   small_p = math.floor(postion_in_column)
   small_num = column[small_p - 1]
   big_p = math.ceil(postion_in_column)
   big_num = column[big_p - 1]
   remainder = postion_in_column - int(postion_in_column)
   linear_inter_num = ((1 - remainder) * small_num) + (remainder * big_num)
   List_VaR=[linear_inter_num]
   # check if size of file is 0
   if os.path.exists(fileN):
     print(fileN)
     new_df = pd.read_excel(fileN)
     print(new_df)
     new_df[column.name]=List_VaR
     tf=new_df
     print(tf)
     tf.to_excel(fileN,startcol=0, index=False)
   else:
      print("You have created a new file")
      new_df = pd.DataFrame()
      new_df[column.name] = List_VaR
      new_df.to_excel(fileN, index=False)


