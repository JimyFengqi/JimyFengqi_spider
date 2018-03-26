# -*- coding: utf-8 -*-

#!/usr/bin/python  
#coding:utf-8  
  
import urllib2  
import re  
import time  
import sys  
import datetime  
  
class MyQiuBai:  
    #初始化方法，定义一些变量  
    def __init__(self):  
        self.pageIndex=1  
        self.user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'  
        #初始化Headers  
        self.headers={'User-Agent':self.user_agent}  
        #存放段子的变量，每一个元素是每一页的段子  
        self.stories=[]  
        #存放程序是否继续运行的变量  
        self.enable=False  
        #将读过的段子保存到本地，这是本地文件名字  
        self.filename='qiubai.txt'  
        self.filesymbol=open(self.filename,'wb')  
  
    #传入某一页面的索引获得页面代码  
    def getPages(self,pageIndex):  
        #print "翻页 %d" % (pageIndex)  
        try:  
            #构建新的URL地址  
            url="http://www.qiushibaike.com/text/page/"+str(pageIndex)  
            #构建请求的request  
            request=urllib2.Request(url,headers=self.headers)  
            #利用urlopen获取页面代码  
            response=urllib2.urlopen(request)  
            #将页面转化为UTF-8编码格式  
            html=response.read().decode('utf-8')  
            return html  
        #捕捉异常，防止程序直接死掉  
        except urllib2.URLError,e:  
            if hasattr(e,"reason"):  
                print u"连接糗事百科失败，错误原因",e.reason  
                return None  
      
    def getPageItem(self,html):  
        #定义存贮list，保存所需内容  
        pageStories=[]  
        #通过正则暴力匹配获取内容，依次是作者、内容、点赞人数、评论人数  
        pattern_author=re.compile(u'<h2>(.*?)</h2>',re.S)  
        pattern_content=re.compile(u'<span>(.*?)</span>',re.S)  
        pattern_support=re.compile(u'<i class="number">(\d*)</i>\s*好笑',re.S)  
        pattern_comment=re.compile(u'<i class="number">(\d*)</i>\s*评论',re.S)  
          
        find_author=re.findall(pattern_author,html)  
        find_content=re.findall(pattern_content,html)  
        find_support=re.findall(pattern_support,html)  
        find_comment=re.findall(pattern_comment,html)  
        #有的可能没有作者，提前做一个判断  
        if find_author:  
            for i in xrange(len(find_author)):  
                #对段子内容简单的做一个处理，将换行符替换为真正的换行  
                replaceBR=re.compile("<br/>")  
                text=re.sub(replaceBR,"\n",find_content[i])  
                comment="0"  
                if i<len(find_comment):  
                    comment=find_comment[i].strip()  
                support="0"  
                if i<len(find_support):  
                    support=find_support[i].strip()  
                #将获得到的内容，存放到list中,此处的i，也代表了这是本页的第几条  
                pageStories.append([str(i+1),find_author[i].strip(),text,support,comment])  
        else:  
            print "数据异常"  
            return None  
        return pageStories  
    #加载并提取页面的内容，加入到列表中    
    def loadPage(self,pageCode):  
        if self.enable==True:  
            #当前加载页面小于2页就再加载一页  
            if len(self.stories)<2:  
                pageStories=self.getPageItem(pageCode)  
                if pageStories:  
                    #将该页的段子存放到全局list中  
                    self.stories.append(pageStories)  
    #调用该方法，每次敲回车打印输出一个段子                  
    def getOneJoke(self,pageStories,page):  
        for story in pageStories:  
            #获取当前时间  
            writetime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')  
            #打印输出一条段子 
            print '**************************************************'
            print "第%d页第%s篇\t发布人:%s\t%s\n%s\n赞:%s  评论人数:%s\n" % (page,story[0],story[1],str(writetime),story[2],story[3],story[4])  
            #输出之后，将其写到文件中  
            content="第%d页第%s篇\t发布人:%s\t%s\n%s\n赞:%s  评论人数:%s\n" % (page,story[0],story[1],str(writetime),story[2],story[3],story[4])  
            self.filesymbol.write(content)  
            self.filesymbol.write('\n')  
            input=raw_input()  
            #如果输入"Q"，那就退出程序，同时关闭文件描述符  
            if input=="Q":  
                self.enable=False  
                self.filesymbol.close()  
                return        
    def begin(self):  
        print u"正在读取糗事百科,按页数查看新段子,Q退出，按Enter读取下一条"  
        self.enable= True  
        #自定义新的起始页面  
        nowPage=1  
        input=raw_input('输入开始看的页面(默认是第一页开始):')  
        try:  
            nowPage=int(input)  
        except Exception,e:  
            print "input what %s" % (input)  
          
        if input=="Q":  
            self.enable=False  
            self.filesymbol.close()  
            return  
        while self.enable:  
            #获取起始页面  
            pageCode=self.getPages(nowPage)  
            if not pageCode:  
                print("页面加载失败...")  
                return None  
            #多缓存一页  
            self.loadPage(pageCode)  
            if len(self.stories)>0:  
                #从全局list中获取一页内容  
                pageStories=self.stories[0]  
                ##将全局list中第一个元素删除，因为已经取出  
                del self.stories[0]  
                #获取这一页的内容  
                self.getOneJoke(pageStories,nowPage)  
            nowPage +=1  
  
  
                  
reload(sys)  
sys.setdefaultencoding( "utf-8" )                 
qiubai=MyQiuBai()  
qiubai.begin()  