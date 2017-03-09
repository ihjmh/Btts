# Btts
a python text to sound, use baidu tts cause most of situations can't use google

useage:
  
    from btts import Btts
  
    #default chinese
    b=Btts(lan='zh') 
    #check what language can support,which the list may not be true,i have not test all of it
    print(Btts.languages) 
  
    result  = b.genWavfile(file_name='test.wav',text='你好，世界')
    content = b.content  #you can get the wav body through this,but only after you execute b.genWavfile
    print(result) # True or False
