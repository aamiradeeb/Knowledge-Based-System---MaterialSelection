from tkinter import*
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox                                                   #   Messagebox
import numpy as np                                                          #   Array
import matplotlib.pyplot as plt                                             #   Plot Chart
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg             #   Plot Chart
from fpdf import FPDF                                                       #   Print pdf
from pandas import DataFrame                                                #   Matrix
import sqlite3                                                              #   Database
from criteria_DM_fuzzyweight import *                                       #   Support File
from dm_option import *                                                     #   Support File
from rho_tau_coorelation import *                                           #   Rank Coorelation
from materialdatabase_input import*                                         #   Database import file
import datetime as datetime

from TOPSIS import*
from VIKOR import*
from Fuzzy_TOPSIS_dm import*
from Fuzzy_VIKOR_dm import*

#===================================================================================================================

class app:

    def __init__(self,mainwindow):

        self.mainwindow = mainwindow
        blank_space = " "
        self.mainwindow.title('Material Selection KBS')
        width_of_window=1920
        height_of_window=1080
        screen_width=mainwindow.winfo_screenwidth()
        screen_height=mainwindow.winfo_screenheight()
        x_coordinate= (screen_width/2)-(width_of_window/2)
        y_coordinate= (screen_height/2)-(height_of_window/2)         
        self.mainwindow.geometry("%dx%d+%d+%d" %  (width_of_window,height_of_window,x_coordinate,y_coordinate)) 
 
        #w, h = self.mainwindow.winfo_screenwidth(), self.mainwindow.winfo_screenheight()
        #self.mainwindow.geometry("%dx%d+0+0" % (w, h))
        self.mainwindow.state("zoomed")

        self.mainwindow.resizable(0,0)
        #self.mainwindow.attributes('-fullscreen', True)

        self.main_frame_tab1 = Frame(self.mainwindow, 
        height=height_of_window,
        width=width_of_window)
        self.main_frame_tab1.pack() 
        self.main_frame_tab1.place(
        relx=0.5,
        rely=0.5,
        anchor=CENTER) 

        self.wdtitle1=Label(self.main_frame_tab1, text="Material Selection KBS", font=("Helvetica", 16, "bold"))
        self.wdtitle1.pack()
        self.wdtitle1.place(relx=0.5,rely=0.45, anchor=CENTER)

        btnnextX=0.865
        btnnextY=0.83

        self.btnnext1 = Button(self.main_frame_tab1, text='Next', height=1, width=10)
        self.btnnext1.pack()
        self.btnnext1.place(relx=btnnextX,rely=btnnextY, anchor=CENTER)

#===================================================================================================================
        def tab_2():
 
            location_x_tab2=0.03
            location_y2_tab2=0.1

            location_x2_tab2=0.15 # to delete
            location_y2_tab2_gap=0.043 #

            heightbox_tab2=700

            self.main_frame_tab2 = Frame(self.mainwindow, 
            height=height_of_window,
            width=width_of_window)
            self.main_frame_tab2.pack() 
            self.main_frame_tab2.place(
            relx=0.5,
            rely=0.5,
            anchor=CENTER) 

            self.infodetail_frame = LabelFrame(self.main_frame_tab2, 
            text=("Info"),
            font=("Helvetica", 10, "italic"),
            height=heightbox_tab2,
            width=600)
            self.infodetail_frame.pack() 
            self.infodetail_frame.place(
            relx=0.27,
            rely=0.48,
            anchor=CENTER) 

            self.criteriaweighting_frame = LabelFrame(self.main_frame_tab2, 
            text=("Criteria Weighting"),
            font=("Helvetica", 10, "italic"),
            height=heightbox_tab2,
            width=530)
            self.criteriaweighting_frame.pack() 
            self.criteriaweighting_frame.place(
            relx=0.577,
            rely=0.48,
            anchor=CENTER)            

            self.criteria_optimization = LabelFrame(self.main_frame_tab2, 
            text=("Criteria Optimization"),
            font=("Helvetica", 10, "italic"),
            height=heightbox_tab2,
            width=300)
            self.criteria_optimization.pack() 
            self.criteria_optimization.place(
            relx=0.807,
            rely=0.48,
            anchor=CENTER)   

            self.button_database = Button(self.main_frame_tab2, text='Database', width=10)
            self.button_database.configure(command=open_database_window) 
            self.button_database.pack()
            self.button_database.place(relx=btnnextX,rely=0.138, anchor=CENTER)

            self.wdtitle1.place_forget()
            self.btnnext1.place_forget()

            self.nameofproject1=Label(self.infodetail_frame, text="Project name", font=("Helvetica", 10, 'bold'))

            def handle_focus_in(_):
                self.nameofproject2.delete(0, tk.END)
                self.nameofproject2.config(fg='black') 

            def handle_enter(txt):
                print(self.nameofproject2.get())

            self.nameofproject2=Entry(self.infodetail_frame,width=58,bd=1) 

            self.nameofproject2.insert(0,"Enter Project name")

            self.nameofproject2.bind("<FocusIn>", handle_focus_in) 
            self.nameofproject2.bind("<Return>", handle_enter)

            self.typeofproject1=Label(self.infodetail_frame, text="Type of project", font=("Helvetica", 10, 'bold' ))

            Typeofproject_var=IntVar()
            Typeofproject_var.set(3)
            self.r1=Radiobutton(self.infodetail_frame, text="Performance", variable=Typeofproject_var,value=1, tristatevalue=0)
            self.r2=Radiobutton(self.infodetail_frame, text="Cost", variable=Typeofproject_var,value=2, tristatevalue=0)
            self.r3=Radiobutton(self.infodetail_frame, text="Customise", variable=Typeofproject_var,value=3, tristatevalue=0)

            
            self.dm_q1=Label(self.infodetail_frame, text="Decision makers", font=("Helvetica", 10, 'bold' ))
            
            self.dm_selection = ttk.Combobox(self.infodetail_frame, values=[1,2,3,4,5], width = 11, state='readonly')
            self.dm_selection.set(1)

            self.Typeofevaluation=Label(self.infodetail_frame, text="Type of evaluation", font=("Helvetica", 10, 'bold' ))
            Typeofevaluation_Var=IntVar()
            Typeofevaluation_Var.set(3)
            self.r4=Radiobutton(self.infodetail_frame, text="Quantitative", variable=Typeofevaluation_Var,value=1, tristatevalue=0)
            self.r5=Radiobutton(self.infodetail_frame, text="Qualitative", variable=Typeofevaluation_Var,value=2, tristatevalue=0)            
            self.r6=Radiobutton(self.infodetail_frame, text="Combination", variable=Typeofevaluation_Var,value=3, tristatevalue=0)

            self.criteria_label_listbox_info=Label(self.infodetail_frame, text="Criteria", font=("Helvetica", 10, 'bold' )) 

            item_infodetail_xmove=0.053
            item_infodetail_ymove=0.05
            item_infodetail_xmove_gap=0.25
            item_infodetail_ymove_gap=0.07


            self.nameofproject1.pack()
            self.nameofproject1.place(relx=item_infodetail_xmove,rely=item_infodetail_ymove, anchor=NW)

            self.nameofproject2.pack()
            self.nameofproject2.place(relx=item_infodetail_xmove+item_infodetail_xmove_gap*1.2,rely=item_infodetail_ymove, anchor=NW)

            self.typeofproject1.pack()
            self.typeofproject1.place(relx=item_infodetail_xmove,rely=item_infodetail_ymove+item_infodetail_ymove_gap*1, anchor=NW)
             
            self.r1.pack()
            self.r2.pack()
            self.r3.pack() 
            self.r1.place(relx=item_infodetail_xmove+item_infodetail_xmove_gap*1.2,rely=item_infodetail_ymove+item_infodetail_ymove_gap*1, anchor=NW)
            self.r2.place(relx=item_infodetail_xmove+item_infodetail_xmove_gap*2.1,rely=item_infodetail_ymove+item_infodetail_ymove_gap*1, anchor=NW)
            self.r3.place(relx=item_infodetail_xmove+item_infodetail_xmove_gap*2.8,rely=item_infodetail_ymove+item_infodetail_ymove_gap*1, anchor=NW)
            
            self.dm_q1.pack()
            self.dm_q1.place(relx=item_infodetail_xmove,rely=item_infodetail_ymove+item_infodetail_ymove_gap*2, anchor=NW)

            self.dm_selection.pack()
            self.dm_selection.place(relx=item_infodetail_xmove+item_infodetail_xmove_gap*1.2,rely=item_infodetail_ymove+item_infodetail_ymove_gap*2, anchor=NW)
            self.dm_selection.current()

            self.Typeofevaluation.pack()
            self.Typeofevaluation.place(relx=item_infodetail_xmove,rely=item_infodetail_ymove+item_infodetail_ymove_gap*3, anchor=NW)

            self.r4.pack()
            self.r5.pack()
            self.r6.pack()
            self.r4.place(relx=item_infodetail_xmove+item_infodetail_xmove_gap*1.2,rely=item_infodetail_ymove+item_infodetail_ymove_gap*3, anchor=NW)
            self.r5.place(relx=item_infodetail_xmove+item_infodetail_xmove_gap*2.1,rely=item_infodetail_ymove+item_infodetail_ymove_gap*3, anchor=NW)
            self.r6.place(relx=item_infodetail_xmove+item_infodetail_xmove_gap*2.8,rely=item_infodetail_ymove+item_infodetail_ymove_gap*3, anchor=NW)

            self.criteria_label_listbox_info.pack()
            self.criteria_label_listbox_info.place(relx=item_infodetail_xmove,rely=item_infodetail_ymove+item_infodetail_ymove_gap*4, anchor=NW)

            height_listbox=19
            self.C_Listbox=Listbox(self.infodetail_frame,height=height_listbox , width = 28, selectmode=MULTIPLE,exportselection=False)
            self.C_Listbox.insert(1,'Physical Properties')
            self.C_Listbox.insert(2,'Mechanical Properties')
            self.C_Listbox.insert(3,'Chemical Properties')
            self.C_Listbox.insert(4,'Manufacturing Processes')
            self.C_Listbox.insert(5,'Operating Condition')
            self.C_Listbox.insert(6,'Recyclability')
            self.C_Listbox.insert(7,'Cost')                  
            self.C_Listbox.insert(10,'Quality')
            self.C_Listbox.insert(11,'SHE Risk')
            self.C_Listbox.pack()      

        
            def tab_3(): 

                self.main_frame_tab3 = Frame(self.mainwindow, 
                height=height_of_window,
                width=width_of_window)
                self.main_frame_tab3.pack() 
                self.main_frame_tab3.place(
                relx=0.5,
                rely=0.5,
                anchor=CENTER) 

                self.figure_fuzzy_DMs_Weight_frame = LabelFrame(self.main_frame_tab3)
                self.figure_fuzzy_DMs_Weight_frame.pack() 
                self.figure_fuzzy_DMs_Weight_frame.place(
                relx=0.5,
                rely=0.48,
                #rely= 0.35,
                anchor=CENTER) 

                # initialize tab_3

                # name of project

                print('Project Name         :',self.nameofproject2.get())  

                # type of project
                if Typeofproject_var.get() == 1:
                    print('Type of Project      : Performance')
                if Typeofproject_var.get() == 2:
                    print('Type of Project      : Cost')
                if Typeofproject_var.get() == 3:
                    print('Type of Project      : Customise')    

                # number of dm slected
                print('Number of DM         :',self.dm_selection.get())  

                # type of evaluation
                if Typeofevaluation_Var.get() == 1:
                    print('Type of Evaluation   : Quantitative')
                if Typeofevaluation_Var.get() == 2:
                    print('Type of Evaluation   : Qualitative')
                if Typeofevaluation_Var.get() == 3:
                    print('Type of Evaluation   : Combination')
 
                con=sqlite3.connect("materialdatabase.db")
                df=pd.read_sql("SELECT * FROM Material_Database",con)                
                rowdatabase=len(df)
                print('Number of alternative:',rowdatabase) 

                # First group of criteria
                values_SubCriteria_level_1 = [self.C_Listbox.get(idx) for idx in self.C_Listbox.curselection()]
                #print(values_SubCriteria_level_1)
                # Second group of criteria
                values_SubCriteria_level_2 = [self.C_Listbox2.get(idx) for idx in self.C_Listbox2.curselection()]   
                #print(values_SubCriteria_level_2)

                # Number of criteria
                num_val_sublv2 = len(values_SubCriteria_level_2)  
                print('Number of Criteria   :',num_val_sublv2)
                print('                      ',values_SubCriteria_level_2)     
                print("")    
                # Material database 
                print(df)

 
                # # Output Pdf
                #timestamp=StringVar()
                #timestamp=datetime.datetime.now()
                #timename=('_'+timestamp.strftime("%H")+'_'+timestamp.strftime("%d"))
                #filename='Material_Analysis_Report_'
                #typefile='.pdf' 
                #Projectnamefile=self.nameofproject2.get()
                #pdf.output(filename+Projectnamefile+str(timename)+'.pdf')

                #fuzzification
                #fuzzy number 9-Saaty scale

                fz1= (0.001,0.1,0.2) # Extremely Low
                fz2= (0.1,0.2,0.3) # Very Low
                fz3= (0.2,0.3,0.4) # Low
                fz4= (0.3,0.4,0.5) # Medium low
                fz5= (0.4,0.5,0.6) # Medium
                fz6= (0.5,0.6,0.7) # Medium High
                fz7= (0.6,0.7,0.8) # High
                fz8= (0.7,0.8,0.9) # Very High
                fz9= (0.8,0.9,1.0)# Extremely Very High    
                fz10= (0.9,1.0,1.0)
              
                dm_number=self.dm_selection.get()

                dm1_c1_get   = dm1_c1.get()   
                dm1_c2_get   = dm1_c2.get()   
                dm1_c3_get   = dm1_c3.get()   
                dm1_c4_get   = dm1_c4.get()   
                dm1_c5_get   = dm1_c5.get()   
                dm1_c6_get   = dm1_c6.get()  
                dm1_c7_get   = dm1_c7.get()   
                dm1_c8_get   = dm1_c8.get()   
                dm1_c9_get   = dm1_c9.get()   
                dm1_c10_get  = dm1_c10.get()
                dm1_c11_get  = dm1_c11.get() 
                dm1_c12_get  = dm1_c12.get() 
                dm1_c13_get  = dm1_c13.get() 
                dm1_c14_get  = dm1_c14.get()                
                dm1_c15_get  = dm1_c15.get() 
                dm1_c16_get  = dm1_c16.get() 
                dm1_c17_get  = dm1_c17.get() 
                dm1_c18_get  = dm1_c18.get()   
                dm1_c19_get  = dm1_c19.get()   
                dm1_c20_get  = dm1_c20.get()  

                dm2_c1_get   = dm2_c1.get()  
                dm2_c2_get   = dm2_c2.get()  
                dm2_c3_get   = dm2_c3.get()  
                dm2_c4_get   = dm2_c4.get()  
                dm2_c5_get   = dm2_c5.get()  
                dm2_c6_get   = dm2_c6.get()  
                dm2_c7_get   = dm2_c7.get()  
                dm2_c8_get   = dm2_c8.get()  
                dm2_c9_get   = dm2_c9.get()  
                dm2_c10_get  = dm2_c10.get()
                dm2_c11_get  = dm2_c11.get() 
                dm2_c12_get  = dm2_c12.get() 
                dm2_c13_get  = dm2_c13.get() 
                dm2_c14_get  = dm2_c14.get()                
                dm2_c15_get  = dm2_c15.get()  
                dm2_c16_get  = dm2_c16.get() 
                dm2_c17_get  = dm2_c17.get() 
                dm2_c18_get  = dm2_c18.get()   
                dm2_c19_get  = dm2_c19.get()   
                dm2_c20_get  = dm2_c20.get()  

                dm3_c1_get   = dm3_c1.get()  
                dm3_c2_get   = dm3_c2.get()  
                dm3_c3_get   = dm3_c3.get()  
                dm3_c4_get   = dm3_c4.get()  
                dm3_c5_get   = dm3_c5.get()  
                dm3_c6_get   = dm3_c6.get()  
                dm3_c7_get   = dm3_c7.get()  
                dm3_c8_get   = dm3_c8.get()  
                dm3_c9_get   = dm3_c9.get()  
                dm3_c10_get  = dm3_c10.get()
                dm3_c11_get  = dm3_c11.get() 
                dm3_c12_get  = dm3_c12.get() 
                dm3_c13_get  = dm3_c13.get() 
                dm3_c14_get  = dm3_c14.get()                
                dm3_c15_get  = dm3_c15.get()   
                dm3_c16_get  = dm3_c16.get() 
                dm3_c17_get  = dm3_c17.get() 
                dm3_c18_get  = dm3_c18.get()   
                dm3_c19_get  = dm3_c19.get()   
                dm3_c20_get  = dm3_c20.get()  

                dm4_c1_get   = dm4_c1.get()  
                dm4_c2_get   = dm4_c2.get()  
                dm4_c3_get   = dm4_c3.get()  
                dm4_c4_get   = dm4_c4.get()  
                dm4_c5_get   = dm4_c5.get()  
                dm4_c6_get   = dm4_c6.get()  
                dm4_c7_get   = dm4_c7.get()  
                dm4_c8_get   = dm4_c8.get()  
                dm4_c9_get   = dm4_c9.get()  
                dm4_c10_get  = dm4_c10.get()
                dm4_c11_get  = dm4_c11.get() 
                dm4_c12_get  = dm4_c12.get() 
                dm4_c13_get  = dm4_c13.get() 
                dm4_c14_get  = dm4_c14.get()                
                dm4_c15_get  = dm4_c15.get()   
                dm4_c16_get  = dm4_c16.get() 
                dm4_c17_get  = dm4_c17.get() 
                dm4_c18_get  = dm4_c18.get()   
                dm4_c19_get  = dm4_c19.get()   
                dm4_c20_get  = dm4_c20.get()  

                dm5_c1_get   = dm5_c1.get()  
                dm5_c2_get   = dm5_c2.get()  
                dm5_c3_get   = dm5_c3.get()  
                dm5_c4_get   = dm5_c4.get()  
                dm5_c5_get   = dm5_c5.get()  
                dm5_c6_get   = dm5_c6.get()  
                dm5_c7_get   = dm5_c7.get()  
                dm5_c8_get   = dm5_c8.get()  
                dm5_c9_get   = dm5_c9.get()  
                dm5_c10_get  = dm5_c10.get()
                dm5_c11_get  = dm5_c11.get() 
                dm5_c12_get  = dm5_c12.get() 
                dm5_c13_get  = dm5_c13.get() 
                dm5_c14_get  = dm5_c14.get()                
                dm5_c15_get  = dm5_c15.get() 
                dm5_c16_get  = dm5_c16.get() 
                dm5_c17_get  = dm5_c17.get() 
                dm5_c18_get  = dm5_c18.get()   
                dm5_c19_get  = dm5_c19.get()   
                dm5_c20_get  = dm5_c20.get()  

                dm_for_averagedm_cal=int(dm_number)

                c1_optimise_get =c1_optimise.get()
                c2_optimise_get =c2_optimise.get()
                c3_optimise_get =c3_optimise.get()
                c4_optimise_get =c4_optimise.get()
                c5_optimise_get =c5_optimise.get()
                c6_optimise_get =c6_optimise.get()
                c7_optimise_get =c7_optimise.get()
                c8_optimise_get =c8_optimise.get()
                c9_optimise_get =c9_optimise.get()
                c10_optimise_get=c10_optimise.get()
                c11_optimise_get=c11_optimise.get()
                c12_optimise_get=c12_optimise.get()
                c13_optimise_get=c13_optimise.get()
                c14_optimise_get=c14_optimise.get()
                c15_optimise_get=c15_optimise.get()
                c16_optimise_get=c16_optimise.get()
                c17_optimise_get=c17_optimise.get()
                c18_optimise_get=c18_optimise.get()
                c19_optimise_get=c19_optimise.get()
                c20_optimise_get=c20_optimise.get() 

                c_optimise_setdata = []
                c_optimise_setdata_list =[]
                c_optimise_setdata_list=matrix_optimise_fuzzy_dm_list(c_optimise_setdata,c_optimise_setdata_list,num_val_sublv2,rowdatabase, 
                c1_optimise_get ,c2_optimise_get ,c3_optimise_get ,c4_optimise_get ,c5_optimise_get ,
                c6_optimise_get ,c7_optimise_get ,c8_optimise_get ,c9_optimise_get ,c10_optimise_get,
                c11_optimise_get,c12_optimise_get,c13_optimise_get,c14_optimise_get,c15_optimise_get,
                c16_optimise_get,c17_optimise_get,c18_optimise_get,c19_optimise_get,c20_optimise_get)

                matrix_array_optimisation_C=function_matrix_array_optimisation_C(num_val_sublv2,c1_optimise_get ,c2_optimise_get ,c3_optimise_get ,c4_optimise_get 
                ,c5_optimise_get ,c6_optimise_get ,c7_optimise_get ,c8_optimise_get ,c9_optimise_get ,c10_optimise_get,c11_optimise_get,
                c12_optimise_get,c13_optimise_get,c14_optimise_get,c15_optimise_get,c16_optimise_get,c17_optimise_get,c18_optimise_get,c19_optimise_get,c20_optimise_get) 

                df_alternative = df['Material'].to_numpy()   
                average_ranking=[]                 


                if Typeofevaluation_Var.get() == 1:

                    quantitative_value_dm_c1 =((int(dm1_c1_get )+ int(dm2_c1_get )+ int(dm3_c1_get )+ int(dm4_c1_get )+ int(dm5_c1_get ))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c2 =((int(dm1_c2_get )+ int(dm2_c2_get )+ int(dm3_c2_get )+ int(dm4_c2_get )+ int(dm5_c2_get ))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c3 =((int(dm1_c3_get )+ int(dm2_c3_get )+ int(dm3_c3_get )+ int(dm4_c3_get )+ int(dm5_c3_get ))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c4 =((int(dm1_c4_get )+ int(dm2_c4_get )+ int(dm3_c4_get )+ int(dm4_c4_get )+ int(dm5_c4_get ))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c5 =((int(dm1_c5_get )+ int(dm2_c5_get )+ int(dm3_c5_get )+ int(dm4_c5_get )+ int(dm5_c5_get ))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c6 =((int(dm1_c6_get )+ int(dm2_c6_get )+ int(dm3_c6_get )+ int(dm4_c6_get )+ int(dm5_c6_get ))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c7 =((int(dm1_c7_get )+ int(dm2_c7_get )+ int(dm3_c7_get )+ int(dm4_c7_get )+ int(dm5_c7_get ))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c8 =((int(dm1_c8_get )+ int(dm2_c8_get )+ int(dm3_c8_get )+ int(dm4_c8_get )+ int(dm5_c8_get ))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c9 =((int(dm1_c9_get )+ int(dm2_c9_get )+ int(dm3_c9_get )+ int(dm4_c9_get )+ int(dm5_c9_get ))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c10=((int(dm1_c10_get)+ int(dm2_c10_get)+ int(dm3_c10_get)+ int(dm4_c10_get)+ int(dm5_c10_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c11=((int(dm1_c11_get)+ int(dm2_c11_get)+ int(dm3_c11_get)+ int(dm4_c11_get)+ int(dm5_c11_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c12=((int(dm1_c12_get)+ int(dm2_c12_get)+ int(dm3_c12_get)+ int(dm4_c12_get)+ int(dm5_c12_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c13=((int(dm1_c13_get)+ int(dm2_c13_get)+ int(dm3_c13_get)+ int(dm4_c13_get)+ int(dm5_c13_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c14=((int(dm1_c14_get)+ int(dm2_c14_get)+ int(dm3_c14_get)+ int(dm4_c14_get)+ int(dm5_c14_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c15=((int(dm1_c15_get)+ int(dm2_c15_get)+ int(dm3_c15_get)+ int(dm4_c15_get)+ int(dm5_c15_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c16=((int(dm1_c16_get)+ int(dm2_c16_get)+ int(dm3_c16_get)+ int(dm4_c16_get)+ int(dm5_c16_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c17=((int(dm1_c17_get)+ int(dm2_c17_get)+ int(dm3_c17_get)+ int(dm4_c17_get)+ int(dm5_c17_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c18=((int(dm1_c18_get)+ int(dm2_c18_get)+ int(dm3_c18_get)+ int(dm4_c18_get)+ int(dm5_c18_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c19=((int(dm1_c19_get)+ int(dm2_c19_get)+ int(dm3_c19_get)+ int(dm4_c19_get)+ int(dm5_c19_get))/10)/dm_for_averagedm_cal
                    quantitative_value_dm_c20=((int(dm1_c20_get)+ int(dm2_c20_get)+ int(dm3_c20_get)+ int(dm4_c20_get)+ int(dm5_c20_get))/10)/dm_for_averagedm_cal   

                    weight_matrix_dm = Matrix_quantitative_DM(num_val_sublv2,quantitative_value_dm_c1 ,quantitative_value_dm_c2 ,quantitative_value_dm_c3 ,quantitative_value_dm_c4 ,
                    quantitative_value_dm_c5 ,quantitative_value_dm_c6 ,quantitative_value_dm_c7 ,quantitative_value_dm_c8 ,quantitative_value_dm_c9 ,
                    quantitative_value_dm_c10,quantitative_value_dm_c11,quantitative_value_dm_c12,quantitative_value_dm_c13,quantitative_value_dm_c14,
                    quantitative_value_dm_c15,quantitative_value_dm_c16,quantitative_value_dm_c17,quantitative_value_dm_c18,quantitative_value_dm_c19,quantitative_value_dm_c20)

                    print(" ")
                    print('Ave. DMs weight:')
                    print(weight_matrix_dm)
                    print('List Optimisation:')
                    print(c_optimise_setdata_list)
                    print('')
                    print('TOPSIS and VIKOR module initatiated')
                    print('')
                    TOPSIS_RANK=TOPSIS(num_val_sublv2,weight_matrix_dm,matrix_array_optimisation_C)
                    print("TOPSIS RANK  :",TOPSIS_RANK) 
                    VIKOR_RANK=VIKOR(num_val_sublv2,weight_matrix_dm,matrix_array_optimisation_C)
                    print("VIKOR RANK   :",VIKOR_RANK) 
                    values1=TOPSIS_RANK
                    values2=VIKOR_RANK
                    for num1, num2 in zip(values1, values2):
                        average_ranking.append((num1+num2)/2)         
                    rankAVERAGE= [sorted(average_ranking,reverse=False).index(x)+1 for x in average_ranking]
                    print("Average RANK :",rankAVERAGE) 
                    print("")
                    rho_value=rho(values1, values2)
                    tau_value=tau(values1, values2)
                    print("rho value  :",rho_value) 
                    print("tau value  :",tau_value)         

                    def add_value_labels(ax, spacing=5):   
                        for rect in ax.patches: 
                            y_value = rect.get_height()
                            x_value = rect.get_x() + rect.get_width() / 2 
                            space = spacing 
                            va = 'bottom' 
                            if y_value < 0:
                                # Invert space to place label below
                                space *= -1
                                # Vertically align label at top
                                va = 'top' 
                            label = "{:}".format(y_value)
                            # Create annotation
                            ax.annotate(
                                label,                      # Use `label` as label
                                (x_value, y_value),         # Place label at end of the bar
                                xytext=(0, space),
                                fontsize=8,          # Vertically shift label by `space`
                                textcoords="offset points", # Interpret `xytext` as offset in points
                                ha='center',                # Horizontally center label
                                va=va)                      # Vertically align label differently for
                                                            # positive and negative values.        


                    data_rank = {'Material': df_alternative,'Ranking TOPSIS':values1,'Ranking VIKOR':values2, 'Average ranking':rankAVERAGE}  
                    data_rank=DataFrame(data_rank,columns=['Material','Ranking TOPSIS','Ranking VIKOR', 'Average ranking']) 
                    figureranking =  plt.Figure(edgecolor="#04253a",figsize=(10,5), dpi=140,facecolor="#e5e5e5")                                 
                    ax1 = figureranking.add_subplot(111)                            
                    bar1 = FigureCanvasTkAgg(figureranking, self.figure_fuzzy_DMs_Weight_frame)
                    bar1.get_tk_widget().pack() 
                    data_rank.plot(kind='bar', legend=True, ax=ax1,width=0.45,color=['slategrey', 'royalblue', 'black'])
                    ax1.set_title('Material Ranking', fontsize=8,fontweight="bold", y=1.0, pad=15) 
                    ax1.legend(fontsize=5)
                    ax1.set_xlabel('Material',fontsize=6)
                    ax1.set_ylabel('Ranking',fontsize=6)
                    ax1.tick_params(axis='both', which='major', labelsize=6)
                    print("") 
                    print(data_rank)                            
                    yLIMIT=len(df['Material'])
                    ax1.set_ylim([0, yLIMIT+3])
                    ax1.set_xticklabels(df_alternative, rotation=25, ha='right')                       
                    add_value_labels(ax1) 




                if Typeofevaluation_Var.get() > 1:

                    value_fuzzy_dm1_c1 =function_fuzzy_dm1_c1(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c1_get,dm2_c1_get,dm3_c1_get,dm4_c1_get,dm5_c1_get) 
                    value_fuzzy_dm1_c2 =function_fuzzy_dm1_c2(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c2_get,dm2_c2_get,dm3_c2_get,dm4_c2_get,dm5_c2_get)
                    value_fuzzy_dm1_c3 =function_fuzzy_dm1_c3(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c3_get,dm2_c3_get,dm3_c3_get,dm4_c3_get,dm5_c3_get)
                    value_fuzzy_dm1_c4 =function_fuzzy_dm1_c4(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c4_get,dm2_c4_get,dm3_c4_get,dm4_c4_get,dm5_c4_get)
                    value_fuzzy_dm1_c5 =function_fuzzy_dm1_c5(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c5_get,dm2_c5_get,dm3_c5_get,dm4_c5_get,dm5_c5_get)
                    value_fuzzy_dm1_c6 =function_fuzzy_dm1_c6(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c6_get,dm2_c6_get,dm3_c6_get,dm4_c6_get,dm5_c6_get)
                    value_fuzzy_dm1_c7 =function_fuzzy_dm1_c7(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c7_get,dm2_c7_get,dm3_c7_get,dm4_c7_get,dm5_c7_get)
                    value_fuzzy_dm1_c8 =function_fuzzy_dm1_c8(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c8_get,dm2_c8_get,dm3_c8_get,dm4_c8_get,dm5_c8_get)
                    value_fuzzy_dm1_c9 =function_fuzzy_dm1_c9(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c9_get,dm2_c9_get,dm3_c9_get,dm4_c9_get,dm5_c9_get)
                    value_fuzzy_dm1_c10=function_fuzzy_dm1_c10(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c10_get,dm2_c10_get,dm3_c10_get,dm4_c10_get,dm5_c10_get)
                    value_fuzzy_dm1_c11=function_fuzzy_dm1_c11(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c11_get,dm2_c11_get,dm3_c11_get,dm4_c11_get,dm5_c11_get)
                    value_fuzzy_dm1_c12=function_fuzzy_dm1_c12(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c12_get,dm2_c12_get,dm3_c12_get,dm4_c12_get,dm5_c12_get)
                    value_fuzzy_dm1_c13=function_fuzzy_dm1_c13(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c13_get,dm2_c13_get,dm3_c13_get,dm4_c13_get,dm5_c13_get)
                    value_fuzzy_dm1_c14=function_fuzzy_dm1_c14(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c14_get,dm2_c14_get,dm3_c14_get,dm4_c14_get,dm5_c14_get)
                    value_fuzzy_dm1_c15=function_fuzzy_dm1_c15(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c15_get,dm2_c15_get,dm3_c15_get,dm4_c15_get,dm5_c15_get)            
                    value_fuzzy_dm1_c16=function_fuzzy_dm1_c16(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c16_get,dm2_c16_get,dm3_c16_get,dm4_c16_get,dm5_c16_get)
                    value_fuzzy_dm1_c17=function_fuzzy_dm1_c17(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c17_get,dm2_c17_get,dm3_c17_get,dm4_c17_get,dm5_c17_get)
                    value_fuzzy_dm1_c18=function_fuzzy_dm1_c18(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c18_get,dm2_c18_get,dm3_c18_get,dm4_c18_get,dm5_c18_get)
                    value_fuzzy_dm1_c19=function_fuzzy_dm1_c19(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c19_get,dm2_c19_get,dm3_c19_get,dm4_c19_get,dm5_c19_get)
                    value_fuzzy_dm1_c20=function_fuzzy_dm1_c20(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c20_get,dm2_c20_get,dm3_c20_get,dm4_c20_get,dm5_c20_get)

                    value_fuzzy_dm2_c1 =function_fuzzy_dm2_c1(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c1_get,dm2_c1_get,dm3_c1_get,dm4_c1_get,dm5_c1_get)
                    value_fuzzy_dm2_c2 =function_fuzzy_dm2_c2(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c2_get,dm2_c2_get,dm3_c2_get,dm4_c2_get,dm5_c2_get)
                    value_fuzzy_dm2_c3 =function_fuzzy_dm2_c3(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c3_get,dm2_c3_get,dm3_c3_get,dm4_c3_get,dm5_c3_get)
                    value_fuzzy_dm2_c4 =function_fuzzy_dm2_c4(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c4_get,dm2_c4_get,dm3_c4_get,dm4_c4_get,dm5_c4_get)
                    value_fuzzy_dm2_c5 =function_fuzzy_dm2_c5(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c5_get,dm2_c5_get,dm3_c5_get,dm4_c5_get,dm5_c5_get)
                    value_fuzzy_dm2_c6 =function_fuzzy_dm2_c6(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c6_get,dm2_c6_get,dm3_c6_get,dm4_c6_get,dm5_c6_get)
                    value_fuzzy_dm2_c7 =function_fuzzy_dm2_c7(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c7_get,dm2_c7_get,dm3_c7_get,dm4_c7_get,dm5_c7_get)
                    value_fuzzy_dm2_c8 =function_fuzzy_dm2_c8(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c8_get,dm2_c8_get,dm3_c8_get,dm4_c8_get,dm5_c8_get)
                    value_fuzzy_dm2_c9 =function_fuzzy_dm2_c9(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c9_get,dm2_c9_get,dm3_c9_get,dm4_c9_get,dm5_c9_get)
                    value_fuzzy_dm2_c10=function_fuzzy_dm2_c10(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c10_get,dm2_c10_get,dm3_c10_get,dm4_c10_get,dm5_c10_get)
                    value_fuzzy_dm2_c11=function_fuzzy_dm2_c11(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c11_get,dm2_c11_get,dm3_c11_get,dm4_c11_get,dm5_c11_get)
                    value_fuzzy_dm2_c12=function_fuzzy_dm2_c12(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c12_get,dm2_c12_get,dm3_c12_get,dm4_c12_get,dm5_c12_get)
                    value_fuzzy_dm2_c13=function_fuzzy_dm2_c13(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c13_get,dm2_c13_get,dm3_c13_get,dm4_c13_get,dm5_c13_get)
                    value_fuzzy_dm2_c14=function_fuzzy_dm2_c14(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c14_get,dm2_c14_get,dm3_c14_get,dm4_c14_get,dm5_c14_get)
                    value_fuzzy_dm2_c15=function_fuzzy_dm2_c15(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c15_get,dm2_c15_get,dm3_c15_get,dm4_c15_get,dm5_c15_get)    
                    value_fuzzy_dm2_c16=function_fuzzy_dm2_c16(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c16_get,dm2_c16_get,dm3_c16_get,dm4_c16_get,dm5_c16_get)
                    value_fuzzy_dm2_c17=function_fuzzy_dm2_c17(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c17_get,dm2_c17_get,dm3_c17_get,dm4_c17_get,dm5_c17_get)
                    value_fuzzy_dm2_c18=function_fuzzy_dm2_c18(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c18_get,dm2_c18_get,dm3_c18_get,dm4_c18_get,dm5_c18_get)
                    value_fuzzy_dm2_c19=function_fuzzy_dm2_c19(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c19_get,dm2_c19_get,dm3_c19_get,dm4_c19_get,dm5_c19_get)
                    value_fuzzy_dm2_c20=function_fuzzy_dm2_c20(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c20_get,dm2_c20_get,dm3_c20_get,dm4_c20_get,dm5_c20_get)

                    value_fuzzy_dm3_c1 =function_fuzzy_dm3_c1(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c1_get,dm2_c1_get,dm3_c1_get,dm4_c1_get,dm5_c1_get)
                    value_fuzzy_dm3_c2 =function_fuzzy_dm3_c2(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c2_get,dm2_c2_get,dm3_c2_get,dm4_c2_get,dm5_c2_get)
                    value_fuzzy_dm3_c3 =function_fuzzy_dm3_c3(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c3_get,dm2_c3_get,dm3_c3_get,dm4_c3_get,dm5_c3_get)
                    value_fuzzy_dm3_c4 =function_fuzzy_dm3_c4(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c4_get,dm2_c4_get,dm3_c4_get,dm4_c4_get,dm5_c4_get)
                    value_fuzzy_dm3_c5 =function_fuzzy_dm3_c5(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c5_get,dm2_c5_get,dm3_c5_get,dm4_c5_get,dm5_c5_get)
                    value_fuzzy_dm3_c6 =function_fuzzy_dm3_c6(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c6_get,dm2_c6_get,dm3_c6_get,dm4_c6_get,dm5_c6_get)
                    value_fuzzy_dm3_c7 =function_fuzzy_dm3_c7(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c7_get,dm2_c7_get,dm3_c7_get,dm4_c7_get,dm5_c7_get)
                    value_fuzzy_dm3_c8 =function_fuzzy_dm3_c8(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c8_get,dm2_c8_get,dm3_c8_get,dm4_c8_get,dm5_c8_get)
                    value_fuzzy_dm3_c9 =function_fuzzy_dm3_c9(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c9_get,dm2_c9_get,dm3_c9_get,dm4_c9_get,dm5_c9_get)
                    value_fuzzy_dm3_c10=function_fuzzy_dm3_c10(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c10_get,dm2_c10_get,dm3_c10_get,dm4_c10_get,dm5_c10_get)
                    value_fuzzy_dm3_c11=function_fuzzy_dm3_c11(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c11_get,dm2_c11_get,dm3_c11_get,dm4_c11_get,dm5_c11_get)
                    value_fuzzy_dm3_c12=function_fuzzy_dm3_c12(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c12_get,dm2_c12_get,dm3_c12_get,dm4_c12_get,dm5_c12_get)
                    value_fuzzy_dm3_c13=function_fuzzy_dm3_c13(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c13_get,dm2_c13_get,dm3_c13_get,dm4_c13_get,dm5_c13_get)
                    value_fuzzy_dm3_c14=function_fuzzy_dm3_c14(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c14_get,dm2_c14_get,dm3_c14_get,dm4_c14_get,dm5_c14_get)
                    value_fuzzy_dm3_c15=function_fuzzy_dm3_c15(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c15_get,dm2_c15_get,dm3_c15_get,dm4_c15_get,dm5_c15_get)    
                    value_fuzzy_dm3_c16=function_fuzzy_dm3_c16(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c16_get,dm2_c16_get,dm3_c16_get,dm4_c16_get,dm5_c16_get)
                    value_fuzzy_dm3_c17=function_fuzzy_dm3_c17(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c17_get,dm2_c17_get,dm3_c17_get,dm4_c17_get,dm5_c17_get)
                    value_fuzzy_dm3_c18=function_fuzzy_dm3_c18(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c18_get,dm2_c18_get,dm3_c18_get,dm4_c18_get,dm5_c18_get)
                    value_fuzzy_dm3_c19=function_fuzzy_dm3_c19(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c19_get,dm2_c19_get,dm3_c19_get,dm4_c19_get,dm5_c19_get)
                    value_fuzzy_dm3_c20=function_fuzzy_dm3_c20(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c20_get,dm2_c20_get,dm3_c20_get,dm4_c20_get,dm5_c20_get)

                    value_fuzzy_dm4_c1 =function_fuzzy_dm4_c1(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c1_get,dm2_c1_get,dm3_c1_get,dm4_c1_get,dm5_c1_get)
                    value_fuzzy_dm4_c2 =function_fuzzy_dm4_c2(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c2_get,dm2_c2_get,dm3_c2_get,dm4_c2_get,dm5_c2_get)
                    value_fuzzy_dm4_c3 =function_fuzzy_dm4_c3(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c3_get,dm2_c3_get,dm3_c3_get,dm4_c3_get,dm5_c3_get)
                    value_fuzzy_dm4_c4 =function_fuzzy_dm4_c4(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c4_get,dm2_c4_get,dm3_c4_get,dm4_c4_get,dm5_c4_get)
                    value_fuzzy_dm4_c5 =function_fuzzy_dm4_c5(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c5_get,dm2_c5_get,dm3_c5_get,dm4_c5_get,dm5_c5_get)
                    value_fuzzy_dm4_c6 =function_fuzzy_dm4_c6(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c6_get,dm2_c6_get,dm3_c6_get,dm4_c6_get,dm5_c6_get)
                    value_fuzzy_dm4_c7 =function_fuzzy_dm4_c7(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c7_get,dm2_c7_get,dm3_c7_get,dm4_c7_get,dm5_c7_get)
                    value_fuzzy_dm4_c8 =function_fuzzy_dm4_c8(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c8_get,dm2_c8_get,dm3_c8_get,dm4_c8_get,dm5_c8_get)
                    value_fuzzy_dm4_c9 =function_fuzzy_dm4_c9(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c9_get,dm2_c9_get,dm3_c9_get,dm4_c9_get,dm5_c9_get)
                    value_fuzzy_dm4_c10=function_fuzzy_dm4_c10(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c10_get,dm2_c10_get,dm3_c10_get,dm4_c10_get,dm5_c10_get)
                    value_fuzzy_dm4_c11=function_fuzzy_dm4_c11(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c11_get,dm2_c11_get,dm3_c11_get,dm4_c11_get,dm5_c11_get)
                    value_fuzzy_dm4_c12=function_fuzzy_dm4_c12(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c12_get,dm2_c12_get,dm3_c12_get,dm4_c12_get,dm5_c12_get)
                    value_fuzzy_dm4_c13=function_fuzzy_dm4_c13(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c13_get,dm2_c13_get,dm3_c13_get,dm4_c13_get,dm5_c13_get)
                    value_fuzzy_dm4_c14=function_fuzzy_dm4_c14(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c14_get,dm2_c14_get,dm3_c14_get,dm4_c14_get,dm5_c14_get)
                    value_fuzzy_dm4_c15=function_fuzzy_dm4_c15(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c15_get,dm2_c15_get,dm3_c15_get,dm4_c15_get,dm5_c15_get)    
                    value_fuzzy_dm4_c16=function_fuzzy_dm4_c16(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c16_get,dm2_c16_get,dm3_c16_get,dm4_c16_get,dm5_c16_get)
                    value_fuzzy_dm4_c17=function_fuzzy_dm4_c17(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c17_get,dm2_c17_get,dm3_c17_get,dm4_c17_get,dm5_c17_get)
                    value_fuzzy_dm4_c18=function_fuzzy_dm4_c18(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c18_get,dm2_c18_get,dm3_c18_get,dm4_c18_get,dm5_c18_get)
                    value_fuzzy_dm4_c19=function_fuzzy_dm4_c19(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c19_get,dm2_c19_get,dm3_c19_get,dm4_c19_get,dm5_c19_get)
                    value_fuzzy_dm4_c20=function_fuzzy_dm4_c20(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c20_get,dm2_c20_get,dm3_c20_get,dm4_c20_get,dm5_c20_get)

                    value_fuzzy_dm5_c1 =function_fuzzy_dm5_c1(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c1_get,dm2_c1_get,dm3_c1_get,dm4_c1_get,dm5_c1_get)
                    value_fuzzy_dm5_c2 =function_fuzzy_dm5_c2(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c2_get,dm2_c2_get,dm3_c2_get,dm4_c2_get,dm5_c2_get)
                    value_fuzzy_dm5_c3 =function_fuzzy_dm5_c3(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c3_get,dm2_c3_get,dm3_c3_get,dm4_c3_get,dm5_c3_get)
                    value_fuzzy_dm5_c4 =function_fuzzy_dm5_c4(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c4_get,dm2_c4_get,dm3_c4_get,dm4_c4_get,dm5_c4_get)
                    value_fuzzy_dm5_c5 =function_fuzzy_dm5_c5(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c5_get,dm2_c5_get,dm3_c5_get,dm4_c5_get,dm5_c5_get)
                    value_fuzzy_dm5_c6 =function_fuzzy_dm5_c6(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c6_get,dm2_c6_get,dm3_c6_get,dm4_c6_get,dm5_c6_get)
                    value_fuzzy_dm5_c7 =function_fuzzy_dm5_c7(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c7_get,dm2_c7_get,dm3_c7_get,dm4_c7_get,dm5_c7_get)
                    value_fuzzy_dm5_c8 =function_fuzzy_dm5_c8(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c8_get,dm2_c8_get,dm3_c8_get,dm4_c8_get,dm5_c8_get)
                    value_fuzzy_dm5_c9 =function_fuzzy_dm5_c9(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c9_get,dm2_c9_get,dm3_c9_get,dm4_c9_get,dm5_c9_get)
                    value_fuzzy_dm5_c10=function_fuzzy_dm5_c10(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c10_get,dm2_c10_get,dm3_c10_get,dm4_c10_get,dm5_c10_get)
                    value_fuzzy_dm5_c11=function_fuzzy_dm5_c11(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c11_get,dm2_c11_get,dm3_c11_get,dm4_c11_get,dm5_c11_get)
                    value_fuzzy_dm5_c12=function_fuzzy_dm5_c12(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c12_get,dm2_c12_get,dm3_c12_get,dm4_c12_get,dm5_c12_get)
                    value_fuzzy_dm5_c13=function_fuzzy_dm5_c13(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c13_get,dm2_c13_get,dm3_c13_get,dm4_c13_get,dm5_c13_get)
                    value_fuzzy_dm5_c14=function_fuzzy_dm5_c14(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c14_get,dm2_c14_get,dm3_c14_get,dm4_c14_get,dm5_c14_get)
                    value_fuzzy_dm5_c15=function_fuzzy_dm5_c15(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c15_get,dm2_c15_get,dm3_c15_get,dm4_c15_get,dm5_c15_get)    
                    value_fuzzy_dm5_c16=function_fuzzy_dm5_c16(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c16_get,dm2_c16_get,dm3_c16_get,dm4_c16_get,dm5_c16_get)
                    value_fuzzy_dm5_c17=function_fuzzy_dm5_c17(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c17_get,dm2_c17_get,dm3_c17_get,dm4_c17_get,dm5_c17_get)
                    value_fuzzy_dm5_c18=function_fuzzy_dm5_c18(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c18_get,dm2_c18_get,dm3_c18_get,dm4_c18_get,dm5_c18_get)
                    value_fuzzy_dm5_c19=function_fuzzy_dm5_c19(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c19_get,dm2_c19_get,dm3_c19_get,dm4_c19_get,dm5_c19_get)
                    value_fuzzy_dm5_c20=function_fuzzy_dm5_c20(fz1,fz2,fz3,fz4,fz5,fz6,fz7,fz8,fz9,fz10,dm1_c20_get,dm2_c20_get,dm3_c20_get,dm4_c20_get,dm5_c20_get)

                    matrix_value_fuzzy_dm1_c1 =np.array(value_fuzzy_dm1_c1 )           
                    matrix_value_fuzzy_dm1_c2 =np.array(value_fuzzy_dm1_c2 )           
                    matrix_value_fuzzy_dm1_c3 =np.array(value_fuzzy_dm1_c3 )           
                    matrix_value_fuzzy_dm1_c4 =np.array(value_fuzzy_dm1_c4 )           
                    matrix_value_fuzzy_dm1_c5 =np.array(value_fuzzy_dm1_c5 )           
                    matrix_value_fuzzy_dm1_c6 =np.array(value_fuzzy_dm1_c6 )           
                    matrix_value_fuzzy_dm1_c7 =np.array(value_fuzzy_dm1_c7 )           
                    matrix_value_fuzzy_dm1_c8 =np.array(value_fuzzy_dm1_c8 )           
                    matrix_value_fuzzy_dm1_c9 =np.array(value_fuzzy_dm1_c9 )           
                    matrix_value_fuzzy_dm1_c10=np.array(value_fuzzy_dm1_c10)        
                    matrix_value_fuzzy_dm1_c11=np.array(value_fuzzy_dm1_c11)        
                    matrix_value_fuzzy_dm1_c12=np.array(value_fuzzy_dm1_c12)        
                    matrix_value_fuzzy_dm1_c13=np.array(value_fuzzy_dm1_c13)        
                    matrix_value_fuzzy_dm1_c14=np.array(value_fuzzy_dm1_c14)        
                    matrix_value_fuzzy_dm1_c15=np.array(value_fuzzy_dm1_c15)      
                    matrix_value_fuzzy_dm1_c16=np.array(value_fuzzy_dm1_c16)        
                    matrix_value_fuzzy_dm1_c17=np.array(value_fuzzy_dm1_c17)        
                    matrix_value_fuzzy_dm1_c18=np.array(value_fuzzy_dm1_c18)        
                    matrix_value_fuzzy_dm1_c19=np.array(value_fuzzy_dm1_c19)        
                    matrix_value_fuzzy_dm1_c20=np.array(value_fuzzy_dm1_c20) 

                    matrix_value_fuzzy_dm2_c1 =np.array(value_fuzzy_dm2_c1 )           
                    matrix_value_fuzzy_dm2_c2 =np.array(value_fuzzy_dm2_c2 )           
                    matrix_value_fuzzy_dm2_c3 =np.array(value_fuzzy_dm2_c3 )           
                    matrix_value_fuzzy_dm2_c4 =np.array(value_fuzzy_dm2_c4 )           
                    matrix_value_fuzzy_dm2_c5 =np.array(value_fuzzy_dm2_c5 )           
                    matrix_value_fuzzy_dm2_c6 =np.array(value_fuzzy_dm2_c6 )           
                    matrix_value_fuzzy_dm2_c7 =np.array(value_fuzzy_dm2_c7 )           
                    matrix_value_fuzzy_dm2_c8 =np.array(value_fuzzy_dm2_c8 )           
                    matrix_value_fuzzy_dm2_c9 =np.array(value_fuzzy_dm2_c9 )           
                    matrix_value_fuzzy_dm2_c10=np.array(value_fuzzy_dm2_c10)           
                    matrix_value_fuzzy_dm2_c11=np.array(value_fuzzy_dm2_c11)           
                    matrix_value_fuzzy_dm2_c12=np.array(value_fuzzy_dm2_c12)           
                    matrix_value_fuzzy_dm2_c13=np.array(value_fuzzy_dm2_c13)           
                    matrix_value_fuzzy_dm2_c14=np.array(value_fuzzy_dm2_c14)           
                    matrix_value_fuzzy_dm2_c15=np.array(value_fuzzy_dm2_c15)         
                    matrix_value_fuzzy_dm2_c16=np.array(value_fuzzy_dm2_c16)        
                    matrix_value_fuzzy_dm2_c17=np.array(value_fuzzy_dm2_c17)        
                    matrix_value_fuzzy_dm2_c18=np.array(value_fuzzy_dm2_c18)        
                    matrix_value_fuzzy_dm2_c19=np.array(value_fuzzy_dm2_c19)        
                    matrix_value_fuzzy_dm2_c20=np.array(value_fuzzy_dm2_c20)    

                    matrix_value_fuzzy_dm3_c1 =np.array(value_fuzzy_dm3_c1 )           
                    matrix_value_fuzzy_dm3_c2 =np.array(value_fuzzy_dm3_c2 )           
                    matrix_value_fuzzy_dm3_c3 =np.array(value_fuzzy_dm3_c3 )           
                    matrix_value_fuzzy_dm3_c4 =np.array(value_fuzzy_dm3_c4 )           
                    matrix_value_fuzzy_dm3_c5 =np.array(value_fuzzy_dm3_c5 )           
                    matrix_value_fuzzy_dm3_c6 =np.array(value_fuzzy_dm3_c6 )           
                    matrix_value_fuzzy_dm3_c7 =np.array(value_fuzzy_dm3_c7 )           
                    matrix_value_fuzzy_dm3_c8 =np.array(value_fuzzy_dm3_c8 )           
                    matrix_value_fuzzy_dm3_c9 =np.array(value_fuzzy_dm3_c9 )           
                    matrix_value_fuzzy_dm3_c10=np.array(value_fuzzy_dm3_c10)           
                    matrix_value_fuzzy_dm3_c11=np.array(value_fuzzy_dm3_c11)           
                    matrix_value_fuzzy_dm3_c12=np.array(value_fuzzy_dm3_c12)           
                    matrix_value_fuzzy_dm3_c13=np.array(value_fuzzy_dm3_c13)           
                    matrix_value_fuzzy_dm3_c14=np.array(value_fuzzy_dm3_c14)           
                    matrix_value_fuzzy_dm3_c15=np.array(value_fuzzy_dm3_c15)     
                    matrix_value_fuzzy_dm3_c16=np.array(value_fuzzy_dm3_c16)        
                    matrix_value_fuzzy_dm3_c17=np.array(value_fuzzy_dm3_c17)        
                    matrix_value_fuzzy_dm3_c18=np.array(value_fuzzy_dm3_c18)        
                    matrix_value_fuzzy_dm3_c19=np.array(value_fuzzy_dm3_c19)        
                    matrix_value_fuzzy_dm3_c20=np.array(value_fuzzy_dm3_c20)        

                    matrix_value_fuzzy_dm4_c1 =np.array(value_fuzzy_dm4_c1 )           
                    matrix_value_fuzzy_dm4_c2 =np.array(value_fuzzy_dm4_c2 )           
                    matrix_value_fuzzy_dm4_c3 =np.array(value_fuzzy_dm4_c3 )           
                    matrix_value_fuzzy_dm4_c4 =np.array(value_fuzzy_dm4_c4 )           
                    matrix_value_fuzzy_dm4_c5 =np.array(value_fuzzy_dm4_c5 )           
                    matrix_value_fuzzy_dm4_c6 =np.array(value_fuzzy_dm4_c6 )           
                    matrix_value_fuzzy_dm4_c7 =np.array(value_fuzzy_dm4_c7 )           
                    matrix_value_fuzzy_dm4_c8 =np.array(value_fuzzy_dm4_c8 )           
                    matrix_value_fuzzy_dm4_c9 =np.array(value_fuzzy_dm4_c9 )           
                    matrix_value_fuzzy_dm4_c10=np.array(value_fuzzy_dm4_c10)           
                    matrix_value_fuzzy_dm4_c11=np.array(value_fuzzy_dm4_c11)           
                    matrix_value_fuzzy_dm4_c12=np.array(value_fuzzy_dm4_c12)           
                    matrix_value_fuzzy_dm4_c13=np.array(value_fuzzy_dm4_c13)           
                    matrix_value_fuzzy_dm4_c14=np.array(value_fuzzy_dm4_c14)           
                    matrix_value_fuzzy_dm4_c15=np.array(value_fuzzy_dm4_c15)        
                    matrix_value_fuzzy_dm4_c16=np.array(value_fuzzy_dm4_c16)        
                    matrix_value_fuzzy_dm4_c17=np.array(value_fuzzy_dm4_c17)        
                    matrix_value_fuzzy_dm4_c18=np.array(value_fuzzy_dm4_c18)        
                    matrix_value_fuzzy_dm4_c19=np.array(value_fuzzy_dm4_c19)        
                    matrix_value_fuzzy_dm4_c20=np.array(value_fuzzy_dm4_c20)     

                    matrix_value_fuzzy_dm5_c1 =np.array(value_fuzzy_dm5_c1 )           
                    matrix_value_fuzzy_dm5_c2 =np.array(value_fuzzy_dm5_c2 )           
                    matrix_value_fuzzy_dm5_c3 =np.array(value_fuzzy_dm5_c3 )           
                    matrix_value_fuzzy_dm5_c4 =np.array(value_fuzzy_dm5_c4 )           
                    matrix_value_fuzzy_dm5_c5 =np.array(value_fuzzy_dm5_c5 )           
                    matrix_value_fuzzy_dm5_c6 =np.array(value_fuzzy_dm5_c6 )           
                    matrix_value_fuzzy_dm5_c7 =np.array(value_fuzzy_dm5_c7 )           
                    matrix_value_fuzzy_dm5_c8 =np.array(value_fuzzy_dm5_c8 )           
                    matrix_value_fuzzy_dm5_c9 =np.array(value_fuzzy_dm5_c9 )           
                    matrix_value_fuzzy_dm5_c10=np.array(value_fuzzy_dm5_c10)           
                    matrix_value_fuzzy_dm5_c11=np.array(value_fuzzy_dm5_c11)           
                    matrix_value_fuzzy_dm5_c12=np.array(value_fuzzy_dm5_c12)           
                    matrix_value_fuzzy_dm5_c13=np.array(value_fuzzy_dm5_c13)           
                    matrix_value_fuzzy_dm5_c14=np.array(value_fuzzy_dm5_c14)           
                    matrix_value_fuzzy_dm5_c15=np.array(value_fuzzy_dm5_c15)     
                    matrix_value_fuzzy_dm5_c16=np.array(value_fuzzy_dm5_c16)        
                    matrix_value_fuzzy_dm5_c17=np.array(value_fuzzy_dm5_c17)        
                    matrix_value_fuzzy_dm5_c18=np.array(value_fuzzy_dm5_c18)        
                    matrix_value_fuzzy_dm5_c19=np.array(value_fuzzy_dm5_c19)        
                    matrix_value_fuzzy_dm5_c20=np.array(value_fuzzy_dm5_c20) 

                    matrix_value_fuzzy_dm_c1 =np.array((matrix_value_fuzzy_dm1_c1 +matrix_value_fuzzy_dm2_c1 +matrix_value_fuzzy_dm3_c1 +matrix_value_fuzzy_dm4_c1 +matrix_value_fuzzy_dm5_c1 )/dm_for_averagedm_cal) 
                    matrix_value_fuzzy_dm_c2 =np.array((matrix_value_fuzzy_dm1_c2 +matrix_value_fuzzy_dm2_c2 +matrix_value_fuzzy_dm3_c2 +matrix_value_fuzzy_dm4_c2 +matrix_value_fuzzy_dm5_c2 )/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c3 =np.array((matrix_value_fuzzy_dm1_c3 +matrix_value_fuzzy_dm2_c3 +matrix_value_fuzzy_dm3_c3 +matrix_value_fuzzy_dm4_c3 +matrix_value_fuzzy_dm5_c3 )/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c4 =np.array((matrix_value_fuzzy_dm1_c4 +matrix_value_fuzzy_dm2_c4 +matrix_value_fuzzy_dm3_c4 +matrix_value_fuzzy_dm4_c4 +matrix_value_fuzzy_dm5_c4 )/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c5 =np.array((matrix_value_fuzzy_dm1_c5 +matrix_value_fuzzy_dm2_c5 +matrix_value_fuzzy_dm3_c5 +matrix_value_fuzzy_dm4_c5 +matrix_value_fuzzy_dm5_c5 )/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c6 =np.array((matrix_value_fuzzy_dm1_c6 +matrix_value_fuzzy_dm2_c6 +matrix_value_fuzzy_dm3_c6 +matrix_value_fuzzy_dm4_c6 +matrix_value_fuzzy_dm5_c6 )/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c7 =np.array((matrix_value_fuzzy_dm1_c7 +matrix_value_fuzzy_dm2_c7 +matrix_value_fuzzy_dm3_c7 +matrix_value_fuzzy_dm4_c7 +matrix_value_fuzzy_dm5_c7 )/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c8 =np.array((matrix_value_fuzzy_dm1_c8 +matrix_value_fuzzy_dm2_c8 +matrix_value_fuzzy_dm3_c8 +matrix_value_fuzzy_dm4_c8 +matrix_value_fuzzy_dm5_c8 )/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c9 =np.array((matrix_value_fuzzy_dm1_c9 +matrix_value_fuzzy_dm2_c9 +matrix_value_fuzzy_dm3_c9 +matrix_value_fuzzy_dm4_c9 +matrix_value_fuzzy_dm5_c9 )/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c10=np.array((matrix_value_fuzzy_dm1_c10+matrix_value_fuzzy_dm2_c10+matrix_value_fuzzy_dm3_c10+matrix_value_fuzzy_dm4_c10+matrix_value_fuzzy_dm5_c10)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c11=np.array((matrix_value_fuzzy_dm1_c11+matrix_value_fuzzy_dm2_c11+matrix_value_fuzzy_dm3_c11+matrix_value_fuzzy_dm4_c11+matrix_value_fuzzy_dm5_c11)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c12=np.array((matrix_value_fuzzy_dm1_c12+matrix_value_fuzzy_dm2_c12+matrix_value_fuzzy_dm3_c12+matrix_value_fuzzy_dm4_c12+matrix_value_fuzzy_dm5_c12)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c13=np.array((matrix_value_fuzzy_dm1_c13+matrix_value_fuzzy_dm2_c13+matrix_value_fuzzy_dm3_c13+matrix_value_fuzzy_dm4_c13+matrix_value_fuzzy_dm5_c13)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c14=np.array((matrix_value_fuzzy_dm1_c14+matrix_value_fuzzy_dm2_c14+matrix_value_fuzzy_dm3_c14+matrix_value_fuzzy_dm4_c14+matrix_value_fuzzy_dm5_c14)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c15=np.array((matrix_value_fuzzy_dm1_c15+matrix_value_fuzzy_dm2_c15+matrix_value_fuzzy_dm3_c15+matrix_value_fuzzy_dm4_c15+matrix_value_fuzzy_dm5_c15)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c16=np.array((matrix_value_fuzzy_dm1_c16+matrix_value_fuzzy_dm2_c16+matrix_value_fuzzy_dm3_c16+matrix_value_fuzzy_dm4_c16+matrix_value_fuzzy_dm5_c16)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c17=np.array((matrix_value_fuzzy_dm1_c17+matrix_value_fuzzy_dm2_c17+matrix_value_fuzzy_dm3_c17+matrix_value_fuzzy_dm4_c17+matrix_value_fuzzy_dm5_c17)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c18=np.array((matrix_value_fuzzy_dm1_c18+matrix_value_fuzzy_dm2_c18+matrix_value_fuzzy_dm3_c18+matrix_value_fuzzy_dm4_c18+matrix_value_fuzzy_dm5_c18)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c19=np.array((matrix_value_fuzzy_dm1_c19+matrix_value_fuzzy_dm2_c19+matrix_value_fuzzy_dm3_c19+matrix_value_fuzzy_dm4_c19+matrix_value_fuzzy_dm5_c19)/dm_for_averagedm_cal)
                    matrix_value_fuzzy_dm_c20=np.array((matrix_value_fuzzy_dm1_c20+matrix_value_fuzzy_dm2_c20+matrix_value_fuzzy_dm3_c20+matrix_value_fuzzy_dm4_c20+matrix_value_fuzzy_dm5_c20)/dm_for_averagedm_cal)   

                    ave_dmqualitative = []
                    ave_dmqualitative_list =[] 
                    ave_dmqualitative_list =matrix_value_fuzzy_dm_list(ave_dmqualitative,ave_dmqualitative_list,num_val_sublv2,rowdatabase,
                    matrix_value_fuzzy_dm_c1 ,matrix_value_fuzzy_dm_c2 ,matrix_value_fuzzy_dm_c3 ,matrix_value_fuzzy_dm_c4 ,matrix_value_fuzzy_dm_c5 ,
                    matrix_value_fuzzy_dm_c6 ,matrix_value_fuzzy_dm_c7 ,matrix_value_fuzzy_dm_c8 ,matrix_value_fuzzy_dm_c9 ,matrix_value_fuzzy_dm_c10,
                    matrix_value_fuzzy_dm_c11,matrix_value_fuzzy_dm_c12,matrix_value_fuzzy_dm_c13,matrix_value_fuzzy_dm_c14,matrix_value_fuzzy_dm_c15,
                    matrix_value_fuzzy_dm_c16,matrix_value_fuzzy_dm_c17,matrix_value_fuzzy_dm_c18,matrix_value_fuzzy_dm_c19,matrix_value_fuzzy_dm_c20) 
                    
                    # create temporary matrix at database for dm values.

                    weight_matrix_dm = Matrix_quantitative_DM(num_val_sublv2,matrix_value_fuzzy_dm_c1 ,matrix_value_fuzzy_dm_c2 ,matrix_value_fuzzy_dm_c3 ,matrix_value_fuzzy_dm_c4 ,matrix_value_fuzzy_dm_c5 ,
                    matrix_value_fuzzy_dm_c6 , matrix_value_fuzzy_dm_c7 ,matrix_value_fuzzy_dm_c8 ,matrix_value_fuzzy_dm_c9 ,matrix_value_fuzzy_dm_c10,matrix_value_fuzzy_dm_c11,matrix_value_fuzzy_dm_c12,
                    matrix_value_fuzzy_dm_c13,matrix_value_fuzzy_dm_c14,matrix_value_fuzzy_dm_c15,matrix_value_fuzzy_dm_c16,matrix_value_fuzzy_dm_c17,matrix_value_fuzzy_dm_c18,matrix_value_fuzzy_dm_c19,matrix_value_fuzzy_dm_c20)

                    print(" ")
                    print('Ave. DMs Fuzzy weight:')
                    print(ave_dmqualitative_list)


                    by=[0,1,0] 
                    data1 = {'Y': matrix_value_fuzzy_dm_c1 ,'average_fuzzyweight_DMs_C1': by }                
                    data2 = {'Y': matrix_value_fuzzy_dm_c2 ,'average_fuzzyweight_DMs_C2': by }
                    data3 = {'Y': matrix_value_fuzzy_dm_c3 ,'average_fuzzyweight_DMs_C3': by }
                    data4 = {'Y': matrix_value_fuzzy_dm_c4 ,'average_fuzzyweight_DMs_C4': by }
                    data5 = {'Y': matrix_value_fuzzy_dm_c5 ,'average_fuzzyweight_DMs_C5': by }
                    data6 = {'Y': matrix_value_fuzzy_dm_c6 ,'average_fuzzyweight_DMs_C6': by }
                    data7 = {'Y': matrix_value_fuzzy_dm_c7 ,'average_fuzzyweight_DMs_C7': by }
                    data8 = {'Y': matrix_value_fuzzy_dm_c8 ,'average_fuzzyweight_DMs_C8': by }
                    data9 = {'Y': matrix_value_fuzzy_dm_c9 ,'average_fuzzyweight_DMs_C9': by }
                    data10 = {'Y': matrix_value_fuzzy_dm_c10,'average_fuzzyweight_DMs_C10': by }
                    data11 = {'Y': matrix_value_fuzzy_dm_c11,'average_fuzzyweight_DMs_C11': by }
                    data12 = {'Y': matrix_value_fuzzy_dm_c12,'average_fuzzyweight_DMs_C12': by }
                    data13 = {'Y': matrix_value_fuzzy_dm_c13,'average_fuzzyweight_DMs_C13': by }
                    data14 = {'Y': matrix_value_fuzzy_dm_c14,'average_fuzzyweight_DMs_C14': by }         
                    data15 = {'Y': matrix_value_fuzzy_dm_c15,'average_fuzzyweight_DMs_C15': by }
                    data16 = {'Y': matrix_value_fuzzy_dm_c10,'average_fuzzyweight_DMs_C16': by }
                    data17 = {'Y': matrix_value_fuzzy_dm_c11,'average_fuzzyweight_DMs_C17': by }
                    data18 = {'Y': matrix_value_fuzzy_dm_c12,'average_fuzzyweight_DMs_C18': by }
                    data19 = {'Y': matrix_value_fuzzy_dm_c13,'average_fuzzyweight_DMs_C19': by }
                    data20 = {'Y': matrix_value_fuzzy_dm_c14,'average_fuzzyweight_DMs_C20': by }         

                    markersize_plot=7
                    fontsize_plot=7

                    def plot_ave_f_dms_C1() :        
                      df1   = DataFrame(data1,columns=['Y','average_fuzzyweight_DMs_C1'])
                      df1   = df1[['Y','average_fuzzyweight_DMs_C1']].groupby('Y').sum()
                      df1.plot(kind='line',  legend=True, ax=ax2, color='b',marker='.',markersize=markersize_plot, fontsize=fontsize_plot) 

                    def plot_ave_f_dms_C2() :
                      plot_ave_f_dms_C1()
                      df2   = DataFrame(data2,columns=['Y','average_fuzzyweight_DMs_C2'])
                      df2   = df2[['Y','average_fuzzyweight_DMs_C2']].groupby('Y').sum()
                      df2.plot(kind='line',  legend=True, ax=ax2, color='g',marker='o',markersize=markersize_plot, fontsize=fontsize_plot) 

                    def plot_ave_f_dms_C3() :
                      plot_ave_f_dms_C2() 
                      df3   = DataFrame(data3,columns=['Y','average_fuzzyweight_DMs_C3'])
                      df3   = df3[['Y','average_fuzzyweight_DMs_C3']].groupby('Y').sum()
                      df3.plot(kind='line',  legend=True, ax=ax2, color='c',marker='v',markersize=markersize_plot, fontsize=fontsize_plot) 

                    def plot_ave_f_dms_C4() :
                      plot_ave_f_dms_C3() 
                      df4   = DataFrame(data4,columns=['Y','average_fuzzyweight_DMs_C4'])
                      df4   = df4[['Y','average_fuzzyweight_DMs_C4']].groupby('Y').sum()
                      df4.plot(kind='line',  legend=True, ax=ax2, color='m',marker='^',markersize=markersize_plot, fontsize=fontsize_plot) 

                    def plot_ave_f_dms_C5() :
                      plot_ave_f_dms_C4() 
                      df5   = DataFrame(data5,columns=['Y','average_fuzzyweight_DMs_C5'])
                      df5   = df5[['Y','average_fuzzyweight_DMs_C5']].groupby('Y').sum()
                      df5.plot(kind='line',  legend=True, ax=ax2, color='k',marker='X',markersize=markersize_plot, fontsize=fontsize_plot) 

                    def plot_ave_f_dms_C6() :
                      plot_ave_f_dms_C5() 
                      df6   = DataFrame(data6,columns=['Y','average_fuzzyweight_DMs_C6'])
                      df6   = df6[['Y','average_fuzzyweight_DMs_C6']].groupby('Y').sum()
                      df6.plot(kind='line',  legend=True, ax=ax2, color='r',marker='D',markersize=markersize_plot, fontsize=fontsize_plot) 

                    def plot_ave_f_dms_C7() :
                      plot_ave_f_dms_C6() 
                      df7   = DataFrame(data7,columns=['Y','average_fuzzyweight_DMs_C7'])
                      df7   = df7[['Y','average_fuzzyweight_DMs_C7']].groupby('Y').sum()
                      df7.plot(kind='line',  legend=True, ax=ax2, color='y',marker='x',markersize=markersize_plot, fontsize=fontsize_plot) 

                    def plot_ave_f_dms_C8() :
                      plot_ave_f_dms_C7() 
                      df8   = DataFrame(data8,columns=['Y','average_fuzzyweight_DMs_C8'])
                      df8   = df8[['Y','average_fuzzyweight_DMs_C8']].groupby('Y').sum()
                      df8.plot(kind='line',  legend=True, ax=ax2, color='royalblue',marker='d',markersize=markersize_plot, fontsize=fontsize_plot) 

                    def plot_ave_f_dms_C9() :
                      plot_ave_f_dms_C8()
                      df9   = DataFrame(data9,columns=['Y','average_fuzzyweight_DMs_C9'])
                      df9   = df9[['Y','average_fuzzyweight_DMs_C9']].groupby('Y').sum()
                      df9.plot(kind='line',  legend=True, ax=ax2, color='limegreen',marker='p',markersize=markersize_plot, fontsize=fontsize_plot) 

                    def plot_ave_f_dms_C10() :
                      plot_ave_f_dms_C9()
                      df10  = DataFrame(data10,columns=['Y','average_fuzzyweight_DMs_C10'])
                      df10  = df10[['Y','average_fuzzyweight_DMs_C10']].groupby('Y').sum()
                      df10.plot(kind='line', legend=True, ax=ax2, color='purple',marker='1',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C11() :
                      plot_ave_f_dms_C10()
                      df11  = DataFrame(data11,columns=['Y','average_fuzzyweight_DMs_C11'])
                      df11  = df11[['Y','average_fuzzyweight_DMs_C11']].groupby('Y').sum()
                      df11.plot(kind='line', legend=True, ax=ax2, color='orangered',marker='+',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C12() :
                      plot_ave_f_dms_C11()
                      df12  = DataFrame(data12,columns=['Y','average_fuzzyweight_DMs_C12'])
                      df12  = df12[['Y','average_fuzzyweight_DMs_C12']].groupby('Y').sum()
                      df12.plot(kind='line', legend=True, ax=ax2, color='cyan',marker='2',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C13() :
                      plot_ave_f_dms_C12()
                      df13  = DataFrame(data13,columns=['Y','average_fuzzyweight_DMs_C13'])
                      df13  = df13[['Y','average_fuzzyweight_DMs_C13']].groupby('Y').sum()
                      df13.plot(kind='line', legend=True, ax=ax2, color='orange',marker='P',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C14() :
                      plot_ave_f_dms_C13()
                      df14  = DataFrame(data14,columns=['Y','average_fuzzyweight_DMs_C14'])
                      df14  = df14[['Y','average_fuzzyweight_DMs_C14']].groupby('Y').sum()
                      df14.plot(kind='line', legend=True, ax=ax2, color='slategrey',marker='4',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C15() :
                      plot_ave_f_dms_C14()
                      df15  = DataFrame(data15,columns=['Y','average_fuzzyweight_DMs_C15'])
                      df15  = df15[['Y','average_fuzzyweight_DMs_C15']].groupby('Y').sum()
                      df15.plot  (kind='line', legend=True, ax=ax2, color='crimson',marker='v',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C16() :
                      plot_ave_f_dms_C15()
                      df16  = DataFrame(data16,columns=['Y','average_fuzzyweight_DMs_C16'])
                      df16  = df16[['Y','average_fuzzyweight_DMs_C16']].groupby('Y').sum()
                      df16.plot  (kind='line', legend=True, ax=ax2, color='crimson',marker='1',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C17() :
                      plot_ave_f_dms_C16()
                      df17  = DataFrame(data17,columns=['Y','average_fuzzyweight_DMs_C17'])
                      df17  = df17[['Y','average_fuzzyweight_DMs_C17']].groupby('Y').sum()
                      df17.plot  (kind='line', legend=True, ax=ax2, color='brown',marker='p',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C18() :
                      plot_ave_f_dms_C17()
                      df18  = DataFrame(data18,columns=['Y','average_fuzzyweight_DMs_C18'])
                      df18  = df18[['Y','average_fuzzyweight_DMs_C18']].groupby('Y').sum()
                      df18.plot  (kind='line', legend=True, ax=ax2, color='blue',marker='2',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C19() :
                      plot_ave_f_dms_C18()
                      df19  = DataFrame(data19,columns=['Y','average_fuzzyweight_DMs_C19'])
                      df19  = df19[['Y','average_fuzzyweight_DMs_C19']].groupby('Y').sum()
                      df19.plot  (kind='line', legend=True, ax=ax2, color='indigo',marker='*',markersize=markersize_plot, fontsize=fontsize_plot)

                    def plot_ave_f_dms_C20() :
                      plot_ave_f_dms_C19()
                      df20  = DataFrame(data20,columns=['Y','average_fuzzyweight_DMs_C20'])
                      df20  = df20[['Y','average_fuzzyweight_DMs_C20']].groupby('Y').sum()
                      df20.plot  (kind='line', legend=True, ax=ax2, color='cadetblue',marker='3',markersize=markersize_plot, fontsize=fontsize_plot)


                    if num_val_sublv2 >  0 : 

                        figure_fuzzy_DMs_Weight_frame = plt.Figure(edgecolor="#04253a",figsize=(10,5), dpi=140,facecolor="#e5e5e5")
                        ax2 = figure_fuzzy_DMs_Weight_frame.add_subplot(111)
                        line2 = FigureCanvasTkAgg(figure_fuzzy_DMs_Weight_frame, self.figure_fuzzy_DMs_Weight_frame)
                        line2.get_tk_widget().pack() #fill=tk.BOTH)d
                        #line2.place(relx=0.01,rely=0.01)

                    def chart_fuzzzy_dm(): 

                        box = ax2.get_position()
                        ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])                
                        ax2.set_title('Membership function for average DMs weighting for criteria', fontsize=9,fontweight="bold", y=1.0, pad=15)
                        ax2.set_ylabel('Membership value', fontsize=9)
                        ax2.set_xlabel('x')
                        ax2.legend(bbox_to_anchor=[1.2, 0.5],loc='center',fontsize=5)
                        ax2.set_ylim([0, 1])
                        ax2.set_xlim([0, 1]) 
                        major_ticks = np.arange(0, 1, 0.1)
                        minor_ticks = np.arange(0, 1, 0.05)

                        ax2.set_xticks(major_ticks)
                        ax2.set_xticks(minor_ticks, minor=True)
                        ax2.set_yticks(major_ticks)
                        ax2.set_yticks(minor_ticks, minor=True)
                        ax2.grid(which='both')
                        
                     
                    if num_val_sublv2 ==  1 : 
                        plot_ave_f_dms_C1()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  2 : 
                        plot_ave_f_dms_C2()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  3 : 
                        plot_ave_f_dms_C3()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  4 : 
                        plot_ave_f_dms_C4()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 == 5 : 
                        plot_ave_f_dms_C5 ()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 == 6 : 
                        plot_ave_f_dms_C6()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  7 : 
                        plot_ave_f_dms_C7()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  8 : 
                        plot_ave_f_dms_C8()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  9 : 
                        plot_ave_f_dms_C9()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  10: 
                        plot_ave_f_dms_C10()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  11: 
                        plot_ave_f_dms_C11()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  12: 
                        plot_ave_f_dms_C12()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  13: 
                        plot_ave_f_dms_C13()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  14: 
                        plot_ave_f_dms_C14()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  15: 
                        plot_ave_f_dms_C15()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  16: 
                        plot_ave_f_dms_C16()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  17: 
                        plot_ave_f_dms_C17()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  18: 
                        plot_ave_f_dms_C18()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  19: 
                        plot_ave_f_dms_C19()
                        chart_fuzzzy_dm()
                    if num_val_sublv2 ==  20: 
                        plot_ave_f_dms_C20()
                        chart_fuzzzy_dm()

                    print('List Optimisation:')
                    print(c_optimise_setdata_list)

#===================================================================================================================



#===================================================================================================================                 
                def tab_4():  

                    self.main_frame_tab3.place_forget()     

                    self.main_frame_tab4 = Frame(self.mainwindow, 
                    height=height_of_window,
                    width=width_of_window)
                    self.main_frame_tab4.pack() 
                    self.main_frame_tab4.place(
                    relx=0.5,
                    rely=0.5,
                    anchor=CENTER) 

                    self.figure_chart_ranking_frame = LabelFrame(self.main_frame_tab4)
                    self.figure_chart_ranking_frame.pack() 
                    self.figure_chart_ranking_frame.place(
                    relx=0.5,
                    rely=0.48,
                    #rely= 0.35,
                    anchor=CENTER) 

                    def add_value_labels(ax, spacing=5):   
                        for rect in ax.patches: 
                            y_value = rect.get_height()
                            x_value = rect.get_x() + rect.get_width() / 2 
                            space = spacing 
                            va = 'bottom' 
                            if y_value < 0:
                                # Invert space to place label below
                                space *= -1
                                # Vertically align label at top
                                va = 'top' 
                            label = "{:}".format(y_value)
                            # Create annotation
                            ax.annotate(
                                label,                      # Use `label` as label
                                (x_value, y_value),         # Place label at end of the bar
                                xytext=(0, space),
                                fontsize=8,          # Vertically shift label by `space`
                                textcoords="offset points", # Interpret `xytext` as offset in points
                                ha='center',                # Horizontally center label
                                va=va)                      # Vertically align label differently for
                                                            # positive and negative values.

                    self.btnnext4 = Button(self.main_frame_tab4, text='Print', height=1, width=10)
                    self.btnback4 = Button(self.main_frame_tab4, text='Back', height=1, width=10)

                    self.btnnext4.pack()            
                    self.btnnext4.place(relx=btnnextX,rely=btnnextY, anchor=CENTER)  
                    self.btnback4.pack()            
                    self.btnback4.place(relx=btnnextX-0.05,rely=btnnextY, anchor=CENTER)      

                    if num_val_sublv2 == 0 :
                        print('no data for evaluation,')  
                    if num_val_sublv2 > 0 : 
                        if Typeofevaluation_Var.get() == 1:                                                     
                            print('no data for evaluation,')  
 
                        if Typeofevaluation_Var.get() > 1:  # == 2 :
                            print('')
                            print('Fuzzy TOPSIS and Fuzzy VIKOR module initatiated:')
                            print('')
                            FUZZY_TOPSIS_RANK=fuzzyTOPSIS_fuzzydm(num_val_sublv2,ave_dmqualitative_list,c_optimise_setdata_list)
                            print("FUZZY TOPSIS RANK    :",FUZZY_TOPSIS_RANK) 
                            FUZZY_VIKOR_RANK=fuzzyVIKOR_fuzzydm(num_val_sublv2,ave_dmqualitative_list,c_optimise_setdata_list)
                            print("FUZZY VIKOR RANK     :",FUZZY_VIKOR_RANK) 
                            values1=FUZZY_TOPSIS_RANK
                            values2=FUZZY_VIKOR_RANK
                            for num1, num2 in zip(values1, values2):
                                average_ranking.append((num1+num2)/2)    
                            rankAVERAGE= [sorted(average_ranking,reverse=False).index(x)+1 for x in average_ranking]
                            print("Average RANK   :",rankAVERAGE) 
                            print("")
                            rho_value=rho(values1, values2)
                            tau_value=tau(values1, values2)
                            print("rho value  :",rho_value) 
                            print("tau value  :",tau_value) 
                            print("")

                            data_rank = {'Material': df_alternative,'Ranking Fuzzy TOPSIS':values1,'Ranking Fuzzy VIKOR':values2, 'Average ranking':rankAVERAGE}  
                            data_rank=DataFrame(data_rank,columns=['Material','Ranking Fuzzy TOPSIS','Ranking Fuzzy VIKOR', 'Average ranking']) 

                        figureranking =  plt.Figure(edgecolor="#04253a",figsize=(10,5), dpi=140,facecolor="#e5e5e5")                                 
                        ax1 = figureranking.add_subplot(111)                            
                        bar1 = FigureCanvasTkAgg(figureranking, self.figure_chart_ranking_frame)
                        bar1.get_tk_widget().pack() 
                        data_rank.plot(kind='bar', legend=True, ax=ax1,width=0.45,color=['slategrey', 'royalblue', 'black'])
                        ax1.set_title('Material Ranking', fontsize=8,fontweight="bold", y=1.0, pad=15) 
                        ax1.legend(fontsize=5)
                        ax1.set_xlabel('Material',fontsize=6)
                        ax1.set_ylabel('Ranking',fontsize=6)
                        ax1.tick_params(axis='both', which='major', labelsize=6)
                        print(data_rank)                            
                        yLIMIT=len(df['Material'])
                        ax1.set_ylim([0, yLIMIT+3])
                        ax1.set_xticklabels(df_alternative, rotation=25, ha='right')                       
                        add_value_labels(ax1) 

                  # self.btnnext4.configure(command=tab_5)            

#=================================================================================================================== 
                    def back_3(): 
                        #forget everything in tab 4
                        # initialize tab_3
                        self.main_frame_tab4.place_forget()
                        tab_3()                                           
                    self.btnback4.configure(command=back_3)
#=================================================================================================================== 
                def back_2():
                    #forget everything in tab 3
                    # initialize tab_2
                    self.main_frame_tab3.place_forget()
                    tab_2() 
#=================================================================================================================== 
                self.main_frame_tab2.place_forget()

                if Typeofevaluation_Var.get() == 1:      
                    self.btnnext3 = Button(self.main_frame_tab3, text='Print', height=1, width=10)
                    self.btnnext3.pack()             
                    #self.btnnext3.configure(command=tab_4)           

                if Typeofevaluation_Var.get() > 1:      
                    self.btnnext3 = Button(self.main_frame_tab3, text='Next', height=1, width=10)
                    self.btnnext3.pack()             
                    self.btnnext3.configure(command=tab_4)            

                self.btnnext3.place(relx=btnnextX,rely=btnnextY, anchor=CENTER)            
                self.btnback3 = Button(self.main_frame_tab3, text='Back', height=1, width=10)
                self.btnback3.pack()            
                self.btnback3.place(relx=btnnextX-0.05,rely=btnnextY, anchor=CENTER)            
                self.btnback3.configure(command=back_2)

#===================================================================================================================

            self.btnnext2 = Button(self.main_frame_tab2, text='Next', height=1, width=10)
            self.btnback2 = Button(self.main_frame_tab2, text='Back', height=1, width=10)

            self.btnnext2.pack()            
            self.btnnext2.place(relx=btnnextX,rely=btnnextY, anchor=CENTER)            
            self.btnnext2.configure(command=tab_3)            

            self.btnback2.pack()            
            self.btnback2.place(relx=btnnextX-0.05,rely=btnnextY, anchor=CENTER)            
            #self.btnback2.configure(command=back_1)
 
            def CurSelet(evt):
                           
                values_SubCriteria_level_1 = [self.C_Listbox.get(idx) for idx in self.C_Listbox.curselection()]

                SubCriteria_level1_1=""
                SubCriteria_level1_2=""
                SubCriteria_level1_3=""
                SubCriteria_level1_4=""
                SubCriteria_level1_5=""
                SubCriteria_level1_6=""
                SubCriteria_level1_7=""
                SubCriteria_level1_8=""
                SubCriteria_level1_9=""
                SubCriteria_level1_10=""
                SubCriteria_level1_11=""

                if "Physical Properties" in values_SubCriteria_level_1:

                    SubCriteria_level1_1=['Density'
                    ,'Melting Point'
                    ,'Thermal Conductivity'
                    ,'Thermal Expansion'
                    ,'Viscosity'
                    ]

                if "Mechanical Properties" in values_SubCriteria_level_1:
        
                    SubCriteria_level1_2=['Tensile Strength'
                    ,'Shear Strength'
                    ,'Compressive Strength'
                    ,'Hardness'
                    ,'Toughness'
                    ,'Ductility'
                    ,'Elasticity'
                    ,'Impact Resistance'
                    ,'Fatigue Resistance'
                    ]


                if "Chemical Properties" in values_SubCriteria_level_1:
        
                    SubCriteria_level1_3=['Corrosion Resistance'
                    ]

                if "Manufacturing Processes" in values_SubCriteria_level_1:
        
                    SubCriteria_level1_4=['Ease of manufacturing'
                    ,'Bulk Deformation'
                    ,'Machining'
                    ,'Polymer Processing' 
                    ,'Die Casting'
                    ,'Powder Metallurgy'
                    ]


                if "Operating Condition" in values_SubCriteria_level_1:
        
                    SubCriteria_level1_5=['Operating temperature'
                    ,'Ultimate tensile strength'
                    ]

                if "Recyclability" in values_SubCriteria_level_1:
        
                    SubCriteria_level1_6=['Recyclability'
                    ,'Waste - Non hazardaus'
                    ,'Waste - Hazardaus'
                    ]

                if "Cost" in values_SubCriteria_level_1:
        
                    SubCriteria_level1_7=['Material Cost (kg/usd)'
                    ,'Indirect Material Cost'
                    ]    

                if "Quality" in values_SubCriteria_level_1:
        
                    SubCriteria_level1_8=['Material Grade'
                    ,'Supplier performace'
                    ]    

                if "SHE Risk" in values_SubCriteria_level_1:
        
                    SubCriteria_level1_9=['Hazard Rating'
                    ,'Environmental impact'
                    ,'Health & Safety impact'
                    ,'Operation disturbance'
                    ]  

                list_1=(SubCriteria_level1_1) 
                list_2=(SubCriteria_level1_2)
                list_3=(SubCriteria_level1_3)
                list_4=(SubCriteria_level1_4)
                list_5=(SubCriteria_level1_5)
                list_6=(SubCriteria_level1_6)
                list_7=(SubCriteria_level1_7)
                list_8=(SubCriteria_level1_8)
                list_9=(SubCriteria_level1_9) 

                list_all=[list_1,list_2,list_3,list_4,list_5,list_6,list_7,list_8,list_9]       

                self.C_Listbox2.delete(0, END)
       
                for i in list_all:

                    self.C_Listbox2.insert('end', *i)

                self.scrollbarY = Scrollbar(self.C_Listbox2, orient = VERTICAL)
                self.C_Listbox2.config(yscrollcommand = self.scrollbarY.set)
                self.scrollbarY.config(command= self.C_Listbox2.yview )
                self.scrollbarY.pack()
                self.scrollbarY.place(relx=1,rely=0.0, height=305 ,anchor=NE)
                flat_list_SubCriteria_level_1 = []
                for sublist in list_all:
                    for item in sublist:
                        flat_list_SubCriteria_level_1.append(item) 
 
            self.C_Listbox.bind('<<ListboxSelect>>',CurSelet)
            self.C_Listbox.place(relx=0.22,rely=0.35,anchor=NW)     
             
            self.C_Listbox2=Listbox(self.infodetail_frame,height=height_listbox , width = 40, selectmode=MULTIPLE , exportselection=False)    
            self.C_Listbox2.pack()  
            self.C_Listbox2.place(relx=0.53,rely=0.35,anchor=NW)           

            gap_x=0.12  ####
            gap_x_from_border=0.33 ###     

            label_criteria_tab2_y=0.038
            label_criteria_tab2_y_gap=0.043

            label_criteria_tab2_x= 0.05 
            dmbox_criteria_tab2_y=0 
            gapboxdm_fromtop=label_criteria_tab2_y
            gap_y_dmweight=label_criteria_tab2_y_gap

            sizefont=10

            criteria_dm_9_point=[0,1,2,3,4,5,6,7,8,9,10]
            criteria_dm__point=criteria_dm_9_point
 
            input_dm_combobox_definitioncriteriaweighting_frame=self.criteriaweighting_frame
            input_dm_combobox_definition_criteria_dm__point=criteria_dm__point
    
            dm1_c1 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4) 
            #else:                
            #    dm1_c1  = Entry(self.criteriaweighting_frame,width=4,bd=1) 

            dm1_c2  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c3  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c4  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c5  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c6  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c7  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c8  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c9  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c10 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c11 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c12 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c13 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c14 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c15 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c16 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c17 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c18 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c19 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm1_c20 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c1  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c2  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c3  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c4  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c5  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c6  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c7  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c8  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c9  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c10 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c11 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c12 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c13 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c14 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c15 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c16 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c17 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c18 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c19 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm2_c20 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c1  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c2  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c3  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c4  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c5  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c6  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c7  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c8  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c9  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c10 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c11 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c12 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c13 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c14 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c15 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c16 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c17 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c18 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c19 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm3_c20 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c1  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c2  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c3  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c4  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c5  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c6  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c7  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c8  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c9  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c10 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c11 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c12 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c13 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c14 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c15 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c16 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c17 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c18 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c19 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm4_c20 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c1  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c2  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c3  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c4  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c5  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c6  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c7  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c8  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c9  = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c10 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c11 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c12 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c13 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c14 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c15 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4) 
            dm5_c16 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c17 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c18 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c19 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)
            dm5_c20 = ttk.Combobox(self.criteriaweighting_frame,values=criteria_dm__point, width = 4)

            Typeofevaluation_Var_input=Typeofevaluation_Var.get()

            dm_initial_set(Typeofevaluation_Var_input,
            dm1_c1,dm1_c2 ,dm1_c3 ,dm1_c4 ,dm1_c5 ,dm1_c6 ,dm1_c7 ,dm1_c8 ,dm1_c9 ,dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20,  
            dm2_c1,dm2_c2 ,dm2_c3 ,dm2_c4 ,dm2_c5 ,dm2_c6 ,dm2_c7 ,dm2_c8 ,dm2_c9 ,dm2_c10,dm2_c11,dm2_c12,dm2_c13,dm2_c14,dm2_c15,dm2_c16,dm2_c17,dm2_c18,dm2_c19,dm2_c20,  
            dm3_c1,dm3_c2 ,dm3_c3 ,dm3_c4 ,dm3_c5 ,dm3_c6 ,dm3_c7 ,dm3_c8 ,dm3_c9 ,dm3_c10,dm3_c11,dm3_c12,dm3_c13,dm3_c14,dm3_c15,dm3_c16,dm3_c17,dm3_c18,dm3_c19,dm3_c20,  
            dm4_c1,dm4_c2 ,dm4_c3 ,dm4_c4 ,dm4_c5 ,dm4_c6 ,dm4_c7 ,dm4_c8 ,dm4_c9 ,dm4_c10,dm4_c11,dm4_c12,dm4_c13,dm4_c14,dm4_c15,dm4_c16,dm4_c17,dm4_c18,dm4_c19,dm4_c20,  
            dm5_c1,dm5_c2 ,dm5_c3 ,dm5_c4 ,dm5_c5 ,dm5_c6 ,dm5_c7 ,dm5_c8 ,dm5_c9 ,dm5_c10,dm5_c11,dm5_c12,dm5_c13,dm5_c14,dm5_c15,dm5_c16,dm5_c17,dm5_c18,dm5_c19,dm5_c20)    

            criteria_optimise_list=['Max','Min'] 

            c1_optimise   = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c2_optimise   = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c3_optimise   = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c4_optimise   = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c5_optimise   = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c6_optimise   = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c7_optimise   = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c8_optimise   = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c9_optimise   = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c10_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c11_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c12_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c13_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c14_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c15_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c16_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c17_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c18_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c19_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6)
            c20_optimise  = ttk.Combobox(self.criteria_optimization,values=criteria_optimise_list, width = 6) 

            c_optimise_set (c1_optimise ,c2_optimise ,c3_optimise ,c4_optimise ,c5_optimise ,c6_optimise ,c7_optimise ,c8_optimise ,c9_optimise ,c10_optimise,c11_optimise,
            c12_optimise,c13_optimise,c14_optimise,c15_optimise,c16_optimise,c17_optimise,c18_optimise,c19_optimise,c20_optimise)

            self.label_subcriteria_0_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_1_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_2_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_3_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_4_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_5_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_6_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_7_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_8_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_9_level_2     =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_10_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_11_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_12_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_13_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_14_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_15_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_16_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_17_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_18_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_19_level_2    =   Label(self.criteriaweighting_frame)
            self.label_subcriteria_20_level_2    =   Label(self.criteriaweighting_frame)

            self.label_subcriteria_0_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_1_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_2_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_3_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_4_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_5_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_6_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_7_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_8_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_9_level_2_optimise     =Label(self.criteria_optimization)
            self.label_subcriteria_10_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_11_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_12_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_13_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_14_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_15_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_16_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_17_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_18_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_19_level_2_optimise    =Label(self.criteria_optimization)
            self.label_subcriteria_20_level_2_optimise    =Label(self.criteria_optimization)

            def forget_place_item_DM_Criteria():

                self.label_subcriteria_0_level_2.place_forget()
                self.label_subcriteria_1_level_2.place_forget()
                self.label_subcriteria_2_level_2.place_forget()
                self.label_subcriteria_3_level_2.place_forget()
                self.label_subcriteria_4_level_2.place_forget()
                self.label_subcriteria_5_level_2.place_forget()
                self.label_subcriteria_6_level_2.place_forget()
                self.label_subcriteria_7_level_2.place_forget()
                self.label_subcriteria_8_level_2.place_forget()
                self.label_subcriteria_9_level_2.place_forget()
                self.label_subcriteria_10_level_2.place_forget()
                self.label_subcriteria_11_level_2.place_forget()
                self.label_subcriteria_12_level_2.place_forget()
                self.label_subcriteria_13_level_2.place_forget()
                self.label_subcriteria_14_level_2.place_forget()
                self.label_subcriteria_15_level_2.place_forget()
                self.label_subcriteria_16_level_2.place_forget()
                self.label_subcriteria_17_level_2.place_forget()
                self.label_subcriteria_18_level_2.place_forget()
                self.label_subcriteria_19_level_2.place_forget()
                self.label_subcriteria_20_level_2.place_forget()

                self.label_subcriteria_0_level_2_optimise.place_forget()
                self.label_subcriteria_1_level_2_optimise.place_forget()
                self.label_subcriteria_2_level_2_optimise.place_forget()
                self.label_subcriteria_3_level_2_optimise.place_forget()
                self.label_subcriteria_4_level_2_optimise.place_forget()
                self.label_subcriteria_5_level_2_optimise.place_forget()
                self.label_subcriteria_6_level_2_optimise.place_forget()
                self.label_subcriteria_7_level_2_optimise.place_forget()
                self.label_subcriteria_8_level_2_optimise.place_forget()
                self.label_subcriteria_9_level_2_optimise.place_forget()
                self.label_subcriteria_10_level_2_optimise.place_forget()
                self.label_subcriteria_11_level_2_optimise.place_forget()
                self.label_subcriteria_12_level_2_optimise.place_forget()
                self.label_subcriteria_13_level_2_optimise.place_forget()
                self.label_subcriteria_14_level_2_optimise.place_forget()
                self.label_subcriteria_15_level_2_optimise.place_forget()
                self.label_subcriteria_16_level_2_optimise.place_forget()
                self.label_subcriteria_17_level_2_optimise.place_forget()
                self.label_subcriteria_18_level_2_optimise.place_forget()
                self.label_subcriteria_19_level_2_optimise.place_forget()
                self.label_subcriteria_20_level_2_optimise.place_forget()

                dm_place_forget_all(
                dm1_c1,dm1_c2 ,dm1_c3 ,dm1_c4 ,dm1_c5 ,dm1_c6 ,dm1_c7 ,dm1_c8 ,dm1_c9 ,dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20,  
                dm2_c1,dm2_c2 ,dm2_c3 ,dm2_c4 ,dm2_c5 ,dm2_c6 ,dm2_c7 ,dm2_c8 ,dm2_c9 ,dm2_c10,dm2_c11,dm2_c12,dm2_c13,dm2_c14,dm2_c15,dm2_c16,dm2_c17,dm2_c18,dm2_c19,dm2_c20,  
                dm3_c1,dm3_c2 ,dm3_c3 ,dm3_c4 ,dm3_c5 ,dm3_c6 ,dm3_c7 ,dm3_c8 ,dm3_c9 ,dm3_c10,dm3_c11,dm3_c12,dm3_c13,dm3_c14,dm3_c15,dm3_c16,dm3_c17,dm3_c18,dm3_c19,dm3_c20,  
                dm4_c1,dm4_c2 ,dm4_c3 ,dm4_c4 ,dm4_c5 ,dm4_c6 ,dm4_c7 ,dm4_c8 ,dm4_c9 ,dm4_c10,dm4_c11,dm4_c12,dm4_c13,dm4_c14,dm4_c15,dm4_c16,dm4_c17,dm4_c18,dm4_c19,dm4_c20,  
                dm5_c1,dm5_c2 ,dm5_c3 ,dm5_c4 ,dm5_c5 ,dm5_c6 ,dm5_c7 ,dm5_c8 ,dm5_c9 ,dm5_c10,dm5_c11,dm5_c12,dm5_c13,dm5_c14,dm5_c15,dm5_c16,dm5_c17,dm5_c18,dm5_c19,dm5_c20)     
                   
                c_optimise_set_forget_all (c1_optimise ,c2_optimise ,c3_optimise ,c4_optimise ,c5_optimise ,c6_optimise ,c7_optimise ,c8_optimise ,c9_optimise ,c10_optimise,c11_optimise,
                c12_optimise,c13_optimise,c14_optimise,c15_optimise,c16_optimise,c17_optimise,c18_optimise,c19_optimise,c20_optimise)

            def populate_dm_weighting_frame():

                forget_place_item_DM_Criteria()


                self.values_SubCriteria_level_2 = [self.C_Listbox2.get(idx) for idx in self.C_Listbox2.curselection()]         
                num_val_sublv2 = len(self.values_SubCriteria_level_2) 
 
                def num_val_sublv2_1():  

                    self.label_subcriteria_0_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[0]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_0_level_2.pack()

                    self.label_subcriteria_0_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*0,
                    anchor=NW)

                    self.label_subcriteria_0_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[0]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_0_level_2_optimise .pack()

                    self.label_subcriteria_0_level_2_optimise .place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*0,
                    anchor=NW)

                    c1_optimise.pack() 
                    c1_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*0,
                    anchor=NW)

                def num_val_sublv2_2():      

                    num_val_sublv2_1() 
                     

                    self.label_subcriteria_1_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[1]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_1_level_2.pack()

                    self.label_subcriteria_1_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*1,
                    anchor=NW)

                    self.label_subcriteria_1_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[1]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_1_level_2_optimise.pack()

                    self.label_subcriteria_1_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*1,
                    anchor=NW)

                    c2_optimise.pack()
                    c2_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*1,
                    anchor=NW)

                def num_val_sublv2_3():    

                    num_val_sublv2_2() 

                    self.label_subcriteria_2_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[2]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_2_level_2.pack()

                    self.label_subcriteria_2_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*2,
                    anchor=NW)

                    self.label_subcriteria_2_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[2]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_2_level_2_optimise.pack()

                    self.label_subcriteria_2_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*2,
                    anchor=NW)

                    c3_optimise.pack()
                    c3_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*2,
                    anchor=NW)

                def num_val_sublv2_4():          

                    num_val_sublv2_3()   

                    self.label_subcriteria_3_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[3]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_3_level_2.pack()

                    self.label_subcriteria_3_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*3,
                    anchor=NW)

                    self.label_subcriteria_3_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[3]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_3_level_2_optimise.pack()

                    self.label_subcriteria_3_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*3,
                    anchor=NW)

                    c4_optimise.pack()
                    c4_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*3,
                    anchor=NW)
                def num_val_sublv2_5():     

                    num_val_sublv2_4()  

                    self.label_subcriteria_4_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[4]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_4_level_2.pack()

                    self.label_subcriteria_4_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*4,
                    anchor=NW)

                    self.label_subcriteria_4_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[4]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_4_level_2_optimise.pack()

                    self.label_subcriteria_4_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*4,
                    anchor=NW)

                    c5_optimise.pack()
                    c5_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*4,
                    anchor=NW)

                def num_val_sublv2_6():         

                    num_val_sublv2_5()    

                    self.label_subcriteria_5_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[5]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_5_level_2.pack()

                    self.label_subcriteria_5_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*5,
                    anchor=NW)

                    self.label_subcriteria_5_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[5]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_5_level_2_optimise.pack()

                    self.label_subcriteria_5_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*5,
                    anchor=NW)


                    c6_optimise.pack()
                    c6_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*5,
                    anchor=NW)
                def num_val_sublv2_7():   

                    num_val_sublv2_6()

                    self.label_subcriteria_6_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[6]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_6_level_2.pack()

                    self.label_subcriteria_6_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*6,
                    anchor=NW)

                    self.label_subcriteria_6_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[6]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_6_level_2_optimise.pack()

                    self.label_subcriteria_6_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*6,
                    anchor=NW)

                    c7_optimise.pack()
                    c7_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*6,
                    anchor=NW)
                def num_val_sublv2_8():   

                    num_val_sublv2_7()

                    self.label_subcriteria_7_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[7]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_7_level_2.pack()

                    self.label_subcriteria_7_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*7,
                    anchor=NW)

                    self.label_subcriteria_7_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[7]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_7_level_2_optimise.pack()

                    self.label_subcriteria_7_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*7,
                    anchor=NW)

                    c8_optimise.pack()
                    c8_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*7,
                    anchor=NW)

                def num_val_sublv2_9():    

                    num_val_sublv2_8()

                    self.label_subcriteria_8_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[8]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_8_level_2.pack()

                    self.label_subcriteria_8_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*8,
                    anchor=NW)


                    self.label_subcriteria_8_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[8]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_8_level_2_optimise.pack()

                    self.label_subcriteria_8_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*8,
                    anchor=NW)


                    c9_optimise.pack()
                    c9_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*8,
                    anchor=NW)
                def num_val_sublv2_10():   

                    num_val_sublv2_9()

                    self.label_subcriteria_9_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[9]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_9_level_2.pack()

                    self.label_subcriteria_9_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*9,
                    anchor=NW)

                    self.label_subcriteria_9_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[9]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_9_level_2_optimise.pack()

                    self.label_subcriteria_9_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*9,
                    anchor=NW)

                    c10_optimise.pack() 
                    c10_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*9,
                    anchor=NW)

                def num_val_sublv2_11():           

                    num_val_sublv2_10()

                    self.label_subcriteria_10_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[10]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_10_level_2.pack()

                    self.label_subcriteria_10_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*10,
                    anchor=NW)

                    self.label_subcriteria_10_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[10]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_10_level_2_optimise.pack()

                    self.label_subcriteria_10_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*10,
                    anchor=NW)

                    c11_optimise.pack() 
                    c11_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*10,
                    anchor=NW)

                def num_val_sublv2_12():

                    num_val_sublv2_11()

                    self.label_subcriteria_11_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[11]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_11_level_2.pack()

                    self.label_subcriteria_11_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*11,
                    anchor=NW)

                    self.label_subcriteria_11_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[11]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_11_level_2_optimise.pack()

                    self.label_subcriteria_11_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*11,
                    anchor=NW)

                    c12_optimise.pack() 
                    c12_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*11,
                    anchor=NW)

                def num_val_sublv2_13():  

                    num_val_sublv2_12() 

                    self.label_subcriteria_12_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[12]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_12_level_2.pack()

                    self.label_subcriteria_12_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*12,
                    anchor=NW)

                    self.label_subcriteria_12_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[12]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_12_level_2_optimise.pack()

                    self.label_subcriteria_12_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*12,
                    anchor=NW)

                    c13_optimise.pack() 
                    c13_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*12,
                    anchor=NW)

                def num_val_sublv2_14():      

                    num_val_sublv2_13()

                    self.label_subcriteria_13_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[13]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_13_level_2.pack()

                    self.label_subcriteria_13_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*13,
                    anchor=NW)

                    self.label_subcriteria_13_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[13]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_13_level_2_optimise.pack()

                    self.label_subcriteria_13_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*13,
                    anchor=NW)

                    c14_optimise.pack() 
                    c14_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*13,
                    anchor=NW)

                def num_val_sublv2_15():         

                    num_val_sublv2_14()

                    self.label_subcriteria_14_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[14]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_14_level_2.pack()

                    self.label_subcriteria_14_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*14,
                    anchor=NW)

                    self.label_subcriteria_14_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[14]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_14_level_2_optimise.pack()

                    self.label_subcriteria_14_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*14,
                    anchor=NW)

                    c15_optimise.pack() 
                    c15_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*14,
                    anchor=NW)

                def num_val_sublv2_16():         

                    num_val_sublv2_15()

                    self.label_subcriteria_15_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[15]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_15_level_2.pack()

                    self.label_subcriteria_15_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*15,
                    anchor=NW)

                    self.label_subcriteria_15_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[15]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_15_level_2_optimise.pack()

                    self.label_subcriteria_15_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*15,
                    anchor=NW)

                    c16_optimise.pack() 
                    c16_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*15,
                    anchor=NW)

                def num_val_sublv2_17():         

                    num_val_sublv2_16()

                    self.label_subcriteria_16_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[16]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_16_level_2.pack()

                    self.label_subcriteria_16_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*16,
                    anchor=NW)

                    self.label_subcriteria_16_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[16]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_16_level_2_optimise.pack()

                    self.label_subcriteria_16_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*16,
                    anchor=NW)

                    c17_optimise.pack() 
                    c17_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*16,
                    anchor=NW)

                def num_val_sublv2_18():         

                    num_val_sublv2_17()

                    self.label_subcriteria_17_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[17]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_17_level_2.pack()

                    self.label_subcriteria_17_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*17,
                    anchor=NW)

                    self.label_subcriteria_17_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[17]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_17_level_2_optimise.pack()

                    self.label_subcriteria_17_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*17,
                    anchor=NW)

                    c18_optimise.pack() 
                    c18_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*17,
                    anchor=NW)
                def num_val_sublv2_19():         

                    num_val_sublv2_18()

                    self.label_subcriteria_18_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[18]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_18_level_2.pack()

                    self.label_subcriteria_18_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*18,
                    anchor=NW)

                    self.label_subcriteria_18_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[18]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_18_level_2_optimise.pack()

                    self.label_subcriteria_18_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*18,
                    anchor=NW)

                    c19_optimise.pack() 
                    c19_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*18,                    
                    anchor=NW)

                def num_val_sublv2_20():         

                    num_val_sublv2_19()

                    self.label_subcriteria_19_level_2    =   Label(self.criteriaweighting_frame, 
                    text=self.values_SubCriteria_level_2[19]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_19_level_2.pack()

                    self.label_subcriteria_19_level_2.place(
                    relx=label_criteria_tab2_x,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*19,
                    anchor=NW)

                    self.label_subcriteria_19_level_2_optimise    =   Label(self.criteria_optimization, 
                    text=self.values_SubCriteria_level_2[19]  , font=("Helvetica",sizefont,"bold") )
                    self.label_subcriteria_19_level_2_optimise.pack()

                    self.label_subcriteria_19_level_2_optimise.place(
                    relx=label_criteria_tab2_x+0.01,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*19,
                    anchor=NW)

                    c20_optimise.pack() 
                    c20_optimise .place(
                    relx=label_criteria_tab2_x+0.01+0.6,
                    rely=label_criteria_tab2_y+label_criteria_tab2_y_gap*19,
                    anchor=NW)
 
                def dm_option_input_1():

                    if self.dm_selection.get() == "1":
                        dm1_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm1_c1,dm1_c2,dm1_c3,dm1_c4,dm1_c5,dm1_c6,dm1_c7,dm1_c8,dm1_c9,
                        dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20)
 
                def dm_option_input_2():

                    if self.dm_selection.get() == "2":

                        dm1_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm1_c1,dm1_c2,dm1_c3,dm1_c4,dm1_c5,dm1_c6,dm1_c7,dm1_c8,dm1_c9,
                        dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20)

                        dm2_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm2_c1,dm2_c2,dm2_c3,dm2_c4,dm2_c5,dm2_c6,dm2_c7,dm2_c8,dm2_c9,
                        dm2_c10,dm2_c11,dm2_c12,dm2_c13,dm2_c14,dm2_c15,dm2_c16,dm2_c17,dm2_c18,dm2_c19,dm2_c20)            

                def dm_option_input_3():

                    if self.dm_selection.get() == "3":

                        dm1_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm1_c1,dm1_c2,dm1_c3,dm1_c4,dm1_c5,dm1_c6,dm1_c7,dm1_c8,dm1_c9,
                        dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20)

                        dm2_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm2_c1,dm2_c2,dm2_c3,dm2_c4,dm2_c5,dm2_c6,dm2_c7,dm2_c8,dm2_c9,
                        dm2_c10,dm2_c11,dm2_c12,dm2_c13,dm2_c14,dm2_c15,dm2_c16,dm2_c17,dm2_c18,dm2_c19,dm2_c20)               

                        dm3_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm3_c1,dm3_c2,dm3_c3,dm3_c4,dm3_c5,dm3_c6,dm3_c7,dm3_c8,dm3_c9,
                        dm3_c10,dm3_c11,dm3_c12,dm3_c13,dm3_c14,dm3_c15,dm3_c16,dm3_c17,dm3_c18,dm3_c19,dm3_c20)

                def dm_option_input_4():

                    if self.dm_selection.get() == "4":

                        dm1_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm1_c1,dm1_c2,dm1_c3,dm1_c4,dm1_c5,dm1_c6,dm1_c7,dm1_c8,dm1_c9,
                        dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20)

                        dm2_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm2_c1,dm2_c2,dm2_c3,dm2_c4,dm2_c5,dm2_c6,dm2_c7,dm2_c8,dm2_c9,
                        dm2_c10,dm2_c11,dm2_c12,dm2_c13,dm2_c14,dm2_c15,dm2_c16,dm2_c17,dm2_c18,dm2_c19,dm2_c20)               

                        dm3_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm3_c1,dm3_c2,dm3_c3,dm3_c4,dm3_c5,dm3_c6,dm3_c7,dm3_c8,dm3_c9,
                        dm3_c10,dm3_c11,dm3_c12,dm3_c13,dm3_c14,dm3_c15,dm3_c16,dm3_c17,dm3_c18,dm3_c19,dm3_c20)

                        dm4_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm4_c1,dm4_c2,dm4_c3,dm4_c4,dm4_c5,dm4_c6,dm4_c7,dm4_c8,dm4_c9,
                        dm4_c10,dm4_c11,dm4_c12,dm4_c13,dm4_c14,dm4_c15,dm4_c16,dm4_c17,dm4_c18,dm4_c19,dm4_c20)

                def dm_option_input_5():

                    if self.dm_selection.get() == "5":

                        dm1_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm1_c1,dm1_c2,dm1_c3,dm1_c4,dm1_c5,dm1_c6,dm1_c7,dm1_c8,dm1_c9,
                        dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20)

                        dm2_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm2_c1,dm2_c2,dm2_c3,dm2_c4,dm2_c5,dm2_c6,dm2_c7,dm2_c8,dm2_c9,
                        dm2_c10,dm2_c11,dm2_c12,dm2_c13,dm2_c14,dm2_c15,dm2_c16,dm2_c17,dm2_c18,dm2_c19,dm2_c20)               

                        dm3_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm3_c1,dm3_c2,dm3_c3,dm3_c4,dm3_c5,dm3_c6,dm3_c7,dm3_c8,dm3_c9,
                        dm3_c10,dm3_c11,dm3_c12,dm3_c13,dm3_c14,dm3_c15,dm3_c16,dm3_c17,dm3_c18,dm3_c19,dm3_c20)

                        dm4_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm4_c1,dm4_c2,dm4_c3,dm4_c4,dm4_c5,dm4_c6,dm4_c7,dm4_c8,dm4_c9,
                        dm4_c10,dm4_c11,dm4_c12,dm4_c13,dm4_c14,dm4_c15,dm4_c16,dm4_c17,dm4_c18,dm4_c19,dm4_c20)

                        dm5_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
                        dm5_c1,dm5_c2,dm5_c3,dm5_c4,dm5_c5,dm5_c6,dm5_c7,dm5_c8,dm5_c9,
                        dm5_c10,dm5_c11,dm5_c12,dm5_c13,dm5_c14,dm5_c15,dm5_c16,dm5_c17,dm5_c18,dm5_c19,dm5_c20)

                if num_val_sublv2 == 1:
                    num_val_sublv2_1()

                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5()   

                if num_val_sublv2 == 2:
                    num_val_sublv2_2()

                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 3:
                    num_val_sublv2_3() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 4:
                    num_val_sublv2_4() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 5:
                    num_val_sublv2_5() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 6:
                    num_val_sublv2_6() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 7:
                    num_val_sublv2_7() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 8:
                    num_val_sublv2_8() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 9:
                    num_val_sublv2_9() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5()  
                    
                if num_val_sublv2 == 10:
                    num_val_sublv2_10() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 11:
                    num_val_sublv2_11() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 12:
                    num_val_sublv2_12() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5()  
                    
                if num_val_sublv2 == 13:
                    num_val_sublv2_13() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5()   
                    
                if num_val_sublv2 == 14:
                    num_val_sublv2_14() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5()  
                    
                if num_val_sublv2 == 15:
                    num_val_sublv2_15() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 

                if num_val_sublv2 == 16:
                    num_val_sublv2_16() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 
                    
                if num_val_sublv2 == 17:
                    num_val_sublv2_17() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5()  
                    
                if num_val_sublv2 == 18:
                    num_val_sublv2_18() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5()   
                    
                if num_val_sublv2 == 19:
                    num_val_sublv2_19() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5()  
                    
                if num_val_sublv2 == 20:
                    num_val_sublv2_20() 
                    dm_option_input_1() 
                    dm_option_input_2() 
                    dm_option_input_3() 
                    dm_option_input_4() 
                    dm_option_input_5() 

            global num_val_sublv2
            num_val_sublv2=StringVar()

            self.btnclear_dmweighting = Button(self.criteriaweighting_frame, text='<<', height=1, width=3)
            self.btnnext_dmweighting = Button(self.infodetail_frame, text='>>', height=1, width=3)

            self.btnclear_dmweighting.pack()
            self.btnnext_dmweighting.pack()

            self.btnnext_dmweighting.place(relx=0.9,rely=0.95,anchor=NW)   
            self.btnclear_dmweighting.place(relx=0.04,rely=0.95,anchor=NW)         

            self.btnclear_dmweighting.configure(command=forget_place_item_DM_Criteria)
            self.btnnext_dmweighting.configure(command=populate_dm_weighting_frame)

#===================================================================================================================         
        self.btnnext1.configure(command=tab_2) 
#===================================================================================================================           
mainwindow = Tk()
application = app(mainwindow)
mainwindow.mainloop()  