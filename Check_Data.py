import os
import pandas as pd
import numpy as np


def newdir():
    os.chdir("E:/Bo/NEW")
def olddir():
    os.chdir("E:/Bo/OLD")

d1 = "S:/Nutrition/Sacks Lab Data/2018.06 - OMNIHeart HDL Subspecies/DATA"

def checksnm(file1, directory1, file2, directory2):
    """Check to see if sheets match in two excel files"""
    os.chdir(directory1)
    f1 = pd.ExcelFile(file1)
    os.chdir(directory2)
    f2 = pd.ExcelFile(file2)
    if f1.sheet_names == f2.sheet_names:
        print("They are the same!")
    else:
        print("NOPE")
    #return f1.sheet_names, f2.sheet_names
    return f1, f2



##ex_list = ['2018.08.23 - OMNI Heart RUN 1.xlsm', '2018.08.30 - OMNI Heart RUN 2.xlsm', '2018.09.01 - OMNI Heart RUN 3.xlsm',
##           '2018.09.14 - OMNI Heart RUN 4.xlsm', '2018.09.15 - OMNI Heart RUN 5.xlsm']
def checkard(file_list, directory, row_start, row_end, col_start, col_end):
    """Make sure all plate readings are different"""
    os.chdir(directory)   
    for f in range(0,(len(file_list))):
        fx = pd.ExcelFile(str(file_list[f]))
        snames = fx.sheet_names
        #check file against itself
        for i in range(3, len(snames)- 3):
            fxp1 = fx.parse(i)
            for j in range(i + 1, len(snames)-2):
                fxp2 = fx.parse(j)
                fxp2_vals = fxp2.iloc[row_start:row_end,col_start:col_end]#for Bo project [80:87,1:12]
                f2m = fxp2_vals.as_matrix()
                fxp1_vals = fxp1.iloc[row_start:row_end,col_start:col_end]
                f1m = fxp1_vals.as_matrix()
                if np.array_equal(f1m, f2m)== True:
                    print("WARNING SAME READINGS SAME FILE: " + str(file_list[f])+" (" + str(snames[i]) + ' : '+str(snames[j])+ ')')
        #check against other files
        for k in range(f+1, (len(file_list) -1)):
            fk = pd.ExcelFile(str(file_list[k]))
            for m in range(3, len(snames)- 3):
                a = fx.parse(m)
                b = fk.parse(m)
                a_vals = a.iloc[row_start:row_end,col_start:col_end]
                b_vals = b.iloc[row_start:row_end,col_start:col_end]
                am = a.as_matrix()
                bm = b.as_matrix()
                if np.array_equal(am, bm) == True:
                    print("WARNING SAME READINGS CROSS FILE: "+ str(file_list[f]) + ' : ' + str(file_list[k])+ "(" + str(snames[m])+ ")")
#checkard(ex_list, d1, 80,87,1,12)           

                
        
