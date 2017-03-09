import requests

error_content='error:something wrong with the content'
class Btts(object):
    """docstring for Btts"""
    Baidu_TTS_URL='http://tts.baidu.com/text2audio?lan={}&ie={}&text={}'
    def __init__(self, lan='zh',ie='UTF-8'):
        # super(Btts, self).__init__()
        self.lan = lan
        self.ie  = ie
        self.max_tex = 1024

    def genWavfile(self,file_name='default.wav',content=''):
        if not content:
            return error_content
        param=Btts.Baidu_TTS_URL.format(self.lan,self.ie,content)
        r=requests.get(param)
        # print(help(r))
        if r.raise_for_status():
            return 
        with open(file_name,'ab+') as f:
            f.write(r.content)



if __name__ == '__main__':
    b=Btts()
    b.genWavfile(content='哈哈时是地地地地地地地地')
