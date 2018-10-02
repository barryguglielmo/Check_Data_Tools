import pandas as pd
from pandas import ExcelWriter
import os

#This script Concatenates Bo's Data and Exports it to an Excel Sheet
#########################################################
#########################################################
def data_from_all_sheets(file, col_names, protlist, r1, r2, c1, c2):
    """Get the Data From all Sheets"""
    lg_data = []
    for i in protlist:
        myfile = pd.ExcelFile(file)
        data = myfile.parse(i).iloc[r1:r2,c1:c2]
        data.columns = col_names
        lg_data.append(data)
    return lg_data

#########################################################
def myconcat(files, col_names, protlist, out_file, r1, r2, c1 , c2):
    """Concat data from all sheets and return excel file"""
    a = data_from_all_sheets(files[0], col_names, protlist ,r1, r2, c1, c2)
    for f in range(1, len(files)):
        b = data_from_all_sheets(files[f], col_names, protlist ,r1, r2, c1, c2)
        for i in range(0, len(a)):
            a[i] = pd.concat([a[i], b[i]])     
    writer = ExcelWriter(out_file)
    for i in range(0, len(a)):
        a[i].to_excel(writer, sheet_name = str(protlist[i]))
    writer.save()

############################################################
##os.chdir('S:/Nutrition/Sacks Lab Data/2018.06 - OMNIHeart HDL Subspecies/DATA/BG')
##files = os.listdir()
##protlist = ['WP AI', 'A2 P1', 'C1 P1', 'C3 P1', 'E P1',
##          'E(A1)', 'A1AT P3', 'A2 P2', 'A2 P3', 'A4 P3',
##          'A2M P3', 'C1 P3', 'C2 P3', 'C3 P3', 'CoC3 P3',
##          'CP P3', 'E P3', 'FBG P3', 'HP P3', 'J P3', 'L1 P3',
##          'PLMG P3', 'PON1 P3']
##col_names = ['id','na1','abs1','calc1','mgdl1','na2','abs2','calc2','mgdl2',
##             'na3','avg','std','cv']
##out_file = 'ConcatData.xlsx'
##################################################################
##myconcat(files, col_names, protlist, out_file, 33, 69, 0, 13)
