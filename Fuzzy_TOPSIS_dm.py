
import numpy as np 
import sqlite3
import pandas as pd
import warnings
import copy

warnings.filterwarnings('error') 

def fuzzyTOPSIS_fuzzydm(num_val_sublv2,ave_weight_dms_list,c_optimise_setdata_list): 

    con=sqlite3.connect("materialdatabase.db") 

    if num_val_sublv2 == 1 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1  
             FROM Material_database""",con)
    if num_val_sublv2 == 2 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2 
             FROM Material_database""",con)
    if num_val_sublv2 == 3 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3 
             FROM Material_database""",con)
    if num_val_sublv2 == 4 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4 
             FROM Material_database""",con)
    if num_val_sublv2 == 5 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5 
             FROM Material_database""",con)
    if num_val_sublv2 == 6 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6  
             FROM Material_database""",con)
    if num_val_sublv2 == 7 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7 
             FROM Material_database""",con)
    if num_val_sublv2 == 8 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8 
             FROM Material_database""",con)
    if num_val_sublv2 == 9 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9 
             FROM Material_database""",con)
    if num_val_sublv2 == 10 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10 
             FROM Material_database""",con)
    if num_val_sublv2 == 11 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11 
             FROM Material_database""",con)
    if num_val_sublv2 == 12 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11, CRITERIA_12 
             FROM Material_database""",con)
    if num_val_sublv2 == 13 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11, CRITERIA_12, CRITERIA_13 
             FROM Material_database""",con)
    if num_val_sublv2 == 14 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14 
             FROM Material_database""",con)
    if num_val_sublv2 == 15 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15 
             FROM Material_database""",con)
    if num_val_sublv2 == 16 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
             CRITERIA_16  
             FROM Material_database""",con)
    if num_val_sublv2 == 17 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
             CRITERIA_16 , CRITERIA_17 
             FROM Material_database""",con)
    if num_val_sublv2 == 18 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
             CRITERIA_16 , CRITERIA_17, CRITERIA_18 
             FROM Material_database""",con)
    if num_val_sublv2 == 19 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
             CRITERIA_16 , CRITERIA_17, CRITERIA_18, CRITERIA_19 
             FROM Material_database""",con)
    if num_val_sublv2 == 20 :
        df=pd.read_sql("""SELECT Material, 
            CRITERIA_1 , CRITERIA_2, CRITERIA_3, CRITERIA_4, CRITERIA_5, 
            CRITERIA_6, CRITERIA_7, CRITERIA_8, CRITERIA_9, CRITERIA_10, 
            CRITERIA_11, CRITERIA_12, CRITERIA_13, CRITERIA_14, CRITERIA_15,
             CRITERIA_16 , CRITERIA_17, CRITERIA_18, CRITERIA_19, CRITERIA_20 
             FROM Material_database""",con) 

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

    # Function: Fuzzy TOPSIS
    def fuzzy_topsis_method(dataset, ave_weight_dms_list, c_optimise_setdata_list ):
        r_ij      = copy.deepcopy(dataset)
        v_ij      = copy.deepcopy(dataset)
        p_ideal_A = copy.deepcopy(ave_weight_dms_list)
        n_ideal_A = copy.deepcopy(ave_weight_dms_list)
        dist_p    = np.zeros( (len(dataset), len(dataset[0])) )
        dist_n    = np.zeros( (len(dataset), len(dataset[0])) )
        for j in range(0, len(dataset[0])):
            c_star  = -float('inf')
            a_minus =  float('inf')
            for i in range(0, len(dataset)):
                a, b, c = dataset[i][j]
                if (c >= c_star and c_optimise_setdata_list[j] == 'Max'):
                    c_star = c
                if (a <= a_minus and c_optimise_setdata_list[j] == 'Min'):
                    a_minus = a
            if (c_optimise_setdata_list[j] == 'Max'):
                for i in range(0, len(r_ij)):
                    a, b, c    = r_ij[i][j]
                    r_ij[i][j] = (a/c_star, b/c_star, c/c_star)
            else:
                for i in range(0, len(r_ij)):
                    a, b, c    = r_ij[i][j]
                    r_ij[i][j] = (a_minus/c, a_minus/b, a_minus/a)
            for i in range(0, len(r_ij)):
                 a, b, c    = r_ij[i][j]
                 d, e, f    = ave_weight_dms_list[0][j]
                 v_ij[i][j] = (a*d, b*e, c*f)
            d, e, f = v_ij[0][j]
            x, y, z = v_ij[0][j]
            for i in range(0, len(v_ij)):
                a, b, c = v_ij[i][j]
                if (a > d):
                    d = a
                if (b > e):
                    e = b 
                if (c > f):
                    f = c  
                if (a < x):
                    x = a
                if (b < y):
                    y = b 
                if (c < z):
                    z = c  
            p_ideal_A[0][j] = (d, e, f) 
            n_ideal_A[0][j] = (x, y, z)
        for i in range(0, dist_p.shape[0]): 
            for j in range(0, dist_p.shape[1]):             
                a, b, c = v_ij[i][j]
                x, y, z = p_ideal_A[0][j]
                d, e, f = n_ideal_A[0][j]
                dist_p[i][j] = ( (1/dist_p.shape[1])* ( (a-x)**2 + (b-y)**2 + (c-z)**2 ) )**(1/2)
                dist_n[i][j] = ( (1/dist_n.shape[1])* ( (a-d)**2 + (b-e)**2 + (c-f)**2 ) )**(1/2)        
        d_plus  = np.sum(dist_p, axis = 1)
        d_minus = np.sum(dist_n, axis = 1) 
        c_i     = d_minus / (d_minus + d_plus) 

        return c_i 
 
    try:
        CCfuzzyTOPSIS=fuzzy_topsis_method(database, ave_weight_dms_list, c_optimise_setdata_list )
        rankfuzzyTOPSIS= [sorted(CCfuzzyTOPSIS,reverse=True).index(x)+1 for x in CCfuzzyTOPSIS] 
        return rankfuzzyTOPSIS
    except ValueError: 
        print("Warning     : 'nan'  or invalid value detected in dataset. Please recheck the dataset")
        print("")
        print("Alert       : only integer based variable will be accepted for evaluation")
        print("")
        print("Fuzzy TOPSIS evaluation cannot proceed")
        print("")
