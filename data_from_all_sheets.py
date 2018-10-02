import pandas as pd
import os


#########################################################

#########################################################
def data_from_all_sheets(file, col_names, sheet_id_list, r1, r2, c1, c2):
    """Get the Data From all Sheets"""
    lg_data = []
    for i in sheet_id_list:
        myfile = pd.ExcelFile(file)
        data = myfile.parse(i).iloc[r1:r2,c1:c2]
        data.columns = col_names
        lg_data.append(data)
    return lg_data


#########################################################
#  This example gets all of the sample ids, abosrbances and other calculations
# From a excel workbook
##exlist = ['WP AI', 'A2 P1', 'C1 P1', 'C3 P1', 'E P1',
##          'E(A1)', 'A1AT P3', 'A2 P2', 'A2 P3', 'A4 P3',
##          'A2M P3', 'C1 P3', 'C2 P3', 'C3 P3', 'CoC3 P3',
##          'CP P3', 'E P3', 'FBG P3', 'HP P3', 'J P3', 'L1 P3',
##          'PLMG P3', 'PON1 P3']
##expath = 'S:/Nutrition/Sacks Lab Data/2018.06 - OMNIHeart HDL Subspecies/DATA'
##exfile = '2018.08.23 - OMNI Heart RUN 1.xlsm'
##col_names = ['id','na1','abs1','calc1','mgdl1','na2','abs2','calc2','mgdl2',
##             'na3','avg','std','cv']
##os.chdir(expath)
##exlg_data = data_from_all_sheets(exfile, col_names, exlist ,33, 69, 0, 13)
###Further use example
##a = exlg_data[0]
##a['avg'].mean()
