import pandas as pd

class ExcelReader:
    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path

    def get_data(self, sheet_name=None, sheet_number=None):
        if sheet_name is not None:
            df = pd.read_excel(self.excel_file_path, sheet_name=sheet_name)
        elif sheet_number is not None:
            df = pd.read_excel(self.excel_file_path, sheet_name=sheet_number)
        else:
            raise ValueError("Either sheet_name or sheet_number must be provided")

        return df.to_dict(orient='records')

    def read_data(self, sheet_name, row_number, column_name):
        df = pd.read_excel(self.excel_file_path, sheet_name=sheet_name)
        return df.at[row_number - 1, column_name]


