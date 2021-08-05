import numpy as np

def dm1_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
dm1_c1,dm1_c2,dm1_c3,dm1_c4,dm1_c5,dm1_c6,dm1_c7,dm1_c8,dm1_c9,
dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20): 

    if num_val_sublv2 == 1:

        dm1_c1.pack() 
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))   

    if num_val_sublv2 == 2:

        dm1_c1.pack()
        dm1_c2.pack()                             
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))    

    if num_val_sublv2 == 3:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()                             
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))    

    if num_val_sublv2 == 4:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack() 
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))  

    if num_val_sublv2 == 5:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack() 
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))  

    if num_val_sublv2 == 6:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack() 
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))  

    if num_val_sublv2 == 7:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack() 
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))  

    if num_val_sublv2 == 8:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack() 
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))  

    if num_val_sublv2 == 9:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack() 
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))  

    if num_val_sublv2 == 11:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))  

    if num_val_sublv2 == 12:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c12.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm1_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))  

    if num_val_sublv2 == 13:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c12.pack()
        dm1_c13.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm1_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm1_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))  

    if num_val_sublv2 == 14:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c12.pack()
        dm1_c13.pack()
        dm1_c14.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm1_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm1_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm1_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13)) 

    if num_val_sublv2 == 15:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c12.pack()
        dm1_c13.pack()
        dm1_c14.pack()
        dm1_c15.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm1_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm1_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm1_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm1_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14)) 

    if num_val_sublv2 == 16:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c12.pack()
        dm1_c13.pack()
        dm1_c14.pack()
        dm1_c15.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm1_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm1_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm1_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm1_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm1_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15)) 

    if num_val_sublv2 == 17:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c12.pack()
        dm1_c13.pack()
        dm1_c14.pack()
        dm1_c15.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm1_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm1_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm1_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm1_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm1_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm1_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16)) 

    if num_val_sublv2 == 18:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c12.pack()
        dm1_c13.pack()
        dm1_c14.pack()
        dm1_c15.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm1_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm1_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm1_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm1_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm1_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm1_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm1_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17)) 

    if num_val_sublv2 == 19:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c12.pack()
        dm1_c13.pack()
        dm1_c14.pack()
        dm1_c15.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm1_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm1_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm1_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm1_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm1_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm1_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm1_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm1_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18))  

    if num_val_sublv2 == 20:

        dm1_c1.pack()
        dm1_c2.pack()
        dm1_c3.pack()
        dm1_c4.pack()
        dm1_c5.pack()
        dm1_c6.pack()
        dm1_c7.pack()
        dm1_c8.pack()
        dm1_c9.pack()
        dm1_c10.pack()
        dm1_c11.pack()
        dm1_c12.pack()
        dm1_c13.pack()
        dm1_c14.pack()
        dm1_c15.pack()
        dm1_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm1_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm1_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm1_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm1_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm1_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm1_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm1_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm1_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm1_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm1_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm1_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm1_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm1_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm1_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm1_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm1_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm1_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm1_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18)) 
        dm1_c20.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(0),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(19)) 


def dm2_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
dm2_c1,dm2_c2,dm2_c3,dm2_c4,dm2_c5,dm2_c6,dm2_c7,dm2_c8,dm2_c9,
dm2_c10,dm2_c11,dm2_c12,dm2_c13,dm2_c14,dm2_c15,dm2_c16,dm2_c17,dm2_c18,dm2_c19,dm2_c20): 

    if num_val_sublv2 == 1:

        dm2_c1.pack() 
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))   

    if num_val_sublv2 == 2:

        dm2_c1.pack()
        dm2_c2.pack()                             
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))    

    if num_val_sublv2 == 3:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()                             
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))    

    if num_val_sublv2 == 4:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack() 
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))  

    if num_val_sublv2 == 5:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack() 
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))  

    if num_val_sublv2 == 6:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack() 
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))  

    if num_val_sublv2 == 7:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack() 
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))  

    if num_val_sublv2 == 8:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack() 
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))  

    if num_val_sublv2 == 9:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack() 
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))  

    if num_val_sublv2 == 11:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))  

    if num_val_sublv2 == 12:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c12.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm2_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))  

    if num_val_sublv2 == 13:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c12.pack()
        dm2_c13.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm2_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm2_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))  

    if num_val_sublv2 == 14:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c12.pack()
        dm2_c13.pack()
        dm2_c14.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm2_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm2_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm2_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13)) 

    if num_val_sublv2 == 15:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c12.pack()
        dm2_c13.pack()
        dm2_c14.pack()
        dm2_c15.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm2_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm2_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm2_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm2_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14)) 

    if num_val_sublv2 == 16:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c12.pack()
        dm2_c13.pack()
        dm2_c14.pack()
        dm2_c15.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm2_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm2_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm2_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm2_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm2_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15)) 

    if num_val_sublv2 == 17:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c12.pack()
        dm2_c13.pack()
        dm2_c14.pack()
        dm2_c15.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm2_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm2_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm2_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm2_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm2_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm2_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16)) 

    if num_val_sublv2 == 18:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c12.pack()
        dm2_c13.pack()
        dm2_c14.pack()
        dm2_c15.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm2_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm2_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm2_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm2_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm2_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm2_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm2_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17)) 

    if num_val_sublv2 == 19:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c12.pack()
        dm2_c13.pack()
        dm2_c14.pack()
        dm2_c15.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm2_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm2_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm2_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm2_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm2_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm2_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm2_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm2_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18))  

    if num_val_sublv2 == 20:

        dm2_c1.pack()
        dm2_c2.pack()
        dm2_c3.pack()
        dm2_c4.pack()
        dm2_c5.pack()
        dm2_c6.pack()
        dm2_c7.pack()
        dm2_c8.pack()
        dm2_c9.pack()
        dm2_c10.pack()
        dm2_c11.pack()
        dm2_c12.pack()
        dm2_c13.pack()
        dm2_c14.pack()
        dm2_c15.pack()
        dm2_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm2_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm2_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm2_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm2_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm2_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm2_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm2_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm2_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm2_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm2_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm2_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm2_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm2_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm2_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm2_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm2_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm2_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm2_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18)) 
        dm2_c20.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(1),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(19)) 

def dm3_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
dm3_c1,dm3_c2,dm3_c3,dm3_c4,dm3_c5,dm3_c6,dm3_c7,dm3_c8,dm3_c9,
dm3_c10,dm3_c11,dm3_c12,dm3_c13,dm3_c14,dm3_c15,dm3_c16,dm3_c17,dm3_c18,dm3_c19,dm3_c20): 

    if num_val_sublv2 == 1:

        dm3_c1.pack() 
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))   

    if num_val_sublv2 == 2:

        dm3_c1.pack()
        dm3_c2.pack()                             
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))    

    if num_val_sublv2 == 3:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()                             
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))    

    if num_val_sublv2 == 4:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack() 
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))  

    if num_val_sublv2 == 5:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack() 
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))  

    if num_val_sublv2 == 6:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack() 
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))  

    if num_val_sublv2 == 7:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack() 
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))  

    if num_val_sublv2 == 8:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack() 
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))  

    if num_val_sublv2 == 9:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack() 
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))  

    if num_val_sublv2 == 11:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))  

    if num_val_sublv2 == 12:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c12.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm3_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))  

    if num_val_sublv2 == 13:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c12.pack()
        dm3_c13.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm3_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm3_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))  

    if num_val_sublv2 == 14:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c12.pack()
        dm3_c13.pack()
        dm3_c14.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm3_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm3_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm3_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13)) 

    if num_val_sublv2 == 15:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c12.pack()
        dm3_c13.pack()
        dm3_c14.pack()
        dm3_c15.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm3_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm3_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm3_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm3_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14)) 

    if num_val_sublv2 == 16:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c12.pack()
        dm3_c13.pack()
        dm3_c14.pack()
        dm3_c15.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm3_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm3_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm3_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm3_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm3_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15)) 

    if num_val_sublv2 == 17:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c12.pack()
        dm3_c13.pack()
        dm3_c14.pack()
        dm3_c15.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm3_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm3_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm3_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm3_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm3_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm3_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16)) 

    if num_val_sublv2 == 18:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c12.pack()
        dm3_c13.pack()
        dm3_c14.pack()
        dm3_c15.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm3_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm3_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm3_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm3_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm3_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm3_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm3_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17)) 

    if num_val_sublv2 == 19:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c12.pack()
        dm3_c13.pack()
        dm3_c14.pack()
        dm3_c15.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm3_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm3_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm3_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm3_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm3_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm3_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm3_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm3_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18))  

    if num_val_sublv2 == 20:

        dm3_c1.pack()
        dm3_c2.pack()
        dm3_c3.pack()
        dm3_c4.pack()
        dm3_c5.pack()
        dm3_c6.pack()
        dm3_c7.pack()
        dm3_c8.pack()
        dm3_c9.pack()
        dm3_c10.pack()
        dm3_c11.pack()
        dm3_c12.pack()
        dm3_c13.pack()
        dm3_c14.pack()
        dm3_c15.pack()
        dm3_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm3_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm3_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm3_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm3_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm3_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm3_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm3_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm3_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm3_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm3_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm3_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm3_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm3_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm3_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm3_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm3_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm3_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm3_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18)) 
        dm3_c20.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(2),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(19)) 

def dm4_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
dm4_c1,dm4_c2,dm4_c3,dm4_c4,dm4_c5,dm4_c6,dm4_c7,dm4_c8,dm4_c9,
dm4_c10,dm4_c11,dm4_c12,dm4_c13,dm4_c14,dm4_c15,dm4_c16,dm4_c17,dm4_c18,dm4_c19,dm4_c20): 

    if num_val_sublv2 == 1:

        dm4_c1.pack() 
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))   

    if num_val_sublv2 == 2:

        dm4_c1.pack()
        dm4_c2.pack()                             
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))    

    if num_val_sublv2 == 3:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()                             
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))    

    if num_val_sublv2 == 4:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack() 
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))  

    if num_val_sublv2 == 5:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack() 
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))  

    if num_val_sublv2 == 6:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack() 
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))  

    if num_val_sublv2 == 7:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack() 
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))  

    if num_val_sublv2 == 8:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack() 
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))  

    if num_val_sublv2 == 9:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack() 
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))  

    if num_val_sublv2 == 11:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))  

    if num_val_sublv2 == 12:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c12.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm4_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))  

    if num_val_sublv2 == 13:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c12.pack()
        dm4_c13.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm4_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm4_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))  

    if num_val_sublv2 == 14:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c12.pack()
        dm4_c13.pack()
        dm4_c14.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm4_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm4_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm4_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13)) 

    if num_val_sublv2 == 15:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c12.pack()
        dm4_c13.pack()
        dm4_c14.pack()
        dm4_c15.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm4_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm4_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm4_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm4_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14)) 

    if num_val_sublv2 == 16:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c12.pack()
        dm4_c13.pack()
        dm4_c14.pack()
        dm4_c15.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm4_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm4_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm4_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm4_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm4_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15)) 

    if num_val_sublv2 == 17:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c12.pack()
        dm4_c13.pack()
        dm4_c14.pack()
        dm4_c15.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm4_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm4_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm4_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm4_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm4_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm4_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16)) 

    if num_val_sublv2 == 18:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c12.pack()
        dm4_c13.pack()
        dm4_c14.pack()
        dm4_c15.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm4_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm4_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm4_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm4_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm4_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm4_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm4_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17)) 

    if num_val_sublv2 == 19:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c12.pack()
        dm4_c13.pack()
        dm4_c14.pack()
        dm4_c15.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm4_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm4_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm4_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm4_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm4_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm4_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm4_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm4_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18))  

    if num_val_sublv2 == 20:

        dm4_c1.pack()
        dm4_c2.pack()
        dm4_c3.pack()
        dm4_c4.pack()
        dm4_c5.pack()
        dm4_c6.pack()
        dm4_c7.pack()
        dm4_c8.pack()
        dm4_c9.pack()
        dm4_c10.pack()
        dm4_c11.pack()
        dm4_c12.pack()
        dm4_c13.pack()
        dm4_c14.pack()
        dm4_c15.pack()
        dm4_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm4_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm4_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm4_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm4_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm4_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm4_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm4_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm4_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm4_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm4_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm4_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm4_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm4_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm4_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm4_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm4_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm4_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm4_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18)) 
        dm4_c20.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(3),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(19)) 

def dm5_option(num_val_sublv2,label_criteria_tab2_x,gap_x_from_border,gap_x,dmbox_criteria_tab2_y,gapboxdm_fromtop,gap_y_dmweight,
dm5_c1,dm5_c2,dm5_c3,dm5_c4,dm5_c5,dm5_c6,dm5_c7,dm5_c8,dm5_c9,
dm5_c10,dm5_c11,dm5_c12,dm5_c13,dm5_c14,dm5_c15,dm5_c16,dm5_c17,dm5_c18,dm5_c19,dm5_c20): 

    if num_val_sublv2 == 1:

        dm5_c1.pack() 
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))   

    if num_val_sublv2 == 2:

        dm5_c1.pack()
        dm5_c2.pack()                             
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))    

    if num_val_sublv2 == 3:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()                             
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))    

    if num_val_sublv2 == 4:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack() 
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))  

    if num_val_sublv2 == 5:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack() 
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))  

    if num_val_sublv2 == 6:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack() 
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))  

    if num_val_sublv2 == 7:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack() 
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))  

    if num_val_sublv2 == 8:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack() 
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))  

    if num_val_sublv2 == 9:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack() 
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))  

    if num_val_sublv2 == 11:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))  

    if num_val_sublv2 == 12:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c12.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm5_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))  

    if num_val_sublv2 == 13:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c12.pack()
        dm5_c13.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm5_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm5_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))  

    if num_val_sublv2 == 14:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c12.pack()
        dm5_c13.pack()
        dm5_c14.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm5_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm5_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm5_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13)) 

    if num_val_sublv2 == 15:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c12.pack()
        dm5_c13.pack()
        dm5_c14.pack()
        dm5_c15.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm5_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm5_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm5_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm5_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14)) 

    if num_val_sublv2 == 16:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c12.pack()
        dm5_c13.pack()
        dm5_c14.pack()
        dm5_c15.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm5_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm5_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm5_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm5_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm5_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15)) 

    if num_val_sublv2 == 17:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c12.pack()
        dm5_c13.pack()
        dm5_c14.pack()
        dm5_c15.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm5_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm5_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm5_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm5_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm5_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm5_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16)) 

    if num_val_sublv2 == 18:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c12.pack()
        dm5_c13.pack()
        dm5_c14.pack()
        dm5_c15.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm5_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm5_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm5_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm5_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm5_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm5_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm5_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17)) 

    if num_val_sublv2 == 19:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c12.pack()
        dm5_c13.pack()
        dm5_c14.pack()
        dm5_c15.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm5_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm5_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm5_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm5_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm5_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm5_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm5_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm5_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18))  

    if num_val_sublv2 == 20:

        dm5_c1.pack()
        dm5_c2.pack()
        dm5_c3.pack()
        dm5_c4.pack()
        dm5_c5.pack()
        dm5_c6.pack()
        dm5_c7.pack()
        dm5_c8.pack()
        dm5_c9.pack()
        dm5_c10.pack()
        dm5_c11.pack()
        dm5_c12.pack()
        dm5_c13.pack()
        dm5_c14.pack()
        dm5_c15.pack()
        dm5_c1.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(0))
        dm5_c2.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(1))
        dm5_c3.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(2))
        dm5_c4.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(3))
        dm5_c5.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(4))
        dm5_c6.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(5))
        dm5_c7.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(6))
        dm5_c8.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(7))
        dm5_c9.place (relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(8))
        dm5_c10.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(9))
        dm5_c11.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(10))
        dm5_c12.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(11))
        dm5_c13.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(12))
        dm5_c14.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(13))
        dm5_c15.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(14))     
        dm5_c16.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(15))
        dm5_c17.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(16))
        dm5_c18.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(17))
        dm5_c19.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(18)) 
        dm5_c20.place(relx=label_criteria_tab2_x+gap_x_from_border+gap_x*(4),rely=dmbox_criteria_tab2_y+gapboxdm_fromtop+gap_y_dmweight*(19)) 


def dm_place_forget_all(
dm1_c1,dm1_c2 ,dm1_c3 ,dm1_c4 ,dm1_c5 ,dm1_c6 ,dm1_c7 ,dm1_c8 ,dm1_c9 ,dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20,  
dm2_c1,dm2_c2 ,dm2_c3 ,dm2_c4 ,dm2_c5 ,dm2_c6 ,dm2_c7 ,dm2_c8 ,dm2_c9 ,dm2_c10,dm2_c11,dm2_c12,dm2_c13,dm2_c14,dm2_c15,dm2_c16,dm2_c17,dm2_c18,dm2_c19,dm2_c20,  
dm3_c1,dm3_c2 ,dm3_c3 ,dm3_c4 ,dm3_c5 ,dm3_c6 ,dm3_c7 ,dm3_c8 ,dm3_c9 ,dm3_c10,dm3_c11,dm3_c12,dm3_c13,dm3_c14,dm3_c15,dm3_c16,dm3_c17,dm3_c18,dm3_c19,dm3_c20,  
dm4_c1,dm4_c2 ,dm4_c3 ,dm4_c4 ,dm4_c5 ,dm4_c6 ,dm4_c7 ,dm4_c8 ,dm4_c9 ,dm4_c10,dm4_c11,dm4_c12,dm4_c13,dm4_c14,dm4_c15,dm4_c16,dm4_c17,dm4_c18,dm4_c19,dm4_c20,  
dm5_c1,dm5_c2 ,dm5_c3 ,dm5_c4 ,dm5_c5 ,dm5_c6 ,dm5_c7 ,dm5_c8 ,dm5_c9 ,dm5_c10,dm5_c11,dm5_c12,dm5_c13,dm5_c14,dm5_c15,dm5_c16,dm5_c17,dm5_c18,dm5_c19,dm5_c20):     

    dm1_c1.place_forget()
    dm1_c2.place_forget()
    dm1_c3.place_forget()
    dm1_c4.place_forget()
    dm1_c5.place_forget()
    dm1_c6.place_forget()
    dm1_c7.place_forget()
    dm1_c8.place_forget()
    dm1_c9.place_forget()
    dm1_c10.place_forget()
    dm1_c11.place_forget()
    dm1_c12.place_forget()
    dm1_c13.place_forget()
    dm1_c14.place_forget()
    dm1_c15.place_forget()  
    dm1_c16.place_forget()
    dm1_c17.place_forget()
    dm1_c18.place_forget()
    dm1_c19.place_forget()
    dm1_c20.place_forget()  
    dm2_c1.place_forget()
    dm2_c2.place_forget()
    dm2_c3.place_forget()
    dm2_c4.place_forget()
    dm2_c5.place_forget()
    dm2_c6.place_forget()
    dm2_c7.place_forget()
    dm2_c8.place_forget()
    dm2_c9.place_forget()
    dm2_c10.place_forget()
    dm2_c11.place_forget()
    dm2_c12.place_forget()
    dm2_c13.place_forget()
    dm2_c14.place_forget()
    dm2_c15.place_forget() 
    dm2_c16.place_forget()
    dm2_c17.place_forget()
    dm2_c18.place_forget()
    dm2_c19.place_forget()
    dm2_c20.place_forget()  
    dm3_c1.place_forget()
    dm3_c2.place_forget()
    dm3_c3.place_forget()
    dm3_c4.place_forget()
    dm3_c5.place_forget()
    dm3_c6.place_forget()
    dm3_c7.place_forget()
    dm3_c8.place_forget()
    dm3_c9.place_forget()
    dm3_c10.place_forget()          
    dm3_c11.place_forget()          
    dm3_c12.place_forget()          
    dm3_c13.place_forget()          
    dm3_c14.place_forget()          
    dm3_c15.place_forget()      
    dm3_c16.place_forget()
    dm3_c17.place_forget()
    dm3_c18.place_forget()
    dm3_c19.place_forget()
    dm3_c20.place_forget()  
    dm4_c1.place_forget()          
    dm4_c2.place_forget()          
    dm4_c3.place_forget()          
    dm4_c4.place_forget()          
    dm4_c5.place_forget()          
    dm4_c6.place_forget()          
    dm4_c7.place_forget()          
    dm4_c8.place_forget()          
    dm4_c9.place_forget()          
    dm4_c10.place_forget()           
    dm4_c11.place_forget()           
    dm4_c12.place_forget()           
    dm4_c13.place_forget()           
    dm4_c14.place_forget()           
    dm4_c15.place_forget()     
    dm4_c16.place_forget()
    dm4_c17.place_forget()
    dm4_c18.place_forget()
    dm4_c19.place_forget()
    dm4_c20.place_forget()  
    dm5_c1.place_forget()           
    dm5_c2.place_forget()           
    dm5_c3.place_forget()           
    dm5_c4.place_forget()           
    dm5_c5.place_forget()           
    dm5_c6.place_forget()           
    dm5_c7.place_forget()           
    dm5_c8.place_forget()           
    dm5_c9.place_forget()           
    dm5_c10.place_forget()           
    dm5_c11.place_forget()           
    dm5_c12.place_forget()           
    dm5_c13.place_forget()           
    dm5_c14.place_forget()           
    dm5_c15.place_forget()                      
    dm5_c16.place_forget()
    dm5_c17.place_forget()
    dm5_c18.place_forget()
    dm5_c19.place_forget()
    dm5_c20.place_forget()     


def dm_initial_set(
Typeofevaluation_Var_input,dm1_c1,dm1_c2 ,dm1_c3 ,dm1_c4 ,dm1_c5 ,dm1_c6 ,dm1_c7 ,dm1_c8 ,dm1_c9 ,dm1_c10,dm1_c11,dm1_c12,dm1_c13,dm1_c14,dm1_c15,dm1_c16,dm1_c17,dm1_c18,dm1_c19,dm1_c20,  
dm2_c1,dm2_c2 ,dm2_c3 ,dm2_c4 ,dm2_c5 ,dm2_c6 ,dm2_c7 ,dm2_c8 ,dm2_c9 ,dm2_c10,dm2_c11,dm2_c12,dm2_c13,dm2_c14,dm2_c15,dm2_c16,dm2_c17,dm2_c18,dm2_c19,dm2_c20,  
dm3_c1,dm3_c2 ,dm3_c3 ,dm3_c4 ,dm3_c5 ,dm3_c6 ,dm3_c7 ,dm3_c8 ,dm3_c9 ,dm3_c10,dm3_c11,dm3_c12,dm3_c13,dm3_c14,dm3_c15,dm3_c16,dm3_c17,dm3_c18,dm3_c19,dm3_c20,  
dm4_c1,dm4_c2 ,dm4_c3 ,dm4_c4 ,dm4_c5 ,dm4_c6 ,dm4_c7 ,dm4_c8 ,dm4_c9 ,dm4_c10,dm4_c11,dm4_c12,dm4_c13,dm4_c14,dm4_c15,dm4_c16,dm4_c17,dm4_c18,dm4_c19,dm4_c20,  
dm5_c1,dm5_c2 ,dm5_c3 ,dm5_c4 ,dm5_c5 ,dm5_c6 ,dm5_c7 ,dm5_c8 ,dm5_c9 ,dm5_c10,dm5_c11,dm5_c12,dm5_c13,dm5_c14,dm5_c15,dm5_c16,dm5_c17,dm5_c18,dm5_c19,dm5_c20):    
            
    if Typeofevaluation_Var_input > 1:
        dm1_c1 .set(0) 

    dm1_c2 .set(0) 
    dm1_c3 .set(0) 
    dm1_c4 .set(0) 
    dm1_c5 .set(0) 
    dm1_c6 .set(0) 
    dm1_c7 .set(0) 
    dm1_c8 .set(0) 
    dm1_c9 .set(0) 
    dm1_c10.set(0) 
    dm1_c11.set(0) 
    dm1_c12.set(0) 
    dm1_c13.set(0) 
    dm1_c14.set(0) 
    dm1_c15.set(0) 
    dm1_c16.set(0) 
    dm1_c17.set(0) 
    dm1_c18.set(0) 
    dm1_c19.set(0) 
    dm1_c20.set(0) 
    dm2_c1 .set(0) 
    dm2_c2 .set(0) 
    dm2_c3 .set(0) 
    dm2_c4 .set(0) 
    dm2_c5 .set(0) 
    dm2_c6 .set(0) 
    dm2_c7 .set(0) 
    dm2_c8 .set(0) 
    dm2_c9 .set(0) 
    dm2_c10.set(0) 
    dm2_c11.set(0) 
    dm2_c12.set(0) 
    dm2_c13.set(0) 
    dm2_c14.set(0) 
    dm2_c15.set(0) 
    dm2_c16.set(0)
    dm2_c17.set(0)
    dm2_c18.set(0)
    dm2_c19.set(0)
    dm2_c20.set(0)
    dm3_c1 .set(0) 
    dm3_c2 .set(0) 
    dm3_c3 .set(0) 
    dm3_c4 .set(0) 
    dm3_c5 .set(0) 
    dm3_c6 .set(0) 
    dm3_c7 .set(0) 
    dm3_c8 .set(0) 
    dm3_c9 .set(0) 
    dm3_c10.set(0) 
    dm3_c11.set(0) 
    dm3_c12.set(0) 
    dm3_c13.set(0) 
    dm3_c14.set(0) 
    dm3_c15.set(0) 
    dm3_c16.set(0)
    dm3_c17.set(0)
    dm3_c18.set(0)
    dm3_c19.set(0)
    dm3_c20.set(0)
    dm4_c1 .set(0) 
    dm4_c2 .set(0) 
    dm4_c3 .set(0) 
    dm4_c4 .set(0) 
    dm4_c5 .set(0) 
    dm4_c6 .set(0) 
    dm4_c7 .set(0) 
    dm4_c8 .set(0) 
    dm4_c9 .set(0) 
    dm4_c10.set(0) 
    dm4_c11.set(0) 
    dm4_c12.set(0) 
    dm4_c13.set(0) 
    dm4_c14.set(0) 
    dm4_c15.set(0) 
    dm4_c16.set(0)
    dm4_c17.set(0)
    dm4_c18.set(0)
    dm4_c19.set(0)
    dm4_c20.set(0)
    dm5_c1 .set(0) 
    dm5_c2 .set(0) 
    dm5_c3 .set(0) 
    dm5_c4 .set(0) 
    dm5_c5 .set(0) 
    dm5_c6 .set(0) 
    dm5_c7 .set(0) 
    dm5_c8 .set(0) 
    dm5_c9 .set(0) 
    dm5_c10.set(0) 
    dm5_c11.set(0) 
    dm5_c12.set(0) 
    dm5_c13.set(0) 
    dm5_c14.set(0) 
    dm5_c15.set(0) 
    dm5_c16.set(0)
    dm5_c17.set(0)
    dm5_c18.set(0)
    dm5_c19.set(0)
    dm5_c20.set(0)


def Matrix_quantitative_DM(num_val_sublv2,quantitative_value_dm_c1 ,quantitative_value_dm_c2 ,quantitative_value_dm_c3 ,quantitative_value_dm_c4 ,quantitative_value_dm_c5 ,quantitative_value_dm_c6 ,quantitative_value_dm_c7 ,quantitative_value_dm_c8 ,quantitative_value_dm_c9 ,quantitative_value_dm_c10,quantitative_value_dm_c11,quantitative_value_dm_c12,quantitative_value_dm_c13,quantitative_value_dm_c14,quantitative_value_dm_c15,           
    quantitative_value_dm_c16,quantitative_value_dm_c17,quantitative_value_dm_c18,quantitative_value_dm_c19,quantitative_value_dm_c20):
    
    if num_val_sublv2 ==0:
        weight_matrix_dm=0 

    if num_val_sublv2 ==1:
        weight_matrix_dm=quantitative_value_dm_c1  
        
    if num_val_sublv2 ==2:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2  
        ]) 
        
    if num_val_sublv2 ==3:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3  
        ]) 
        
    if num_val_sublv2 ==4:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4  
        ]) 
        
    if num_val_sublv2 ==5:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5  
        ]) 
        
    if num_val_sublv2 ==6:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6  
        ]) 
        
    if num_val_sublv2 ==7:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7  
        ]) 
        
    if num_val_sublv2 ==8:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8  
        ]) 
        
    if num_val_sublv2 ==9:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9  
        ]) 
        
    if num_val_sublv2 ==10:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10 
        ]) 
         
    if num_val_sublv2 ==11:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11 
        ]) 

    if num_val_sublv2 ==12:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11,
        quantitative_value_dm_c12  
        ]) 
        
    if num_val_sublv2 ==13:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11,
        quantitative_value_dm_c12,
        quantitative_value_dm_c13 
        ]) 
        
    if num_val_sublv2 ==14:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11,
        quantitative_value_dm_c12,
        quantitative_value_dm_c13,
        quantitative_value_dm_c14   
        ]) 
        
    if num_val_sublv2 ==15:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11,
        quantitative_value_dm_c12,
        quantitative_value_dm_c13,
        quantitative_value_dm_c14,
        quantitative_value_dm_c15  
        ]) 
        
    if num_val_sublv2 ==16:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11,
        quantitative_value_dm_c12,
        quantitative_value_dm_c13,
        quantitative_value_dm_c14,
        quantitative_value_dm_c15,                
        quantitative_value_dm_c16 
        ]) 
        
    if num_val_sublv2 ==17:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11,
        quantitative_value_dm_c12,
        quantitative_value_dm_c13,
        quantitative_value_dm_c14,
        quantitative_value_dm_c15,                
        quantitative_value_dm_c16,
        quantitative_value_dm_c17 
        ]) 
        
    if num_val_sublv2 ==18:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11,
        quantitative_value_dm_c12,
        quantitative_value_dm_c13,
        quantitative_value_dm_c14,
        quantitative_value_dm_c15,                
        quantitative_value_dm_c16,
        quantitative_value_dm_c17,
        quantitative_value_dm_c18 
        ]) 
        
    if num_val_sublv2 ==19:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11,
        quantitative_value_dm_c12,
        quantitative_value_dm_c13,
        quantitative_value_dm_c14,
        quantitative_value_dm_c15,                
        quantitative_value_dm_c16,
        quantitative_value_dm_c17,
        quantitative_value_dm_c18,
        quantitative_value_dm_c19 
        ]) 
        
    if num_val_sublv2 ==20:
        weight_matrix_dm=np.hstack([
        quantitative_value_dm_c1 ,
        quantitative_value_dm_c2 ,
        quantitative_value_dm_c3 ,
        quantitative_value_dm_c4 ,
        quantitative_value_dm_c5 ,
        quantitative_value_dm_c6 ,
        quantitative_value_dm_c7 ,
        quantitative_value_dm_c8 ,
        quantitative_value_dm_c9 ,
        quantitative_value_dm_c10,
        quantitative_value_dm_c11,
        quantitative_value_dm_c12,
        quantitative_value_dm_c13,
        quantitative_value_dm_c14,
        quantitative_value_dm_c15,                
        quantitative_value_dm_c16,
        quantitative_value_dm_c17,
        quantitative_value_dm_c18,
        quantitative_value_dm_c19,
        quantitative_value_dm_c20
        ]) 

    return weight_matrix_dm


def Matrix_quantitative_DM(num_val_sublv2,matrix_value_fuzzy_dm_c1 ,matrix_value_fuzzy_dm_c2 ,matrix_value_fuzzy_dm_c3 ,matrix_value_fuzzy_dm_c4 ,matrix_value_fuzzy_dm_c5 ,matrix_value_fuzzy_dm_c6 ,
    matrix_value_fuzzy_dm_c7 ,matrix_value_fuzzy_dm_c8 ,matrix_value_fuzzy_dm_c9 ,matrix_value_fuzzy_dm_c10,matrix_value_fuzzy_dm_c11,matrix_value_fuzzy_dm_c12,
    matrix_value_fuzzy_dm_c13,matrix_value_fuzzy_dm_c14,matrix_value_fuzzy_dm_c15,matrix_value_fuzzy_dm_c16,matrix_value_fuzzy_dm_c17,matrix_value_fuzzy_dm_c18,matrix_value_fuzzy_dm_c19,matrix_value_fuzzy_dm_c20):
    
    if num_val_sublv2 ==0:
        weight_matrix_dm=0 
                   
    if num_val_sublv2 ==1: 

        weight_matrix_dm=matrix_value_fuzzy_dm_c1 

    if num_val_sublv2 ==2: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2  
        ])

    if num_val_sublv2 ==3: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3   
        ])

    if num_val_sublv2 ==4: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4   
        ])

    if num_val_sublv2 ==5: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5  
        ])

    if num_val_sublv2 ==6: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6  
        ])

    if num_val_sublv2 ==7: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7  
        ])

    if num_val_sublv2 ==8: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8  
        ])

    if num_val_sublv2 ==9: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9  
        ])

    if num_val_sublv2 ==10: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10 
        ])

    if num_val_sublv2 ==11: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11 
        ])

    if num_val_sublv2 ==12: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11,
        matrix_value_fuzzy_dm_c12 
        ])

    if num_val_sublv2 ==13: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11,
        matrix_value_fuzzy_dm_c12,
        matrix_value_fuzzy_dm_c13 
        ])

    if num_val_sublv2 ==14: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11,
        matrix_value_fuzzy_dm_c12,
        matrix_value_fuzzy_dm_c13,
        matrix_value_fuzzy_dm_c14 
        ])

    if num_val_sublv2 ==15: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11,
        matrix_value_fuzzy_dm_c12,
        matrix_value_fuzzy_dm_c13,
        matrix_value_fuzzy_dm_c14,
        matrix_value_fuzzy_dm_c15 
        ])

    if num_val_sublv2 ==16: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11,
        matrix_value_fuzzy_dm_c12,
        matrix_value_fuzzy_dm_c13,
        matrix_value_fuzzy_dm_c14,
        matrix_value_fuzzy_dm_c15,                
        matrix_value_fuzzy_dm_c16 

        ])
    if num_val_sublv2 ==17: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11,
        matrix_value_fuzzy_dm_c12,
        matrix_value_fuzzy_dm_c13,
        matrix_value_fuzzy_dm_c14,
        matrix_value_fuzzy_dm_c15,                
        matrix_value_fuzzy_dm_c16,
        matrix_value_fuzzy_dm_c17 
        ])    

    if num_val_sublv2 ==18: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11,
        matrix_value_fuzzy_dm_c12,
        matrix_value_fuzzy_dm_c13,
        matrix_value_fuzzy_dm_c14,
        matrix_value_fuzzy_dm_c15,                
        matrix_value_fuzzy_dm_c16,
        matrix_value_fuzzy_dm_c17,
        matrix_value_fuzzy_dm_c18 
        ])    

    if num_val_sublv2 ==19: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11,
        matrix_value_fuzzy_dm_c12,
        matrix_value_fuzzy_dm_c13,
        matrix_value_fuzzy_dm_c14,
        matrix_value_fuzzy_dm_c15,                
        matrix_value_fuzzy_dm_c16,
        matrix_value_fuzzy_dm_c17,
        matrix_value_fuzzy_dm_c18,
        matrix_value_fuzzy_dm_c19
        ])    


    if num_val_sublv2 ==20: 

        weight_matrix_dm=np.hstack([
        matrix_value_fuzzy_dm_c1 ,
        matrix_value_fuzzy_dm_c2 ,
        matrix_value_fuzzy_dm_c3 ,
        matrix_value_fuzzy_dm_c4 ,
        matrix_value_fuzzy_dm_c5 ,
        matrix_value_fuzzy_dm_c6 ,
        matrix_value_fuzzy_dm_c7 ,
        matrix_value_fuzzy_dm_c8 ,
        matrix_value_fuzzy_dm_c9 ,
        matrix_value_fuzzy_dm_c10,
        matrix_value_fuzzy_dm_c11,
        matrix_value_fuzzy_dm_c12,
        matrix_value_fuzzy_dm_c13,
        matrix_value_fuzzy_dm_c14,
        matrix_value_fuzzy_dm_c15,                
        matrix_value_fuzzy_dm_c16,
        matrix_value_fuzzy_dm_c17,
        matrix_value_fuzzy_dm_c18,
        matrix_value_fuzzy_dm_c19,
        matrix_value_fuzzy_dm_c20
        ])

    return weight_matrix_dm



def function_matrix_array_optimisation_C(num_val_sublv2,c1_optimise_get ,c2_optimise_get ,c3_optimise_get ,c4_optimise_get ,c5_optimise_get ,c6_optimise_get ,c7_optimise_get ,c8_optimise_get ,c9_optimise_get ,
    c10_optimise_get,c11_optimise_get,c12_optimise_get,c13_optimise_get,c14_optimise_get,c15_optimise_get,c16_optimise_get,c17_optimise_get,c18_optimise_get,c19_optimise_get,c20_optimise_get):


    if num_val_sublv2 ==0:
        matrix_array_optimisation_C=0 

    if num_val_sublv2 == 1 : 

        matrix_array_optimisation_C=c1_optimise_get  

    if num_val_sublv2 == 2: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get  
        ])

    if num_val_sublv2 == 3: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get  
        ])

    if num_val_sublv2 == 4: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get  
        ])

    if num_val_sublv2 == 5: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get  
        ])

    if num_val_sublv2 == 6: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get  
        ])

    if num_val_sublv2 == 7: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get  
        ])

    if num_val_sublv2 == 8: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get  
        ])

    if num_val_sublv2 == 9: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get 
        ])

    if num_val_sublv2 == 10: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get 
        ])

    if num_val_sublv2 == 11: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get 
        ])

    if num_val_sublv2 == 12: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get,
        c12_optimise_get 
        ])

    if num_val_sublv2 == 13: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get,
        c12_optimise_get,
        c13_optimise_get 
        ])

    if num_val_sublv2 == 14: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get,
        c12_optimise_get,
        c13_optimise_get,
        c14_optimise_get 
        ])

    if num_val_sublv2 == 15: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get,
        c12_optimise_get,
        c13_optimise_get,
        c14_optimise_get,
        c15_optimise_get 
        ])

    if num_val_sublv2 == 16: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get,
        c12_optimise_get,
        c13_optimise_get,
        c14_optimise_get,
        c15_optimise_get,
        c16_optimise_get 
        ])

    if num_val_sublv2 == 17: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get,
        c12_optimise_get,
        c13_optimise_get,
        c14_optimise_get,
        c15_optimise_get,
        c16_optimise_get,
        c17_optimise_get 
        ])

    if num_val_sublv2 == 18: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get,
        c12_optimise_get,
        c13_optimise_get,
        c14_optimise_get,
        c15_optimise_get,
        c16_optimise_get,
        c17_optimise_get,
        c18_optimise_get 
        ])

    if num_val_sublv2 == 19: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get,
        c12_optimise_get,
        c13_optimise_get,
        c14_optimise_get,
        c15_optimise_get,
        c16_optimise_get,
        c17_optimise_get,
        c18_optimise_get,
        c19_optimise_get 
        ])

    if num_val_sublv2 == 20: 

        matrix_array_optimisation_C=np.hstack([
        c1_optimise_get ,
        c2_optimise_get ,
        c3_optimise_get ,
        c4_optimise_get ,
        c5_optimise_get ,
        c6_optimise_get ,
        c7_optimise_get ,
        c8_optimise_get ,
        c9_optimise_get ,
        c10_optimise_get,
        c11_optimise_get,
        c12_optimise_get,
        c13_optimise_get,
        c14_optimise_get,
        c15_optimise_get,
        c16_optimise_get,
        c17_optimise_get,
        c18_optimise_get,
        c19_optimise_get,
        c20_optimise_get,
        ])

    return matrix_array_optimisation_C