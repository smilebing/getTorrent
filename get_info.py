#coding=utf-8
import  re
import  requests

url='http://yu.dk1024.net/bbs/thread-174653-1-1.html'
whole_page=requests.get(url)
whole_page.encoding='utf-8'

# temp=whole_page.text
# print temp
#print(whole_page.text)

result=re.findall('=<br />(.*?)<br />',whole_page.text,re.S)

i=1
for each in result:
    print str(i)+"  "+each
    i+=1

# 【影片名称】：gachi874 莉子－実録ガチ面接67<br />
# 【影片格式】：WMV<br />
# 【影片大小】：1.03GB<br />
# 【影片码别】：无码<br />
# 【特 征 码】：哈希校验; 1d589a990af673448024db8e32ce9713cfba483b; ;<br />
# 【做種期限】：<font color="#006400">5种或健康度1000，请大家下载完成后自觉上传一个小时！万分感谢！ </font><br />
# 【下载软件】：<font color="#8b0000">请使用比特彗星、比特精灵、μTorrent 等BT端下载！</font> <br />
# 【图片预览】： 图片较大请等待，看不到图请使用代理。 <br />