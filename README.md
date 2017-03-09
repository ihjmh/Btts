# Btts
a python text to sound, use baidu tts cause most of situations can't use google

useage:
  
  from btts import Btts
  
  
  print(Btts.languages) #check what language can support,which the list may not be true,i am not test all of it
  
  
  
  b=Btts(lan='zh') #default chinese
  
  result= b.genWavfile(file_name='test.wav',text='你好，世界')
  
  print(result) # True or False
