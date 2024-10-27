import excel_functions as ef
import custom_functions_contants as cf

if __name__ == '__main__':
    file_name = 'tts.txt'
    file_path = cf.DESK_PATH + file_name
    content = cf.read_txt(file_path)
    # cf.generate_txt_file(content, file_path)
    cf.tts(content)