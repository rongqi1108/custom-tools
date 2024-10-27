import custom_functions_contants as cfc
import excel_functions as ef
if __name__ == '__main__':
    file_name = '口语词搭.xlsx'
    file_path = cfc.DESK_PATH + file_name
    sheet_name = 'Sheet2'
    column_name = '词搭'
    mixed_data = ef.read(file_path, sheet_name, column_name)
    english_data = []
    chinese_data = []
    cfc.split_en_ch(mixed_data, english_data, chinese_data)
    ef.write_by_index(file_path, 1, english_data)
    ef.write_by_index(file_path, 2, chinese_data)