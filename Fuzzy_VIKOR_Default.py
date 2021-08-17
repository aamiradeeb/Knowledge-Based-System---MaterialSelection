
import numpy as np 
import sqlite3
import pandas as pd
import warnings
import copy

from pandas import DataFrame 
import matplotlib.pyplot as plt                                             #   Plot Chart
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg             #   Plot Chart


warnings.filterwarnings('error') 
strategy_coefficient=0.5
#def fuzzyTOPSIS_fuzzydm(num_val_sublv2,weight_matrix_dm,matrix_array_optimisation_C):
num_val_sublv2=3
#weight_matrix_dm =['Max','Max']
#matrix_array_optimisation_C=['Max','Max']   

weight_matrix_dm = list([
          [ (  0.1,   0.1,   0.1), (  0.1,   0.1,   0.1), (  0.1,   0.1,   0.1) ]    
    ])


matrix_array_optimisation_C = ['Max', 'Max', 'Max']


con=sqlite3.connect("materialdatabase.db") 

if num_val_sublv2 == 1 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1  
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 2 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 3 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 4 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 5 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 6 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6  
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 7 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 8 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 9 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 10 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 11 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 12 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11, CRITERIA_12 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 13 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11, CRITERIA_12, CRITERIA_13 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 14 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 15 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 16 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
         CRITERIA_16  
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 17 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
         CRITERIA_16 , CRITERIA_17 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 18 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
         CRITERIA_16 , CRITERIA_17, CRITERIA_18 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 19 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
         CRITERIA_16 , CRITERIA_17, CRITERIA_18, CRITERIA_19 
         FROM Material_database_FuzzyWeight""",con)
if num_val_sublv2 == 20 :
    df=pd.read_sql("""SELECT Material, 
        CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
        CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
        CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
         CRITERIA_16 , CRITERIA_17, CRITERIA_18, CRITERIA_19, CRITERIA_20 
         FROM Material_database_FuzzyWeight""",con) 

arr = df.to_numpy() 
rowdatabase=len(df)

def column(matrix, i):
    return [row[i] for row in matrix]

if num_val_sublv2 == 1 :
    column1=column(arr,1)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x])
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 2 :
    column1=column(arr,1)
    column2=column(arr,2) 
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x])
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 3 :
    column1=np.array(column(arr,1))
    column2=np.array(column(arr,2))
    column3=np.array(column(arr,3))
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]) 
        ]) 
        database.append(databaselist)
        x += 1  

if num_val_sublv2 == 4 :
    column1=np.array(column(arr,1))
    column2=np.array(column(arr,2))
    column3=np.array(column(arr,3))
    column4=np.array(column(arr,4))

    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):

        databaselist =(
        [(column1[x],column1[x],column1[x]),
         (column2[x],column2[x],column2[x]),
         (column3[x],column3[x],column3[x]),
         (column4[x],column4[x],column4[x])         
        ]) 
        database.append(databaselist)
        x += 1 


if num_val_sublv2 == 5 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]) 
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 6 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]) 
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 7 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]) 
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 8 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x])  
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 9 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x])   
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 10 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x])  
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 11 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x])  
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 12 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    column12=column(arr,12)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x]),
         (column12[x],column12[x],column12[x])    
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 13 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    column12=column(arr,12)
    column13=column(arr,13) 
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x]),
         (column12[x],column12[x],column12[x]),
         (column13[x],column13[x],column13[x])  
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 14 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    column12=column(arr,12)
    column13=column(arr,13)  
    column14=column(arr,14)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x]),
         (column12[x],column12[x],column12[x]),
         (column13[x],column13[x],column13[x]),
         (column14[x],column14[x],column14[x])  
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 15 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    column12=column(arr,12)
    column13=column(arr,13)  
    column14=column(arr,14)
    column15=column(arr,15)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x]),
         (column12[x],column12[x],column12[x]),
         (column13[x],column13[x],column13[x]),
         (column14[x],column14[x],column14[x]),
         (column15[x],column15[x],column15[x])  
        ]) 
        database.append(databaselist)
        x += 1  

if num_val_sublv2 == 16 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    column12=column(arr,12)
    column13=column(arr,13)  
    column14=column(arr,14)
    column15=column(arr,15)
    column16=column(arr,16)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x]),
         (column12[x],column12[x],column12[x]),
         (column13[x],column13[x],column13[x]),
         (column14[x],column14[x],column14[x]),
         (column15[x],column15[x],column15[x]),
         (column16[x],column16[x],column16[x])   
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 17 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    column12=column(arr,12)
    column13=column(arr,13)  
    column14=column(arr,14)
    column15=column(arr,15)
    column16=column(arr,16)  
    column17=column(arr,17)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x]),
         (column12[x],column12[x],column12[x]),
         (column13[x],column13[x],column13[x]),
         (column14[x],column14[x],column14[x]),
         (column15[x],column15[x],column15[x]),
         (column16[x],column16[x],column16[x]),
         (column17[x],column17[x],column17[x])  
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 18 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    column12=column(arr,12)
    column13=column(arr,13)  
    column14=column(arr,14)
    column15=column(arr,15)
    column16=column(arr,16)  
    column17=column(arr,17)
    column18=column(arr,18)
    
    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x]),
         (column12[x],column12[x],column12[x]),
         (column13[x],column13[x],column13[x]),
         (column14[x],column14[x],column14[x]),
         (column15[x],column15[x],column15[x]),
         (column16[x],column16[x],column16[x]),
         (column17[x],column17[x],column17[x]),
         (column18[x],column18[x],column18[x])  
        ]) 
        database.append(databaselist)
        x += 1 

if num_val_sublv2 == 19 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    column12=column(arr,12)
    column13=column(arr,13)  
    column14=column(arr,14)
    column15=column(arr,15)
    column16=column(arr,16)  
    column17=column(arr,17)
    column18=column(arr,18)
    column19=column(arr,19)  

    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x]),
         (column12[x],column12[x],column12[x]),
         (column13[x],column13[x],column13[x]),
         (column14[x],column14[x],column14[x]),
         (column15[x],column15[x],column15[x]),
         (column16[x],column16[x],column16[x]),
         (column17[x],column17[x],column17[x]),
         (column18[x],column18[x],column18[x]),
         (column19[x],column19[x],column19[x])  
        ]) 
        database.append(databaselist)
        x += 1     

if num_val_sublv2 == 20 :
    column1=column(arr,1)
    column2=column(arr,2)
    column3=column(arr,3)
    column4=column(arr,4)
    column5=column(arr,5)
    column6=column(arr,6)
    column7=column(arr,7)  
    column8=column(arr,8)
    column9=column(arr,9)
    column10=column(arr,10)  
    column11=column(arr,11)
    column12=column(arr,12)
    column13=column(arr,13)  
    column14=column(arr,14)
    column15=column(arr,15)
    column16=column(arr,16)  
    column17=column(arr,17)
    column18=column(arr,18)
    column19=column(arr,19)  
    column20=column(arr,20)   

    database = []
    databaselist =[]
    x = 0
    while len(database) < (rowdatabase):
        databaselist =(
        [(column1 [x],column1 [x],column1 [x]),
         (column2 [x],column2 [x],column2 [x]),
         (column3 [x],column3 [x],column3 [x]),
         (column4 [x],column4 [x],column4 [x]),
         (column5 [x],column5 [x],column5 [x]),
         (column6 [x],column6 [x],column6 [x]),
         (column7 [x],column7 [x],column7 [x]),
         (column8 [x],column8 [x],column8 [x]),
         (column9 [x],column9 [x],column9 [x]),
         (column10[x],column10[x],column10[x]),
         (column11[x],column11[x],column11[x]),
         (column12[x],column12[x],column12[x]),
         (column13[x],column13[x],column13[x]),
         (column14[x],column14[x],column14[x]),
         (column15[x],column15[x],column15[x]),
         (column16[x],column16[x],column16[x]),
         (column17[x],column17[x],column17[x]),
         (column18[x],column18[x],column18[x]),
         (column19[x],column19[x],column19[x]),
         (column20[x],column20[x],column20[x])
        ]) 
        database.append(databaselist)
        x += 1  

 


# Function: VIKOR
def fuzzy_vikor_method(dataset, weights, criterion_type, strategy_coefficient = 0.5):
    dataset_A  = np.zeros((len(dataset), len(dataset[0]) ))
    dataset_B  = np.zeros((len(dataset), len(dataset[0]) ))
    dataset_C  = np.zeros((len(dataset), len(dataset[0]) ))  
    weights_A  = np.zeros(len(weights[0]))
    weights_B  = np.zeros(len(weights[0]))
    weights_C  = np.zeros(len(weights[0]))
    best_A  = np.zeros(dataset_A.shape[1])
    best_B  = np.zeros(dataset_A.shape[1])
    best_C  = np.zeros(dataset_A.shape[1])
    worst_A = np.zeros(dataset_A.shape[1])
    worst_B = np.zeros(dataset_A.shape[1])
    worst_C = np.zeros(dataset_A.shape[1])
    for j in range(0, dataset_A.shape[1]):
        weights_A[j] = weights[0][j][0]
        weights_B[j] = weights[0][j][1]
        weights_C[j] = weights[0][j][2]
        for i in range(0, dataset_A.shape[0]):
            a, b, c = dataset[i][j]
            dataset_A[i, j] = a
            dataset_B[i, j] = b
            dataset_C[i, j] = c
    for i in range(0, dataset_A.shape[1]):
        if (criterion_type[i] == 'Max'):
            best_A[i]  = np.max(dataset_A[:, i])
            best_B[i]  = np.max(dataset_B[:, i])
            best_C[i]  = np.max(dataset_C[:, i])
            worst_A[i] = np.min(dataset_A[:, i])
            worst_B[i] = np.min(dataset_B[:, i])
            worst_C[i] = np.min(dataset_C[:, i])
        else:
            best_A[i]  = np.min(dataset_A[:, i])
            best_B[i]  = np.min(dataset_B[:, i])
            best_C[i]  = np.min(dataset_C[:, i])
            worst_A[i] = np.max(dataset_A[:, i])
            worst_B[i] = np.max(dataset_B[:, i])
            worst_C[i] = np.max(dataset_C[:, i]) 
    s_i_A = weights_A*( abs(best_A - dataset_A) / abs(best_A - worst_A ) )
    s_i_B = weights_B*( abs(best_B - dataset_B) / abs(best_B - worst_B) )
    s_i_C = weights_C*( abs(best_C - dataset_C) / abs(best_C - worst_C) )
    r_i_A = np.max(s_i_A, axis = 1)
    r_i_B = np.max(s_i_B, axis = 1)
    r_i_C = np.max(s_i_C, axis = 1)
    s_i_A = np.sum(s_i_A, axis = 1)
    s_i_B = np.sum(s_i_B, axis = 1)
    s_i_C = np.sum(s_i_C, axis = 1)
    s_best_A  = np.min(s_i_A)
    s_best_B  = np.min(s_i_B)
    s_best_C  = np.min(s_i_C)
    s_worst_A = np.max(s_i_A)
    s_worst_B = np.max(s_i_B)
    s_worst_C = np.max(s_i_C)
    r_best_A  = np.min(r_i_A)
    r_best_B  = np.min(r_i_B)
    r_best_C  = np.min(r_i_C)
    r_worst_A = np.max(r_i_A)
    r_worst_B = np.max(r_i_B)
    r_worst_C = np.max(r_i_C)
    q_i_A = strategy_coefficient*( (s_i_A - s_best_A) / (s_worst_A - s_best_A) ) + (1 - strategy_coefficient)*( (r_i_A - r_best_A) / (r_worst_A - r_best_A) )
    q_i_B = strategy_coefficient*( (s_i_B - s_best_B) / (s_worst_B - s_best_B) ) + (1 - strategy_coefficient)*( (r_i_B - r_best_B) / (r_worst_B - r_best_B) )
    q_i_C = strategy_coefficient*( (s_i_C - s_best_C) / (s_worst_C - s_best_C) ) + (1 - strategy_coefficient)*( (r_i_C - r_best_C) / (r_worst_C - r_best_C) )
    s_i = (1/3)*(s_i_A + s_i_B + s_i_C)
    r_i = (1/3)*(r_i_A + r_i_B + r_i_C)
    q_i = (1/3)*(q_i_A + q_i_B + q_i_C)


    dq = 1 /(dataset_A.shape[0] - 1)
    flow_s = np.copy(s_i)
    flow_s = np.reshape(flow_s, (s_i.shape[0], 1))
    flow_s = np.insert(flow_s, 0, list(range(1, s_i.shape[0]+1)), axis = 1)
    flow_s = flow_s[np.argsort(flow_s[:, 1])]
    flow_r = np.copy(r_i)
    flow_r = np.reshape(flow_r, (r_i.shape[0], 1))
    flow_r = np.insert(flow_r, 0, list(range(1, r_i.shape[0]+1)), axis = 1)
    flow_r = flow_r[np.argsort(flow_r[:, 1])]
    flow_q = np.copy(q_i)

    flow_q = np.reshape(flow_q, (q_i.shape[0], 1)) 

    return(flow_q)

 
try:
    fQi=fuzzy_vikor_method(database, weight_matrix_dm, matrix_array_optimisation_C, strategy_coefficient)
    rankfuzzyVIKOR= [sorted(fQi,reverse=False).index(x)+1 for x in fQi]
    print(rankfuzzyVIKOR)
    #return rankfuzzyVIKOR
except RuntimeWarning: 
    print("Warning     : 'nan'  or invalid value detected in dataset. Please recheck the dataset")
    print("")
    print("Alert       : Only integer based variable will be accepted for evaluation")
    print("")
    print("Fuzzy VIKOR evaluation cannot proceed")
    print("")



 