#coding=utf-8
import requests
import re
import  json

left_url='http://yu.pk1024.info/bbs/'

downUrl="http://down.happytogether2015.com/freeone/down.php"
downHeader={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Content-Length':'50',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'__cfduid=ddd73aae69e20e8ddb4bdf10c03b5603e1440341165',
'Host':'down.happytogether2015.com',
'Origin':'http://down.happytogether2015.com',
'Pragma':'no-cache',
'Referer':'http://down.happytogether2015.com/freeone/file.php/NRL2CLa.html',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36'
}
formData={'type' : 'torrent','id' : 'NRL2CLa','name' : '1024gc.com_070415-001'}
downCookies={'__cfduid':'d5df37787808f3e2ac87502a20801c39e1440832841'}
testDownload=requests.post(downUrl,data=formData,headers=downHeader,cookies=downCookies)


# file_object = open('test.torrent', 'w')
# file_object.write(testDownload.response())
# file_object.close()
#print 'size is '+str(len(testDownload.text))
#print 'size is '+str(len(testDownload.text))

days_html=requests.get("http://yu.dk1024.info/bbs/forum-3-1.html")
every_day_url=re.findall('<td class="f_title">.*?<a href="(.*?)"',days_html.text,re.S)

i=1
for each in every_day_url:
    print str(i)+" "+left_url+each
    i+=1
print days_html

# torrent=open('test.torrent','wb')
# torrent.write(testDownload.content)
# torrent.close()
print 'finish'

# f=open('test.torrent','r')
# temp=f.read()
# f.close()
#
# pic_url=re.findall('''<img src="(.*?)" ''',html,re.S)
# i=1
# for each in pic_url:
#     print("now downloading"+str(i)+" "+each)
#     pic=requests.get(each)
#     fp = open('pic/' + str(i) + '.jpg','wb')
#     fp.write(pic.content)
#     fp.close()
#     i += 1