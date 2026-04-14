

def remove_duplicates(df):

    return df.drop_duplicates()


def drop_irrelevant_columns(df):
    
    columns_to_drop = ['salary_in_usd','salary_currency']
    return df.drop(columns=columns_to_drop, errors = 'ignore')

def handle_missing_values (df):
    return df


def preprocess_data (df):
    df = remove_duplicates(df)
    df = drop_irrelevant_columns(df)
    df = handle_missing_values(df)

    return df

