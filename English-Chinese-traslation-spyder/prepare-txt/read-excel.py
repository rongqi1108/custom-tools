import pandas as pd


def read_excel_column(file_path, sheet_name, column_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    column_data = df[column_name]
    return column_data


if __name__ == "__main__":
    file_path = 'C:\\Users\\admin\\Desktop\\vocabularies.xlsx'
    sheet_name = 'Sheet1'
    column_name = '单词'

    column_data = read_excel_column(file_path, sheet_name, column_name)
    print(column_data)
