#Collect Data, Verify, and Convert Stats
# Read csv file
from utils import *
import pandas as pd
import matplotlib.pyplot as plt

# Set the maximum number of rows and columns to display
pd.set_option('display.max_rows', None)  # To display all rows
pd.set_option('display.max_columns', None) 
    

is_formatted = False
while is_formatted == False:
    path_to_stats = input('Please enter filepath to game/season stats: ')
    
    # Step 1. Verify file name ends with .csv
    path = verify_csv(path_to_stats)
    
    # Step 2. Turn data in csv file into panda
    # empty --> Check to see if df is empty 
    df = open_csv(path)
    
    # Step 3. Delete useless columns (2pt, 3pt, ft - Percentage | Points | Rank)
    df_update_columns = delete_columns(df)
    
    # Step 4. Split shooting stats into separate categories two_MA, 
    # twoA, threeMA, threeA, ftMA, ftA
    formatted_data = format_split_stats(df_update_columns)
    
    # Step 5: Change data types
    calculable_df = change_to_int(formatted_data) 
    print(calculable_df)
    # Production, Efficiency, Effectiveness Calculations
    calculable_df['twoProduction'] = production(calculable_df['twoMA'], calculable_df['twoA'])
    calculable_df['threeProduction'] = production(calculable_df['threeMA'], calculable_df['threeA'])
    calculable_df['ftProduction'] = production(calculable_df['ftMA'], calculable_df['ftA'])

    calculable_df['teamTwoProduction'] = production(calculable_df['twoMA'].sum(),calculable_df['twoA'].sum())
    calculable_df['teamThreeProduction'] = production(calculable_df['threeMA'].sum(),calculable_df['threeA'].sum())
    calculable_df['teamFtProduction'] = production(calculable_df['ftMA'].sum(),calculable_df['ftA'].sum())

    calculable_df['twoEfficiency'] = efficiency(calculable_df['twoMA'], calculable_df['twoA'])
    calculable_df['threeEfficiency'] = efficiency(calculable_df['threeMA'], calculable_df['threeA'])
    calculable_df['ftEfficiency'] = efficiency(calculable_df['ftMA'], calculable_df['ftA'])


    calculable_df['twoEffectiveness'] = effective(calculable_df['twoProduction'], calculable_df['teamTwoProduction'])
    calculable_df['threeEffectiveness'] = effective(calculable_df['threeProduction'], calculable_df['teamThreeProduction'])
    calculable_df['ftEffectiveness'] = effective(calculable_df['ftProduction'], calculable_df['teamFtProduction'])
    
    new_df = calculable_df[['Name', 'twoMA', 'twoA', 'threeMA', 'threeA', 'ftMA', 'ftA', 'twoProduction', 'threeProduction', 'ftProduction', 'twoEfficiency', 'threeEfficiency', 'ftEfficiency', 'twoEffectiveness', 'threeEffectiveness', 'ftEffectiveness']]
    dataToExcel = pd.ExcelWriter('updated_stat_sheet.xlsx', engine='xlsxwriter')
    new_df.to_excel(dataToExcel, index=False)
    dataToExcel.save()
    print('Updated stats have been written to Excel File successfully.')
    is_formatted = True
else:
    print("The csv file you have enter is invalid.")
    is_formatted = True
