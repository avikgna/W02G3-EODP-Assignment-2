import pandas as pd
import csv

def impute_incomes():
    """Function imputing household incomes <$600/week and household income percent 
    <$600/week with mean values"""

    communities_df = pd.read_csv('communities.csv')
    household_income_col = 'Equivalent household income <$600/week'
    mean_household_income = pd.to_numeric(communities_df["Equivalent household income <$600/week"], errors='coerce').mean()

    household_income_percent_col = 'Equivalent household income <$600/week, %'
    mean_household_income_percent = pd.to_numeric(communities_df["Equivalent household income <$600/week, %"], errors='coerce').mean()

    #converts any invalid values into Nan then replaces with 0, else if its a valid string we convert to a number
    communities_df[household_income_col] = pd.to_numeric(communities_df[household_income_col], errors='coerce').fillna(mean_household_income)
    communities_df[household_income_percent_col] = pd.to_numeric(communities_df[household_income_percent_col], errors='coerce').fillna(mean_household_income_percent)

    communities_df.to_csv("imputed_data_communities.csv")
    
    return

def impute_unemployed():
    communities_df = pd.read_csv('communities.csv')
    num_unemployed_col = 'Unemployed, persons'
    mean_num_unemployed = pd.to_numeric(communities_df["Unemployed, persons"], errors='coerce').mean()

    unemployed_percent_col = 'Unemployed, %'
    mean_unemployed_percent = pd.to_numeric(communities_df["Unemployed, %"], errors='coerce').mean()

    #converts any invalid values into Nan then replaces with 0, else if its a valid string we convert to a number
    communities_df[num_unemployed_col] = pd.to_numeric(communities_df[num_unemployed_col], errors='coerce').fillna(mean_num_unemployed)
    communities_df[unemployed_percent_col] = pd.to_numeric(communities_df[unemployed_percent_col], errors='coerce').fillna(mean_unemployed_percent)
    communities_df.to_csv("imputed_data_communities.csv")
    
    return

def impute_public_housing():
    communities_df = pd.read_csv('communities.csv')
    
    num_public_housing_col = 'Public Housing Dwellings'
    mean_num_housing = pd.to_numeric(communities_df["Public Housing Dwellings"], errors='coerce').mean()

    public_housing_percent_col = '% dwellings which are public housing'
    mean_public_housing_percent = pd.to_numeric(communities_df["% dwellings which are public housing"], errors='coerce').mean()

    #converts any invalid values into Nan then replaces with 0, else if its a valid string we convert to a number
    communities_df[num_public_housing_col] = pd.to_numeric(communities_df[num_public_housing_col], errors='coerce').fillna(mean_num_housing)
    communities_df[public_housing_percent_col] = pd.to_numeric(communities_df[public_housing_percent_col], errors='coerce').fillna(mean_public_housing_percent)
    communities_df.to_csv("imputed_data_communities.csv")
    
    return


