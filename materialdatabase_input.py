from tkinter import*
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import sqlite3
import pandas as pd

def open_database_window():

    top_mainwindow=Toplevel()
    blank_space = " "
    top_mainwindow.title('Material Database')
    width_of_window=1920
    height_of_window=1080
    screen_width=top_mainwindow.winfo_screenwidth()
    screen_height=top_mainwindow.winfo_screenheight()
    x_coordinate= (screen_width/2)-(width_of_window/2)
    y_coordinate= (screen_height/2)-(height_of_window/2)
    top_mainwindow.geometry("%dx%d+%d+%d" %  (width_of_window,height_of_window,x_coordinate,y_coordinate))

    #ratio=1

    #w, h = top_mainwindow.winfo_screenwidth(), top_mainwindow.winfo_screenheight()
    #top_mainwindow.geometry("%dx%d+0+0" % (ratio*w, ratio*h))
    top_mainwindow.state("zoomed")

    top_mainwindow.resizable(0,0)
    #top_mainwindow.attributes('-fullscreen', True)

#=================================================================================================================== 

    conn=sqlite3.connect("materialdatabase.db")
    cur = conn.cursor()

    cur.execute(""" CREATE TABLE if not exists Material_Database (

    ID                   integer PRIMARY KEY ASC UNIQUE,
    Material             text   ,
    CRITERIA_1           integer,       
    CRITERIA_2           integer,
    CRITERIA_3           integer,
    CRITERIA_4           integer,
    CRITERIA_5           integer,
    CRITERIA_6           integer,
    CRITERIA_7           integer,
    CRITERIA_8           integer,
    CRITERIA_9           integer,
    CRITERIA_10          integer,
    CRITERIA_11          integer,
    CRITERIA_12          integer,
    CRITERIA_13          integer,
    CRITERIA_14          integer,
    CRITERIA_15          integer,
    CRITERIA_16          integer,
    CRITERIA_17          integer,
    CRITERIA_18          integer,
    CRITERIA_19          integer,        
    CRITERIA_20          integer
    )
    """)

    conn.commit()
   
#=================================================================================================================== 
    heightdatabase=800
    Widthdatabase=1225

    database_x=0.5 #move
    database_y=0.5
    databasefromtop=0.1

    maindatabase_frame = Frame(top_mainwindow,
    height=height_of_window,
    width=width_of_window)
    maindatabase_frame.pack() 
    maindatabase_frame.place(
    relx=0.5,
    rely=0.5,
    anchor=CENTER,) 

    database_frame = Frame(maindatabase_frame,
    height=heightdatabase-135,
    width=47*20+25+140)
    database_frame.pack() 
    database_frame.place(
    relx=database_x-0.10,
    rely=0.5,
    anchor=CENTER) 

    database_input_frame = Frame(maindatabase_frame,
    height=heightdatabase,
    width=380)
    database_input_frame.pack() 
    database_input_frame.place(
    relx=0.5+0.3,
    rely=0.52,
    anchor=CENTER) 

    #database_button_frame = Frame(maindatabase_frame,
    #height=40,
    #width=Widthdatabase)
    #database_button_frame.pack() 
    #database_button_frame.place(
    #relx=database_x-0.15,
    #rely=0.1,
    #anchor=CENTER) 

    #btnupdate = Button(database_button_frame, text='Update', height=1, width=10)
    #btnadd = Button(database_button_frame, text='Add', height=1, width=10)
    #btnremove = Button(database_button_frame, text='Remove', height=1, width=10) 

    #ttkcolumn=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)     
    ttkcolumn=(
    "ID",  
    "Material",  
    "CRITERIA_1",  
    "CRITERIA_2",  
    "CRITERIA_3",  
    "CRITERIA_4",  
    "CRITERIA_5",  
    "CRITERIA_6",  
    "CRITERIA_7",  
    "CRITERIA_8",  
    "CRITERIA_9",  
    "CRITERIA_10",  
    "CRITERIA_11",  
    "CRITERIA_12",  
    "CRITERIA_13",  
    "CRITERIA_14",  
    "CRITERIA_15",  
    "CRITERIA_16",  
    "CRITERIA_17",  
    "CRITERIA_18",  
    "CRITERIA_19",  
    "CRITERIA_20")   
    criteria_width=47

    trv=ttk.Treeview(database_frame, columns=ttkcolumn,show="headings",height=heightdatabase)
    trv.pack()

    trv.column("ID", width=  25            ,stretch=NO)
    trv.column("Material", width=  135           ,stretch=NO)
    trv.column("CRITERIA_1", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_2", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_3", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_4", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_5", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_6", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_7", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_8", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_9", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_10", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_11", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_12", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_13", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_14", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_15", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_16", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_17", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_18", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_19", width=  criteria_width,stretch=NO, anchor=tk.CENTER)
    trv.column("CRITERIA_20", width=  criteria_width,stretch=NO, anchor=tk.CENTER) 

    trv.heading("ID",text="ID")
    trv.heading("Material",text="Material Name")
    trv.heading("CRITERIA_1",text="1")
    trv.heading("CRITERIA_2",text="2")
    trv.heading("CRITERIA_3",text="3")
    trv.heading("CRITERIA_4",text="4")
    trv.heading("CRITERIA_5",text="5")
    trv.heading("CRITERIA_6",text="6")
    trv.heading("CRITERIA_7",text="7")
    trv.heading("CRITERIA_8",text="8")
    trv.heading("CRITERIA_9",text="9")
    trv.heading("CRITERIA_10",text="10")
    trv.heading("CRITERIA_11",text="11")
    trv.heading("CRITERIA_12",text="12")
    trv.heading("CRITERIA_13",text="13")
    trv.heading("CRITERIA_14",text="14")
    trv.heading("CRITERIA_15",text="15")
    trv.heading("CRITERIA_16",text="16")
    trv.heading("CRITERIA_17",text="17")
    trv.heading("CRITERIA_18",text="18")
    trv.heading("CRITERIA_19",text="19")
    trv.heading("CRITERIA_20",text="20")     
    trv.place(x=0,y=0)


    cur.execute("SELECT * FROM Material_Database")

    data=cur.fetchall()
    for row in data:
        trv.insert(parent='', index=END, iid=row, text='', values=row)


    def deletefromdatabase():  

        conn=sqlite3.connect("materialdatabase.db")
        cur = conn.cursor()

        cur.execute("SELECT ID FROM Material_Database")
        ID=cur.fetchall()            

        selected_item = trv.selection()[0] ## get selected item 
        selected_item_number=selected_item[0]   

        cur.execute("DELETE from Material_Database WHERE ID=" + selected_item_number)                
        trv.delete(selected_item) #delete from Treeview 

        conn.commit()
      
    #gapbtn=0.08
    #btnupdate.pack() 
    #btnupdate.place(relx=0.88+gapbtn*0,rely=0.5, anchor=CENTER)  
    #btnremove.pack()  
    #btnremove.place(relx=0.88+gapbtn*1,rely=0.5, anchor=CENTER)           
    #btnremove.configure(command=deletefromdatabase)


    scrollbarY_MDbox = Scrollbar(database_frame , orient=VERTICAL)        
    scrollbarY_MDbox.pack()
    trv.config(yscrollcommand=scrollbarY_MDbox.set)
    scrollbarY_MDbox.config(command=trv.yview)               

    scrollbarY_MDbox.place(relx=1,rely=0, height=heightdatabase,anchor=NE)

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")    

#=================================================================================================================== 

    input_material_name   =Label(database_input_frame, text="Material Name", font=("Helvetica", 9, 'bold' ))
    input_material_C1     =Label(database_input_frame, text="Criteria 1   ") 
    input_material_C2     =Label(database_input_frame, text="Criteria 2   ")
    input_material_C3     =Label(database_input_frame, text="Criteria 3   ")
    input_material_C4     =Label(database_input_frame, text="Criteria 4   ")
    input_material_C5     =Label(database_input_frame, text="Criteria 5   ")
    input_material_C6     =Label(database_input_frame, text="Criteria 6   ")
    input_material_C7     =Label(database_input_frame, text="Criteria 7   ")
    input_material_C8     =Label(database_input_frame, text="Criteria 8   ")
    input_material_C9     =Label(database_input_frame, text="Criteria 9   ")
    input_material_C10    =Label(database_input_frame, text="Criteria 10  ")
    input_material_C11    =Label(database_input_frame, text="Criteria 11  ") 
    input_material_C12    =Label(database_input_frame, text="Criteria 12  ")
    input_material_C13    =Label(database_input_frame, text="Criteria 13  ")
    input_material_C14    =Label(database_input_frame, text="Criteria 14  ")
    input_material_C15    =Label(database_input_frame, text="Criteria 15  ")
    input_material_C16    =Label(database_input_frame, text="Criteria 16  ")
    input_material_C17    =Label(database_input_frame, text="Criteria 17  ")
    input_material_C18    =Label(database_input_frame, text="Criteria 18  ")
    input_material_C19    =Label(database_input_frame, text="Criteria 19  ")
    input_material_C20    =Label(database_input_frame, text="Criteria 20  ")

    input_y_from_top=0.05
    gap_input_y=0.04

    gap_input_x=0.6

    values_OorSub=['Quantitative','Qualitative']
    width_Combobox_Oorsub=12

    combobox_f_C1    = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C2    = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C3    = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C4    = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C5    = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C6    = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C7    = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C8    = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C9    = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C10   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C11   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C12   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C13   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C14   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C15   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C16   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C17   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C18   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C19   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly') 
    combobox_f_C20   = ttk.Combobox(database_input_frame,values=values_OorSub, width= width_Combobox_Oorsub, state='readonly')  

    combobox_f_C1 .set('')
    combobox_f_C2 .set('')
    combobox_f_C3 .set('')
    combobox_f_C4 .set('')
    combobox_f_C5 .set('')
    combobox_f_C6 .set('')
    combobox_f_C7 .set('')
    combobox_f_C8 .set('')
    combobox_f_C9 .set('')
    combobox_f_C10.set('')
    combobox_f_C11.set('')
    combobox_f_C12.set('')
    combobox_f_C13.set('')
    combobox_f_C14.set('')
    combobox_f_C15.set('')
    combobox_f_C16.set('')
    combobox_f_C17.set('')
    combobox_f_C18.set('')
    combobox_f_C19.set('')
    combobox_f_C20.set('')

    combobox_f_C1 .pack()
    combobox_f_C2 .pack()
    combobox_f_C3 .pack()
    combobox_f_C4 .pack()
    combobox_f_C5 .pack()
    combobox_f_C6 .pack()
    combobox_f_C7 .pack()
    combobox_f_C8 .pack()
    combobox_f_C9 .pack()
    combobox_f_C10.pack()
    combobox_f_C11.pack()
    combobox_f_C12.pack()
    combobox_f_C13.pack()
    combobox_f_C14.pack()
    combobox_f_C15.pack()
    combobox_f_C16.pack()
    combobox_f_C17.pack()
    combobox_f_C18.pack()
    combobox_f_C19.pack()
    combobox_f_C20.pack()

    f_gap=0.3
    f_gap_b=0.2

    combobox_f_C1     .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*1      ,anchor=W          )        
    combobox_f_C2     .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*2      ,anchor=W          )         
    combobox_f_C3     .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*3      ,anchor=W          )         
    combobox_f_C4     .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*4      ,anchor=W          )         
    combobox_f_C5     .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*5      ,anchor=W          )         
    combobox_f_C6     .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*6      ,anchor=W          )         
    combobox_f_C7     .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*7      ,anchor=W          )          
    combobox_f_C8     .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*8      ,anchor=W          )          
    combobox_f_C9     .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*9      ,anchor=W          )          
    combobox_f_C10    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*10     ,anchor=W          )        
    combobox_f_C11    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*11     ,anchor=W          )        
    combobox_f_C12    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*12     ,anchor=W          )        
    combobox_f_C13    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*13     ,anchor=W          )        
    combobox_f_C14    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*14     ,anchor=W          )        
    combobox_f_C15    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*15     ,anchor=W          )        
    combobox_f_C16    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*16     ,anchor=W          )        
    combobox_f_C17    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*17     ,anchor=W          )        
    combobox_f_C18    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*18     ,anchor=W          )        
    combobox_f_C19    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*19     ,anchor=W          )        
    combobox_f_C20    .place(relx=0.025+f_gap   ,  rely=input_y_from_top+gap_input_y*20     ,anchor=W          )


    Entry_material_C1        =Entry(database_input_frame)
    Entry_material_C2        =Entry(database_input_frame)
    Entry_material_C3        =Entry(database_input_frame)
    Entry_material_C4        =Entry(database_input_frame)
    Entry_material_C5        =Entry(database_input_frame)
    Entry_material_C6        =Entry(database_input_frame)
    Entry_material_C7        =Entry(database_input_frame)
    Entry_material_C8        =Entry(database_input_frame)
    Entry_material_C9        =Entry(database_input_frame)
    Entry_material_C10       =Entry(database_input_frame)
    Entry_material_C11       =Entry(database_input_frame)
    Entry_material_C12       =Entry(database_input_frame)
    Entry_material_C13       =Entry(database_input_frame)
    Entry_material_C14       =Entry(database_input_frame)
    Entry_material_C15       =Entry(database_input_frame)
    Entry_material_C16       =Entry(database_input_frame)
    Entry_material_C17       =Entry(database_input_frame)
    Entry_material_C18       =Entry(database_input_frame)
    Entry_material_C19       =Entry(database_input_frame)
    Entry_material_C20       =Entry(database_input_frame)

    fuzzy_criteria_rating_dict={        
    '    '                   :'',
    'Extremely low (EL)     ':'EL',
    'Very low (VL)          ':'VL',
    'Low (L)                ':'L',
    'Medium low (ML)        ':'ML',
    'Medium (M)             ':'M',
    'Medium high (MH)       ':'MH',
    'High (H)               ':'H',
    'Very high (VH)         ':'VH',
    'Extremely high (EH)    ':'EH'
    } 

    var_fuzzy1 = tk.StringVar()
    var_fuzzy2 = tk.StringVar()
    var_fuzzy3 = tk.StringVar()
    var_fuzzy4 = tk.StringVar()
    var_fuzzy5 = tk.StringVar()
    var_fuzzy6 = tk.StringVar()
    var_fuzzy7 = tk.StringVar()
    var_fuzzy8 = tk.StringVar()
    var_fuzzy9 = tk.StringVar()
    var_fuzzy10 = tk.StringVar()
    var_fuzzy11 = tk.StringVar()
    var_fuzzy12 = tk.StringVar()
    var_fuzzy13 = tk.StringVar()
    var_fuzzy14 = tk.StringVar()
    var_fuzzy15 = tk.StringVar()
    var_fuzzy16 = tk.StringVar()
    var_fuzzy17 = tk.StringVar()
    var_fuzzy18 = tk.StringVar()
    var_fuzzy19 = tk.StringVar()
    var_fuzzy20 = tk.StringVar()  

    width_entryCombobox=20

    Entry_material_C1_combobox  = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy1)
    Entry_material_C2_combobox  = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy2)
    Entry_material_C3_combobox  = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy3)
    Entry_material_C4_combobox  = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy4)
    Entry_material_C5_combobox  = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy5)
    Entry_material_C6_combobox  = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy6)
    Entry_material_C7_combobox  = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy7)
    Entry_material_C8_combobox  = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy8)
    Entry_material_C9_combobox  = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy9)
    Entry_material_C10_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy10)
    Entry_material_C11_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy11)
    Entry_material_C12_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy12)
    Entry_material_C13_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy13)
    Entry_material_C14_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy14)
    Entry_material_C15_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy15)
    Entry_material_C16_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy16)
    Entry_material_C17_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy17)
    Entry_material_C18_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy18)
    Entry_material_C19_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy19)
    Entry_material_C20_combobox = ttk.Combobox(database_input_frame, values=list(fuzzy_criteria_rating_dict.keys()), width= width_entryCombobox,  textvariable=var_fuzzy20)


    Entry_material_C1_combobox.current(0) 
    Entry_material_C1_combobox.current(0)   
    Entry_material_C2_combobox.current(0)   
    Entry_material_C3_combobox.current(0)   
    Entry_material_C4_combobox.current(0)   
    Entry_material_C5_combobox.current(0)   
    Entry_material_C6_combobox.current(0)   
    Entry_material_C7_combobox.current(0)   
    Entry_material_C8_combobox.current(0)   
    Entry_material_C9_combobox.current(0)   
    Entry_material_C10_combobox.current(0)    
    Entry_material_C11_combobox.current(0)    
    Entry_material_C12_combobox.current(0)    
    Entry_material_C13_combobox.current(0)    
    Entry_material_C14_combobox.current(0)    
    Entry_material_C15_combobox.current(0)    
    Entry_material_C16_combobox.current(0)    
    Entry_material_C17_combobox.current(0)    
    Entry_material_C18_combobox.current(0)    
    Entry_material_C19_combobox.current(0)    
    Entry_material_C20_combobox.current(0)    

    def forget_widget_entry_1  (): 
        Entry_material_C1          .place_forget()  
        Entry_material_C1_combobox .place_forget()

    def forget_widget_entry_2  (): 
        Entry_material_C2          .place_forget()
        Entry_material_C2_combobox .place_forget()

    def forget_widget_entry_3  (): 
        Entry_material_C3          .place_forget()
        Entry_material_C3_combobox .place_forget()

    def forget_widget_entry_4  (): 
        Entry_material_C4          .place_forget()
        Entry_material_C4_combobox .place_forget()

    def forget_widget_entry_5  (): 
        Entry_material_C5          .place_forget()
        Entry_material_C5_combobox .place_forget()

    def forget_widget_entry_6  (): 
        Entry_material_C6          .place_forget()
        Entry_material_C6_combobox .place_forget()

    def forget_widget_entry_7  (): 
        Entry_material_C7          .place_forget()
        Entry_material_C7_combobox .place_forget()

    def forget_widget_entry_8  (): 
        Entry_material_C8          .place_forget()
        Entry_material_C8_combobox .place_forget()

    def forget_widget_entry_9  (): 
        Entry_material_C9          .place_forget()
        Entry_material_C9_combobox .place_forget()

    def forget_widget_entry_10 (): 
        Entry_material_C10         .place_forget()
        Entry_material_C10_combobox .place_forget()

    def forget_widget_entry_11 (): 
        Entry_material_C11         .place_forget()
        Entry_material_C11_combobox .place_forget()

    def forget_widget_entry_12 (): 
        Entry_material_C12         .place_forget()
        Entry_material_C12_combobox .place_forget()

    def forget_widget_entry_13 (): 
        Entry_material_C13         .place_forget()
        Entry_material_C13_combobox .place_forget()

    def forget_widget_entry_14 (): 
        Entry_material_C14         .place_forget()
        Entry_material_C14_combobox .place_forget()

    def forget_widget_entry_15 (): 
        Entry_material_C15         .place_forget()
        Entry_material_C15_combobox .place_forget()

    def forget_widget_entry_16 (): 
        Entry_material_C16         .place_forget()
        Entry_material_C16_combobox .place_forget()

    def forget_widget_entry_17 (): 
        Entry_material_C17         .place_forget()
        Entry_material_C17_combobox .place_forget()

    def forget_widget_entry_18 (): 
        Entry_material_C18         .place_forget()
        Entry_material_C18_combobox .place_forget()

    def forget_widget_entry_19 (): 
        Entry_material_C19         .place_forget()
        Entry_material_C19_combobox .place_forget()

    def forget_widget_entry_20 (): 
        Entry_material_C20         .place_forget()
        Entry_material_C20_combobox .place_forget() 


    def set_widget_input_1 (event): 
        if combobox_f_C1 .get()=='Quantitative':
            forget_widget_entry_1 ()                
            Entry_material_C1 .pack()
            Entry_material_C1 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*1 , anchor=W)
        if combobox_f_C1 .get()=='Qualitative':   
            forget_widget_entry_1 () 
            Entry_material_C1_combobox   .pack()
            Entry_material_C1_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*1 , anchor=W)      
    def set_widget_input_2 (event): 
        if combobox_f_C2 .get()=='Quantitative':
            forget_widget_entry_2 ()                
            Entry_material_C2 .pack()
            Entry_material_C2 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*2 , anchor=W)
        if combobox_f_C2 .get()=='Qualitative':   
            forget_widget_entry_2 () 
            Entry_material_C2_combobox   .pack()
            Entry_material_C2_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*2 , anchor=W)    
    def set_widget_input_3 (event): 
        if combobox_f_C3 .get()=='Quantitative':
            forget_widget_entry_3 ()                
            Entry_material_C3 .pack()
            Entry_material_C3 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*3 , anchor=W)
        if combobox_f_C3 .get()=='Qualitative':   
            forget_widget_entry_3 () 
            Entry_material_C3_combobox   .pack()
            Entry_material_C3_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*3 , anchor=W)
    def set_widget_input_4 (event): 
        if combobox_f_C4 .get()=='Quantitative':
            forget_widget_entry_4 ()                
            Entry_material_C4 .pack()
            Entry_material_C4 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*4 , anchor=W)
        if combobox_f_C4 .get()=='Qualitative':   
            forget_widget_entry_4 () 
            Entry_material_C4_combobox   .pack()
            Entry_material_C4_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*4 , anchor=W)
    def set_widget_input_5 (event): 
        if combobox_f_C5 .get()=='Quantitative':
            forget_widget_entry_5 ()                
            Entry_material_C5 .pack()
            Entry_material_C5 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*5 , anchor=W)
        if combobox_f_C5 .get()=='Qualitative':   
            forget_widget_entry_5 () 
            Entry_material_C5_combobox   .pack()
            Entry_material_C5_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*5 , anchor=W)
    def set_widget_input_6 (event): 
        if combobox_f_C6 .get()=='Quantitative':
            forget_widget_entry_6 ()                
            Entry_material_C6 .pack()
            Entry_material_C6 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*6 , anchor=W)
        if combobox_f_C6 .get()=='Qualitative':   
            forget_widget_entry_6 () 
            Entry_material_C6_combobox   .pack()
            Entry_material_C6_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*6 , anchor=W)
    def set_widget_input_7 (event): 
        if combobox_f_C7 .get()=='Quantitative':
            forget_widget_entry_7 ()                
            Entry_material_C7 .pack()
            Entry_material_C7 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*7 , anchor=W)
        if combobox_f_C7 .get()=='Qualitative':   
            forget_widget_entry_7 () 
            Entry_material_C7_combobox   .pack()
            Entry_material_C7_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*7 , anchor=W)
    def set_widget_input_8 (event): 
        if combobox_f_C8 .get()=='Quantitative':
            forget_widget_entry_8 ()                
            Entry_material_C8 .pack()
            Entry_material_C8 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*8 , anchor=W)
        if combobox_f_C8 .get()=='Qualitative':   
            forget_widget_entry_8 () 
            Entry_material_C8_combobox   .pack()
            Entry_material_C8_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*8 , anchor=W)
    def set_widget_input_9 (event): 
        if combobox_f_C9 .get()=='Quantitative':
            forget_widget_entry_9 ()                
            Entry_material_C9 .pack()
            Entry_material_C9 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*9 , anchor=W)
        if combobox_f_C9 .get()=='Qualitative':   
            forget_widget_entry_9 () 
            Entry_material_C9_combobox   .pack()
            Entry_material_C9_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*9 , anchor=W)
    def set_widget_input_10 (event): 
        if combobox_f_C10 .get()=='Quantitative':
            forget_widget_entry_10()                
            Entry_material_C10 .pack()
            Entry_material_C10 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*10 , anchor=W)
        if combobox_f_C10 .get()=='Qualitative':   
            forget_widget_entry_10() 
            Entry_material_C10_combobox   .pack()
            Entry_material_C10_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*10 , anchor=W)
    def set_widget_input_11 (event): 
        if combobox_f_C11 .get()=='Quantitative':
            forget_widget_entry_11()                
            Entry_material_C11 .pack()
            Entry_material_C11 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*11 , anchor=W)
        if combobox_f_C11 .get()=='Qualitative':   
            forget_widget_entry_11() 
            Entry_material_C11_combobox   .pack()
            Entry_material_C11_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*11 , anchor=W)
    def set_widget_input_12 (event): 
        if combobox_f_C12 .get()=='Quantitative':
            forget_widget_entry_12()                
            Entry_material_C12 .pack()
            Entry_material_C12 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*12 , anchor=W)
        if combobox_f_C12 .get()=='Qualitative':   
            forget_widget_entry_12() 
            Entry_material_C12_combobox   .pack()
            Entry_material_C12_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*12 , anchor=W) 
    def set_widget_input_13 (event): 
        if combobox_f_C13 .get()=='Quantitative':
            forget_widget_entry_13()                
            Entry_material_C13 .pack()
            Entry_material_C13 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*13 , anchor=W)
        if combobox_f_C13 .get()=='Qualitative':   
            forget_widget_entry_13() 
            Entry_material_C13_combobox   .pack()
            Entry_material_C13_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*13 , anchor=W)
    def set_widget_input_14 (event): 
        if combobox_f_C14 .get()=='Quantitative':
            forget_widget_entry_14()                
            Entry_material_C14 .pack()
            Entry_material_C14 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*14 , anchor=W)
        if combobox_f_C14 .get()=='Qualitative':   
            forget_widget_entry_14() 
            Entry_material_C14_combobox   .pack()
            Entry_material_C14_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*14 , anchor=W)
    def set_widget_input_15 (event): 
        if combobox_f_C15 .get()=='Quantitative':
            forget_widget_entry_15()                
            Entry_material_C15 .pack()
            Entry_material_C15 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*15 , anchor=W)
        if combobox_f_C15 .get()=='Qualitative':   
            forget_widget_entry_15() 
            Entry_material_C15_combobox   .pack()
            Entry_material_C15_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*15 , anchor=W)
    def set_widget_input_16 (event): 
        if combobox_f_C16 .get()=='Quantitative':
            forget_widget_entry_16()                
            Entry_material_C16 .pack()
            Entry_material_C16 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*16 , anchor=W)
        if combobox_f_C16 .get()=='Qualitative':   
            forget_widget_entry_16() 
            Entry_material_C16_combobox   .pack()
            Entry_material_C16_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*16 , anchor=W)
    def set_widget_input_17 (event): 
        if combobox_f_C17 .get()=='Quantitative':
            forget_widget_entry_17()                
            Entry_material_C17 .pack()
            Entry_material_C17 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*17 , anchor=W)
        if combobox_f_C17 .get()=='Qualitative':   
            forget_widget_entry_17() 
            Entry_material_C17_combobox   .pack()
            Entry_material_C17_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*17 , anchor=W)
    def set_widget_input_18 (event): 
        if combobox_f_C18 .get()=='Quantitative':
            forget_widget_entry_18()                
            Entry_material_C18 .pack()
            Entry_material_C18 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*18 , anchor=W)
        if combobox_f_C18 .get()=='Qualitative':   
            forget_widget_entry_18() 
            Entry_material_C18_combobox   .pack()
            Entry_material_C18_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*18 , anchor=W)
    def set_widget_input_19 (event): 
        if combobox_f_C19 .get()=='Quantitative':
            forget_widget_entry_19()                
            Entry_material_C19 .pack()
            Entry_material_C19 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*19 , anchor=W)
        if combobox_f_C19 .get()=='Qualitative':   
            forget_widget_entry_19() 
            Entry_material_C19_combobox   .pack()
            Entry_material_C19_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*19 , anchor=W)
    def set_widget_input_20 (event): 
        if combobox_f_C20 .get()=='Quantitative':
            forget_widget_entry_20()                
            Entry_material_C20 .pack()
            Entry_material_C20 .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*20 , anchor=W)
        if combobox_f_C20 .get()=='Qualitative':   
            forget_widget_entry_20() 
            Entry_material_C20_combobox   .pack()
            Entry_material_C20_combobox .place(relx=0.025+gap_input_x,rely=input_y_from_top+gap_input_y*20 , anchor=W)

    combobox_f_C1     .bind ("<<ComboboxSelected>>", set_widget_input_1 )
    combobox_f_C2     .bind ("<<ComboboxSelected>>", set_widget_input_2 )
    combobox_f_C3     .bind ("<<ComboboxSelected>>", set_widget_input_3 )
    combobox_f_C4     .bind ("<<ComboboxSelected>>", set_widget_input_4 )
    combobox_f_C5     .bind ("<<ComboboxSelected>>", set_widget_input_5 )
    combobox_f_C6     .bind ("<<ComboboxSelected>>", set_widget_input_6 )
    combobox_f_C7     .bind ("<<ComboboxSelected>>", set_widget_input_7 )
    combobox_f_C8     .bind ("<<ComboboxSelected>>", set_widget_input_8 )
    combobox_f_C9     .bind ("<<ComboboxSelected>>", set_widget_input_9 )
    combobox_f_C10    .bind ("<<ComboboxSelected>>", set_widget_input_10)
    combobox_f_C11    .bind ("<<ComboboxSelected>>", set_widget_input_11)
    combobox_f_C12    .bind ("<<ComboboxSelected>>", set_widget_input_12)
    combobox_f_C13    .bind ("<<ComboboxSelected>>", set_widget_input_13)
    combobox_f_C14    .bind ("<<ComboboxSelected>>", set_widget_input_14)
    combobox_f_C15    .bind ("<<ComboboxSelected>>", set_widget_input_15)
    combobox_f_C16    .bind ("<<ComboboxSelected>>", set_widget_input_16)
    combobox_f_C17    .bind ("<<ComboboxSelected>>", set_widget_input_17)
    combobox_f_C18    .bind ("<<ComboboxSelected>>", set_widget_input_18)
    combobox_f_C19    .bind ("<<ComboboxSelected>>", set_widget_input_19)
    combobox_f_C20    .bind ("<<ComboboxSelected>>", set_widget_input_20)


    Entry_material_name     =Entry(database_input_frame) 
    Entry_material_name .pack()
    Entry_material_name.place(relx=0.025+f_gap,rely=input_y_from_top-0.005,width=220, anchor=W)


    input_material_name.place(relx=0.025,rely=input_y_from_top-0.005,          anchor=W)
    input_material_C1.  place(relx=0.025,rely=input_y_from_top+gap_input_y*1,  anchor=W) 
    input_material_C2.  place(relx=0.025,rely=input_y_from_top+gap_input_y*2,  anchor=W) 
    input_material_C3.  place(relx=0.025,rely=input_y_from_top+gap_input_y*3,  anchor=W) 
    input_material_C4.  place(relx=0.025,rely=input_y_from_top+gap_input_y*4,  anchor=W) 
    input_material_C5.  place(relx=0.025,rely=input_y_from_top+gap_input_y*5,  anchor=W) 
    input_material_C6.  place(relx=0.025,rely=input_y_from_top+gap_input_y*6,  anchor=W) 
    input_material_C7.  place(relx=0.025,rely=input_y_from_top+gap_input_y*7,  anchor=W) 
    input_material_C8.  place(relx=0.025,rely=input_y_from_top+gap_input_y*8,  anchor=W) 
    input_material_C9.  place(relx=0.025,rely=input_y_from_top+gap_input_y*9,  anchor=W) 
    input_material_C10. place(relx=0.025,rely=input_y_from_top+gap_input_y*10, anchor=W) 
    input_material_C11. place(relx=0.025,rely=input_y_from_top+gap_input_y*11, anchor=W) 
    input_material_C12. place(relx=0.025,rely=input_y_from_top+gap_input_y*12, anchor=W) 
    input_material_C13. place(relx=0.025,rely=input_y_from_top+gap_input_y*13, anchor=W) 
    input_material_C14. place(relx=0.025,rely=input_y_from_top+gap_input_y*14, anchor=W) 
    input_material_C15. place(relx=0.025,rely=input_y_from_top+gap_input_y*15, anchor=W) 
    input_material_C16. place(relx=0.025,rely=input_y_from_top+gap_input_y*16, anchor=W) 
    input_material_C17. place(relx=0.025,rely=input_y_from_top+gap_input_y*17, anchor=W) 
    input_material_C18. place(relx=0.025,rely=input_y_from_top+gap_input_y*18, anchor=W) 
    input_material_C19. place(relx=0.025,rely=input_y_from_top+gap_input_y*19, anchor=W) 
    input_material_C20. place(relx=0.025,rely=input_y_from_top+gap_input_y*20, anchor=W) 



    def addintodatabase():      

        values_C1 =0
        values_C2 =0
        values_C3 =0
        values_C4 =0
        values_C5 =0
        values_C6 =0
        values_C7 =0
        values_C8 =0
        values_C9 =0
        values_C10=0
        values_C11=0
        values_C12=0
        values_C13=0
        values_C14=0
        values_C15=0
        values_C16=0
        values_C17=0
        values_C18=0
        values_C19=0
        values_C20=0

        values_material_name = Entry_material_name .get() 
    
        if combobox_f_C1 .get()=='Quantitative':
            values_C1 = Entry_material_C1 .get()
        if combobox_f_C1 .get()=='Qualitative':         
            values_C1= fuzzy_criteria_rating_dict[var_fuzzy1.get()]
        if combobox_f_C2 .get()=='Quantitative':
            values_C2 = Entry_material_C2 .get()
        if combobox_f_C2 .get()=='Qualitative':   
            values_C2 = fuzzy_criteria_rating_dict[var_fuzzy2.get()]
        if combobox_f_C3 .get()=='Quantitative':
            values_C3 = Entry_material_C3 .get()
        if combobox_f_C3 .get()=='Qualitative':   
            values_C3 = fuzzy_criteria_rating_dict[var_fuzzy3.get()]       
        if combobox_f_C4 .get()=='Quantitative':
            values_C4 = Entry_material_C4 .get()
        if combobox_f_C4 .get()=='Qualitative':   
            values_C4 = fuzzy_criteria_rating_dict[var_fuzzy4.get()]       
        if combobox_f_C5 .get()=='Quantitative':
            values_C5 = Entry_material_C5 .get()
        if combobox_f_C5 .get()=='Qualitative':   
            values_C5 = fuzzy_criteria_rating_dict[var_fuzzy5.get()]       
        if combobox_f_C6 .get()=='Quantitative':
            values_C6 = Entry_material_C6 .get()
        if combobox_f_C6 .get()=='Qualitative':   
            values_C6 = fuzzy_criteria_rating_dict[var_fuzzy6.get()]       
        if combobox_f_C7 .get()=='Quantitative':
            values_C7 = Entry_material_C7 .get()
        if combobox_f_C7 .get()=='Qualitative':   
            values_C7 = fuzzy_criteria_rating_dict[var_fuzzy7.get()]       
        if combobox_f_C8 .get()=='Quantitative':
            values_C8 = Entry_material_C8 .get()
        if combobox_f_C8 .get()=='Qualitative':   
            values_C8 = fuzzy_criteria_rating_dict[var_fuzzy8.get()]       
        if combobox_f_C9 .get()=='Quantitative':
            values_C9 = Entry_material_C9 .get()
        if combobox_f_C9 .get()=='Qualitative':   
            values_C9 = fuzzy_criteria_rating_dict[var_fuzzy9.get()]        
        if combobox_f_C10 .get()=='Quantitative':
            values_C10= Entry_material_C10 .get()
        if combobox_f_C10 .get()=='Qualitative':   
            values_C10=  fuzzy_criteria_rating_dict[var_fuzzy10.get()]         
        if combobox_f_C11 .get()=='Quantitative':
            values_C11= Entry_material_C11 .get()
        if combobox_f_C11 .get()=='Qualitative':   
            values_C11=  fuzzy_criteria_rating_dict[var_fuzzy11.get()]         
        if combobox_f_C12 .get()=='Quantitative':
            values_C12= Entry_material_C12 .get()
        if combobox_f_C12 .get()=='Qualitative':   
            values_C12=  fuzzy_criteria_rating_dict[var_fuzzy12.get()]         
        if combobox_f_C13 .get()=='Quantitative':
            values_C13= Entry_material_C13 .get()
        if combobox_f_C13 .get()=='Qualitative':   
            values_C13=  fuzzy_criteria_rating_dict[var_fuzzy13.get()]         
        if combobox_f_C14 .get()=='Quantitative':
            values_C14= Entry_material_C14 .get()
        if combobox_f_C14 .get()=='Qualitative':   
            values_C14=  fuzzy_criteria_rating_dict[var_fuzzy14.get()]         
        if combobox_f_C15 .get()=='Quantitative':
            values_C15= Entry_material_C15 .get()
        if combobox_f_C15 .get()=='Qualitative':   
            values_C15=  fuzzy_criteria_rating_dict[var_fuzzy15.get()]         
        if combobox_f_C16 .get()=='Quantitative':
            values_C16= Entry_material_C16 .get()
        if combobox_f_C16 .get()=='Qualitative':   
            values_C16=  fuzzy_criteria_rating_dict[var_fuzzy16.get()]         
        if combobox_f_C17 .get()=='Quantitative':
            values_C17= Entry_material_C17 .get()
        if combobox_f_C17 .get()=='Qualitative':   
            values_C17=  fuzzy_criteria_rating_dict[var_fuzzy17.get()]         
        if combobox_f_C18 .get()=='Quantitative':
            values_C18= Entry_material_C18 .get()
        if combobox_f_C18 .get()=='Qualitative':   
            values_C18=  fuzzy_criteria_rating_dict[var_fuzzy18.get()]         
        if combobox_f_C19 .get()=='Quantitative':
            values_C19= Entry_material_C19 .get()
        if combobox_f_C19 .get()=='Qualitative':   
            values_C19=  fuzzy_criteria_rating_dict[var_fuzzy19.get()]         
        if combobox_f_C20 .get()=='Quantitative':
            values_C20= Entry_material_C20 .get()
        if combobox_f_C20 .get()=='Qualitative':   
            values_C20=  fuzzy_criteria_rating_dict[var_fuzzy20.get()]

        #
        conn=sqlite3.connect("materialdatabase.db")
        cur = conn.cursor()

        Material   = values_material_name
        CRITERIA_1 = values_C1  
        CRITERIA_2 = values_C2 
        CRITERIA_3 = values_C3 
        CRITERIA_4 = values_C4 
        CRITERIA_5 = values_C5 
        CRITERIA_6 = values_C6 
        CRITERIA_7 = values_C7 
        CRITERIA_8 = values_C8 
        CRITERIA_9 = values_C9 
        CRITERIA_10= values_C10
        CRITERIA_11= values_C11
        CRITERIA_12= values_C12
        CRITERIA_13= values_C13
        CRITERIA_14= values_C14
        CRITERIA_15= values_C15
        CRITERIA_16= values_C16
        CRITERIA_17= values_C17
        CRITERIA_18= values_C18
        CRITERIA_19= values_C19
        CRITERIA_20= values_C20

        params=(Material   
        ,CRITERIA_1 
        ,CRITERIA_2 
        ,CRITERIA_3 
        ,CRITERIA_4 
        ,CRITERIA_5 
        ,CRITERIA_6 
        ,CRITERIA_7 
        ,CRITERIA_8 
        ,CRITERIA_9 
        ,CRITERIA_10
        ,CRITERIA_11
        ,CRITERIA_12
        ,CRITERIA_13
        ,CRITERIA_14
        ,CRITERIA_15
        ,CRITERIA_16
        ,CRITERIA_17
        ,CRITERIA_18
        ,CRITERIA_19
        ,CRITERIA_20)

        #cur.execute("INSERT INTO Material_Database VALUES(NULL,:Material,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",params) 
        cur.execute("INSERT INTO Material_Database VALUES (NULL,:Material,:CRITERIA_1 ,:CRITERIA_2 ,:CRITERIA_3 ,:CRITERIA_4 ,:CRITERIA_5 ,:CRITERIA_6 ,:CRITERIA_7 ,:CRITERIA_8 ,:CRITERIA_9 ,:CRITERIA_10,:CRITERIA_11,:CRITERIA_12,:CRITERIA_13,:CRITERIA_14,:CRITERIA_15,:CRITERIA_16,:CRITERIA_17,:CRITERIA_18,:CRITERIA_19,:CRITERIA_20)",params)
        trv.delete(*trv.get_children())
        conn.commit()        
        cur.execute("SELECT * FROM Material_Database")
        rows=cur.fetchall() 

        for row in rows:
            trv.insert(parent='', index=END, iid=row, text='', values=row)
    
        conn.commit()

    btnadd = Button(database_input_frame, text='Add', height=1, width=8)
    btnadd.configure(command=addintodatabase)
    btnadd.pack()
    btnadd.place(relx=0.825,rely=input_y_from_top+gap_input_y*21.5 , anchor=CENTER) 

    btnremove = Button(database_input_frame, text='Remove', height=1, width=8) 
    btnremove.configure(command=deletefromdatabase)
    btnremove.pack()
    btnremove.place(relx=0.6,rely=input_y_from_top+gap_input_y*21.5 , anchor=CENTER)     
