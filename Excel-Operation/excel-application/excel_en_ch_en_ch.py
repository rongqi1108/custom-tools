import custom_functions_contants as cfc
import excel_functions as ef


if __name__ == '__main__':
    file_name = '口语词搭.xlsx'
    file_path = cfc.DESK_PATH + file_name
    sheet_name = '感受'
    en = '词搭'
    ch = '中文'
    en_data = ef.read(file_path, sheet_name, en)
    ch_data = ef.read(file_path, sheet_name, ch)
    content = ''
    for index, e in enumerate(en_data):
        content += e + '\n' + ch_data[index] + '\n'
    cfc.generate_txt_file(content, 'C:\\Users\\admin\\Desktop\\桌面\\' + sheet_name + '.txt')



