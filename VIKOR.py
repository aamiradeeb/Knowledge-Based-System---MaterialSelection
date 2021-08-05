
import numpy as np 
import sqlite3
import pandas as pd
import warnings

warnings.filterwarnings('error') 
 
def VIKOR(num_val_sublv2,weight_matrix_dm,matrix_array_optimisation_C):
    #weight_matrix_dm 
    #matrix_array_optimisation_C  
    #num_val_sublv2

    strategy_coefficient=0.5

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

    def column(matrix, i):
        return [row[i] for row in matrix]

    if num_val_sublv2 == 1 :
        column1=column(arr,1)
        dataset=np.column_stack((
        column1
        )) 

    if num_val_sublv2 == 2 :
        column1=column(arr,1)
        column2=column(arr,2)
        dataset=np.column_stack((
        column1, column2
        )) 

    if num_val_sublv2 == 3 :
        column1=column(arr,1)
        column2=column(arr,2)
        column3=column(arr,3)
        dataset=np.column_stack((
        column1, column2, column3
        )) 

    if num_val_sublv2 == 4 :
        column1=column(arr,1)
        column2=column(arr,2)
        column3=column(arr,3)
        column4=column(arr,4)

        dataset=np.column_stack((
        column1, column2, column3, column4
        )) 

    if num_val_sublv2 == 5 :
        column1=column(arr,1)
        column2=column(arr,2)
        column3=column(arr,3)
        column4=column(arr,4)
        column5=column(arr,5)

        dataset=np.column_stack((
        column1, column2, column3, column4, column5
        )) 

    if num_val_sublv2 == 6 :
        column1=column(arr,1)
        column2=column(arr,2)
        column3=column(arr,3)
        column4=column(arr,4)
        column5=column(arr,5)
        column6=column(arr,6)

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6
        )) 

    if num_val_sublv2 == 7 :
        column1=column(arr,1)
        column2=column(arr,2)
        column3=column(arr,3)
        column4=column(arr,4)
        column5=column(arr,5)
        column6=column(arr,6)
        column7=column(arr,7)  

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7
        )) 

    if num_val_sublv2 == 8 :
        column1=column(arr,1)
        column2=column(arr,2)
        column3=column(arr,3)
        column4=column(arr,4)
        column5=column(arr,5)
        column6=column(arr,6)
        column7=column(arr,7)  
        column8=column(arr,8)

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8
        )) 

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

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9
        )) 

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

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10 
        )) 

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

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11 
        )) 

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

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11, column12 
        )) 

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

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11, column12, column13 
        )) 

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

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11, column12, column13, column14 
        )) 

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

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11, column12, column13, column14, column15 
        )) 

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

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11, column12, column13, column14, column15, column16 
        )) 

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

        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11, column12, column13, column14, column15, column16, column17 
        )) 

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
        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11, column12, column13, column14, column15, column16, column17, column18 
        )) 

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
        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11, column12, column13, column14, column15, column16, column17, column18, column19 
        )) 

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
        dataset=np.column_stack((
        column1, column2, column3, column4, column5, column6, column7, column8, column9, 
        column10, column11, column12, column13, column14, column15, column16, column17, column18, column19, column20
        ))  


    # Function: VIKOR

    def floater(dataset):  # .astype() can be used but is not reliable
        b = []
        for i in dataset:
            try:
                ix = []
                for j in i:
                    ix.append(float(j))
            except:
                ix = float(i)
                pass
            b.append(ix)
        b = np.array(b)
        return b
     
    # Function: VIKOR
    def vikor_method(dataset, weights, matrix_array_optimisation_C, strategy_coefficient):
        dataset=floater(dataset)
        X = np.copy(dataset)
        w = np.copy(weights)
        best  = np.zeros(X.shape[1])
     
        worst = np.zeros(X.shape[1])
     
        for i in range(0, dataset.shape[1]):
            if (matrix_array_optimisation_C[i] == 'Max'):
                best[i]  = np.max(X[:, i])
                worst[i] = np.min(X[:, i])
            else:
                best[i]  = np.min(X[:, i])
                worst[i] = np.max(X[:, i]) 
        s_i = w*( abs(best - X) / abs(best - worst) )
     
        r_i = np.max(s_i, axis = 1) 
        s_i = np.sum(s_i, axis = 1)
        s_best = np.min(s_i)
        s_worst = np.max(s_i)
        r_best = np.min(r_i)
        r_worst = np.max(r_i)
        q_i = strategy_coefficient*( (s_i - s_best) / (s_worst - s_best) ) + (1 - strategy_coefficient)*( (r_i - r_best) / (r_worst - r_best) ) 

        return (q_i)

    vikor_method(dataset, weight_matrix_dm, matrix_array_optimisation_C, strategy_coefficient)

    try:
        Qi=vikor_method(dataset, weight_matrix_dm, matrix_array_optimisation_C, strategy_coefficient)
        rankVIKOR= [sorted(Qi,reverse=False).index(x)+1 for x in Qi]
        #print(rankcc)
        return rankVIKOR
    except RuntimeWarning: 
        print("Warning     : 'nan'  or invalid value detected in dataset. Please recheck the dataset")
        print("")
        print("Alert       : Only integer based variable will be accepted for evaluation")
        print("")
        print("VIKOR evaluation cannot proceed")
        print("")