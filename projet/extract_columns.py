import pandas as pd
import json


def extract_columns(input_file: str, output_file: str, columns_file: str):
    """
    Extract the selected columns from the data and save them in a new file
    :param input_file: the name of the file to extract the columns from (a csv file)
    :param output_file: the name of the new file (a csv file)
    :param columns_file: the list of the columns to extract (a json file)
    """
    # read the columns to extract
    with open(columns_file) as f:
        columns = json.load(f)
    # read the data
    data = pd.read_csv(input_file, sep=",", header=0, index_col=False)
    # extract the selected columns
    data = data[columns]
    # save the data in a new file
    data.to_csv(output_file, index=False, sep=",")


if __name__ == "__main__":
    extract_columns("en.openfoodfacts.org.products.csv", "data.csv", "columns.json")
