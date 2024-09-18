import os
import sys

def verify_communities_impute():

    try:
        from communities_impute import impute_incomes, impute_unemployed, impute_public_housing 
    except ImportError:
        print("Impute function not found.")
        return

    print("=" * 80)
    print("Executing Imputation...\n")

    impute_incomes()
    impute_unemployed()
    impute_public_housing


def verify_suburb_income_extraction():

    try:
        from income_data import suburb_incomes
    except ImportError:
        print("Income extraction function not found")
        return

    print("=" * 80)
    print("Executing Income Extraction...\n")

    suburb_incomes()
   

def main():
    args = sys.argv
    assert len(args) >= 2, "Please provide a function"
    dataset_function = args[1]
    if dataset_function == "communities_impute":
        verify_communities_impute()
    elif dataset_function == "income_data":
        verify_suburb_income_extraction() 
    

if __name__ == "__main__":
    main()
