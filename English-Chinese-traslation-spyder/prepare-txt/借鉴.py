import requests
import re
import time
#url="https://dict.youdao.com/result?word=form&lang=en"

#headers={
#    "Cookie": "OUTFOX_SEARCH_USER_ID=1959936360@10.110.96.158; OUTFOX_SEARCH_USER_ID_NCOO=1296622016.6470625; __yadk_uid=x7bI3vhAaYCied973blqBic7l0nJuOSH; rollNum=true; ___rl__test__cookies=1678353215491; advertiseCookie=advertiseValue",
#    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
#    }
#resp=requests.get(url=url,headers=headers)
#cont=resp.content.decode('utf-8')
#reExpTra=re.compile('class="trans".*?>(.*?)<')
#dataTransList=reExpTra.findall(cont)
#print(dataTransList)

class EnglishTranslation(object):
    def __init__(self):
        self.keyword=''
        self.url=''
        self.headers={
    "Cookie": "OUTFOX_SEARCH_USER_ID=1959936360@10.110.96.158; OUTFOX_SEARCH_USER_ID_NCOO=1296622016.6470625; __yadk_uid=x7bI3vhAaYCied973blqBic7l0nJuOSH; rollNum=true; ___rl__test__cookies=1678353215491; advertiseCookie=advertiseValue",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
    }
    def getRespond(self,keyword):
        self.keyword=keyword
        self.url="https://dict.youdao.com/result?word={}&lang=en".format(keyword)
        return requests.get(url=self.url,headers=self.headers)
    def dealRespond(self,respond):
        reExpTrans=re.compile('class="trans(-content)?".*?>(.*?)<')
        cont=respond.content.decode('utf-8')
        dataTranList=reExpTrans.findall(cont)
        return dataTranList
    def dataSave(self,dataList):
        fileDir=r"C:\Users\86153\Desktop"
        fileName="EnglistWord.txt"
        filePath=fileDir+'\\'+fileName
        with open(filePath,'a') as outFile:
            outFile.write(self.keyword+':\n')
            for data in dataList:
                outFile.write(data[1]+'\n')
            outFile.write('\n')
    def run(self,filePath):
        with open(filePath,'r') as inFile:
            for lineData in inFile.readlines():
                lineData=lineData.rstrip()
                resp=self.getRespond(lineData)
                dataDealedList=self.dealRespond(resp)
                self.dataSave(dataDealedList)
                time.sleep(0.5)
                print(self.keyword,' ok')
if __name__=='__main__':
    ET=EnglishTranslation()
    ET.run(r"C:\Users\86153\Desktop\EnglishWord.txt")