import pandas as pd

def load_raw_data (path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def save_processed_data(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)