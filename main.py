from src.data.load_data import load_raw_data, save_processed_data
from src.data.preprocess import preprocess_data


RAW_DATA_PATH = "data/raw/salaries.csv"
PROCESSED_DATA_PATH = "data/processed/processed_data.csv"

def main():

    #Load raw dataset
    df = load_raw_data(RAW_DATA_PATH)

    #Preprocess Data
    df_clean = preprocess_data(df)

    #Save processed Data
    save_processed_data(df_clean, PROCESSED_DATA_PATH)

    print("Data Processing Completed succesfully")

if __name__ == "__main__":
    main()