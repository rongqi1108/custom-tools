import requests
import re;


if __name__=='__main__':
    headers = {
        "Cookie": "OUTFOX_SEARCH_USER_ID=1959936360@10.110.96.158; OUTFOX_SEARCH_USER_ID_NCOO=1296622016.6470625; __yadk_uid=x7bI3vhAaYCied973blqBic7l0nJuOSH; rollNum=true; ___rl__test__cookies=1678353215491; advertiseCookie=advertiseValue",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
    }
    u = "https://dict.youdao.com/result?word={}&lang=en".format("key")
    respond = requests.get(url=u, headers=headers)
    reExpTrans = re.compile('英</span><span class="phonetic" data-v-39fab836>/ (.*?) /<')
    reExpTrans2 = re.compile('美</span><span class="phonetic" data-v-39fab836>/ (.*?) /<')
    reExpTrans3 = re.compile('class="trans(-content)?".*?>(.*?)<')
    reExpTrans4 = re.compile('{sentence:"(.*?)"')
    reExpTrans5 = re.compile('sentence-translation":"(.*?)"')
    reExpTrans6 = re.compile('<span class="pos" data-v-8042e1b4>(.*?)<')
    reExpTrans7 = re.compile('class="point" data-v-61ce6cc7>(.*?)<')

    cont = respond.content.decode('utf-8')
    phonetic_uk = reExpTrans.findall(cont)
    phonetic_us = reExpTrans2.findall(cont)
    meanings = reExpTrans3.findall(cont)
    sen = reExpTrans4.findall(cont)
    sen_tran = reExpTrans5.findall(cont)
    pos = reExpTrans6.findall(cont)
    point = reExpTrans7.findall(cont)

    print("美音：")
    print(phonetic_us)
    print("英音：")
    print(phonetic_uk)
    print("含义：")
    print(meanings)
    print("例句：")
    print(sen)
    print("例句翻译：")
    print(sen_tran)
    print("词性：")
    print(pos)
    print("短语：")
    print(point)

    # result = []
    # for item in meanings:
    #     match = re.search(r'\((.*?),(.*?)\)', item[1])
    #     if match:
    #         result.append(match.group(2))
    # print(result)
    # print(meanings[0][1])
    # print(len(meanings))
    # print(len(pos))
    # print(point[0])
    print(sen[0])
    print(sen_tran[0])

# 英</span><span class="phonetic"
# 美</span><span class="phonetic"
# {sentence:"
# sentence-translation":"


'''
 class="pos" data-v-8042e1b4>v.
 <span class="pos" data-v-8042e1b4>n.<
 <span class="trans" data-v-8042e1b4>舞蹈，舞步；舞蹈（艺术）
 class="point" data-v-61ce6cc7>Just Dance
'''
