import pandas as pd

def load_csv(file_path):
    """
    Loads feedback data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully. {len(data)} records found.")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        raise
