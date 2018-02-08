# coding: utf-8

#  AipSpeech 百度云平台上有提供需要自己下载
from aip import AipSpeech
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
""" 你的 APPID AK SK """
#可以在百度云平台上免费获取文字转语音权限  网址https://cloud.baidu.com/?from=console
APP_ID = '********'
API_KEY = '*******************'
SECRET_KEY = '**********************'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
n=1
#小说的位置
with open('C:/Users/Mn/Desktop/1.txt', 'r') as f: 
	lines=f.readlines()
	for line in lines: 
		print n
		#语音效果设置，平台上有参考文档
		result  = client.synthesis(line, 'zh', 1, {'vol': 5,'per':3})
		#写入MP3，以行转化，百度限制没错传递2048字节，MP3合并参考WinRAR
		with open('C:/Users/Mn/Desktop/1/%s.mp3'%n, 'wb') as f:
			f.write(result)
		n=n+1



