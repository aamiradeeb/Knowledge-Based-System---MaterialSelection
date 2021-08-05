
import numpy as np 
import sqlite3
import pandas as pd
import warnings

warnings.filterwarnings('error') 

def TOPSIS(num_val_sublv2,weight_matrix_dm,matrix_array_optimisation_C):
    #weight_matrix_dm 
    #matrix_array_optimisation_C  
        #num_val_sublv2 

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


    def normalize(matrix, r, n, m):
        for j in range(m):
            sq = np.sqrt(sum(matrix[:, j]**2))
            for i in range(n): 
                r[i, j] = matrix[i, j]/sq  

        return r

    def weight_product(matrix, weight):
        r = matrix*weight
        return r

    def calc_ideal_best_worst(matrix_array_optimisation_C, matrix, n, m):
        ideal_worst = []
        ideal_best = []
        for i in range(m):
            if matrix_array_optimisation_C[i] == 'Max':
                ideal_worst.append(min(matrix[:, i]))
                ideal_best.append(max(matrix[:, i]))
            else:
                ideal_worst.append(max(matrix[:, i]))
                ideal_best.append(min(matrix[:, i]))
        return (ideal_worst, ideal_best)

    def euclidean_distance(matrix, ideal_worst, ideal_best, n, m):
        diw = (matrix - ideal_worst)**2
        dib = (matrix - ideal_best)**2
        dw = []
        db = []
        for i in range(n):
            dw.append(sum(diw[i, :])**0.5)
            db.append(sum(dib[i, :])**0.5)
        dw = np.array(dw)
        db = np.array(db)
        return (dw, db)

    def performance_score(distance_best, distance_worst, n, m):
        score = []
        score = distance_worst/(distance_best + distance_worst)
        return score

    def topsis(dataset, weight_matrix_dm, matrix_array_optimisation_C):
        #dataset = floater(dataset)
        dataset=np.array(dataset)
        n = len(dataset) # number of alternative
        m = len(dataset[0]) # number of criteria 
        r = np.empty((n, m))    
        r = normalize(dataset, r, n, m) # normalise matrix
        #print(r)
        t = weight_product(r, weight_matrix_dm) # weighted normalise matrix 
        (ideal_worst, ideal_best) = calc_ideal_best_worst(matrix_array_optimisation_C, t, n, m)
        (distance_worst, distance_best) = euclidean_distance(
            t, ideal_worst, ideal_best, n, m)
        score = performance_score(distance_best, distance_worst, n, m)
        #print(score)
        return (score)
        # returns a tupple with index of best data point as first element and score array(numpy) as the other

    try:
        CC=topsis(dataset, weight_matrix_dm, matrix_array_optimisation_C)
        rankcc= [sorted(CC,reverse=True).index(x)+1 for x in CC]
        #print(rankcc)
        return rankcc
    except ValueError: 
        print("Warning     : 'nan'  or invalid value detected in dataset. Please recheck the dataset")
        print("")
        print("Alert       : only integer based variable will be accepted for evaluation")
        print("")
        print("TOPSIS evaluation cannot proceed")
        print("")
