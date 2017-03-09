import requests

error_content='error:something wrong with the content'
class Btts(object):
    """docstring for Btts"""
    Baidu_TTS_URL='http://tts.baidu.com/text2audio?lan={}&ie={}&text={}'
    LANGUAGES = {
        'sq' : 'Albanian',
        'ar' : 'Arabic',
        'hy' : 'Armenian',
        'bn' : 'Bengali',
        'ca' : 'Catalan',
        'zh' : 'Chinese',
        'hr' : 'Croatian',
        'cs' : 'Czech',
        'da' : 'Danish',
        'nl' : 'Dutch',
        'en' : 'English',
        'eo' : 'Esperanto',
        'fi' : 'Finnish',
        'fr' : 'French',
        'de' : 'German',
        'el' : 'Greek',
        'hi' : 'Hindi',
        'hu' : 'Hungarian',
        'is' : 'Icelandic',
        'id' : 'Indonesian',
        'it' : 'Italian',
        'ja' : 'Japanese',
        'ko' : 'Korean',
        'la' : 'Latin',
        'lv' : 'Latvian',
        'mk' : 'Macedonian',
        'no' : 'Norwegian',
        'pl' : 'Polish',
        'pt' : 'Portuguese',
        'ro' : 'Romanian',
        'ru' : 'Russian',
        'sr' : 'Serbian',
        'sk' : 'Slovak',
        'es' : 'Spanish',
        'sw' : 'Swahili',
        'sv' : 'Swedish',
        'ta' : 'Tamil',
        'th' : 'Thai',
        'tr' : 'Turkish',
        'vi' : 'Vietnamese',
        'cy' : 'Welsh'
    }
    def __init__(self, lan='zh',ie='UTF-8'):
        # super(Btts, self).__init__()
        self.lan = lan
        self.ie  = ie
        self.max_tex = 1024

    def genWavfile(self,file_name='default.wav',text=''):
        if not text:
            return error_content
        param=Btts.Baidu_TTS_URL.format(self.lan,self.ie,text)
        wav_body=''
        r=requests.get(param)
        status_net=r.ok
        error_cont=r.text.find('err')
        # print(status_net,error_cont)
        if status_net and error_cont==-1:
            with open(file_name,'wb+') as f:
                f.write(r.content)
            return True
        else:
            return False,error_content

if __name__ == '__main__':
    b=Btts(lan='zh')
    rec = b.genWavfile(text='工')
    print(rec)
