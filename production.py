# Step 5: Calculations



   



    df['teamTwoProduction'] = round(df['twoProduction'].mean(), 2)
    df['teamThreeProduction'] = round(df['threeProduction'].mean(), 2)
    df['teamFtProduction'] = round(df['ftProduction'], 2)


    return df
    




#   # Split dataframe into the following sections:
#     '''
#     pTwoShooting = [ Name, twoMA, twoMI, twoA, twoProduction, twoEfficiency, twoEffective, teamTwoEffective  ]
#     '''
#     # df_subset = df[['column1', 'column2']]
#     pTwoShooting = df[['Name', 'twoMA', 'twoMI', 'twoA', 'twoProduction', 'twoEfficiency', 'twoEffective', 'teamTwoEffective']]
