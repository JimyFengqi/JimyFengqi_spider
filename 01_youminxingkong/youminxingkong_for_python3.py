#!/usr/bin python  
#--*-- coding:utf-8 --*--  
import urllib.request
import urllib.parse
import urllib.error
import re 
   

def run_for_python3():
    welcom_fun()
  
    count = 1  
    html = getHtml_python3("http://www.gamersky.com/ent/201605/752759.shtml")  
    getImg_for_python3(html,count)  
    for i in range(2,10):  
        url = "http://www.gamersky.com/ent/201605/752759_%d.shtml" % (i)  
        print ("开始抓取",url  )
        html1 = getHtml_python3(url)  
        count +=1  
        getImg_for_python3(html1,count) 
  
#获取页面内容      
def getHtml_python3(url):          
    print (u'start crawl %s ...' % url      )
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}      
    req = urllib.request.Request(url=url,headers=headers)      
    try:      
        html = urllib.request.urlopen(req).read().decode('utf-8')      
        #html=HTMLParser.HTMLParser().unescape(html)#处理网页内容， 可以将一些html类型的符号如" 转换回双引号        
    except urllib.error.HTTPError as e:      
        print (u"连接失败，错误原因：%s " % e.code)      
        return None      
    except urllib.error.URLError as e :      
        if hasattr(e,'reason'):      
            print (u"连接失败，错误原因:%s " % e.reason      )
            return None      
    return html 
    
#获取图片列表的函数，并对图片列表进行遍历，然后将图片存盘到本地  
def getImg_for_python3(html,count):  
    #reg = r'"http.+?\.jpg'  
    #imgre = re.compile(r'src="(http.+?\.jpg)">')  
    imgre = re.compile(r'href="http.+?\.shtml\?(http.+?\.jpg)">')  
    imglist = re.findall(imgre,html)  
    x = 0  
    for imgurl in imglist:  
        urllib.request.urlretrieve(imgurl,'python3_num_%s_%s.jpg' % (x,count))  
        x+=1    
 

def welcom_fun():
    import sys
    import os
    #四种获取文件名字的方法
    #print ('__file__:'+__file__)
    #print ('sys.argv[0]:'+sys.argv[0])
    #print ('os.path.basename(__file__):'+os.path.basename(__file__))
    #print ('os.path.basename(sys.argv[0]):'+os.path.basename(sys.argv[0]))
    
    filename=__file__.split('.')[0]
    print ('''   
            *****************************************    
                  Welcome to python for %s            
                     Modify on 2017-03-26               
                  @author: Jimy _Fengqi              
            ***************************************** 
    ''' % filename)     

    
   
      
