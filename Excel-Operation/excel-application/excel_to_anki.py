import custom_functions_contants as cfc
import excel_functions as ef


if __name__ == '__main__':
    file_name = '口语词搭.xlsx'
    file_path = cfc.DESK_PATH + file_name
    # 感受 欲望 探索 场景 时间 地点 人物 频次
    sheet_name = '频次'
    en = '词搭'
    ch = '中文'
    eg = '例句'
    en_data = ef.read(file_path, sheet_name, en)
    ch_data = ef.read(file_path, sheet_name, ch)
    eg_data = ef.read(file_path, sheet_name, eg)
    content = ''
    for index, e in enumerate(en_data):
        content += ch_data[index] + ':'+ e + '<br><br>' + eg_data[index] + '\n'
    cfc.generate_txt_file(content, 'C:\\Users\\admin\\Desktop\\桌面\\' + sheet_name + '.txt')



