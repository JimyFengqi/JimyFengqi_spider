#!/usr/bin/python      
#coding:utf-8      
    
import HTMLParser      
import urllib2      
import re      
import time      
import sys      
import datetime      
from Tkinter import *      
reload(sys)      
sys.setdefaultencoding( "utf-8" )    
    
class MyQiuBai:      
    #初始化方法，定义一些变量      
    def __init__(self):      
        self.pageIndex=1      
        self.user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'      
        #初始化Headers      
        self.headers={'User-Agent':self.user_agent}      
        #存放段子的变量，每一个元素是每一页的段子      
        self.stories=[]      
        self.page_stories_num=[]    
        #存放程序是否继续运行的变量      
        self.enable=True      
        #将读过的段子保存到本地，这是本地文件名字      
        self.filename='qiubai.txt'      
        self.filesymbol=open(self.filename,'wb')    
    #传入某一页面的索引获得页面代码      
    def get_html_Pages(self,pageIndex):      
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
            html=HTMLParser.HTMLParser().unescape(html)#处理网页内容， 可以将一些html类型的符号如" 转换回双引号         
            return html      
        #捕捉异常，防止程序直接死掉      
        except urllib2.URLError,e:    
            print u"连接失败，错误原因",e.reason      
            return None      
        except urllib2.HTTPError,e:        
            print u"连接失败，错误原因：%s " % e.code        
            return None        
    
          
    def getPageItem(self,html,pageIndex):      
        print u'开始获取条目'    
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
                pageStories.append([str(i+1),find_author[i].strip(),text,support,comment,pageIndex])      
                self.page_stories_num.append([str(i+1),find_author[i].strip(),text,support,comment,pageIndex])    
        else:      
            print u"数据异常"      
            return None     
        print u'获取当前页面段子完毕， 总共获取%d 条' % len(pageStories)    
        #return pageStories    
    
    #加载并提取页面的内容，加入到列表中        
    def loadPage(self,pageCode,pageIndex):      
        #当前加载页面小于2页就再加载一页      
        if len(self.page_stories_num)<20:      
            self.getPageItem(pageCode,pageIndex)      
                
            
        
    #调用该方法，加页面内容，即 self.page_stories_num 页面内容不足一页，就要加载               
    def getOneJoke(self):    
        if len(self.page_stories_num) >1 :    
            #获取这一页的内容      
            story =self.page_stories_num[0]    
            #将全局list中第一个元素删除，因为已经取出      
            del self.page_stories_num[0]    
            return story    
        else:    
            print u'页面不足一页，加载新的页面'    
            pageCode=self.get_html_Pages(self.pageIndex)    
            self.loadPage(pageCode,self.pageIndex)    
            self.pageIndex +=1    
            if len(self.page_stories_num) >1 :    
                #获取这一页的内容      
                story =self.page_stories_num[0]    
                #将全局list中第一个元素删除，因为已经取出      
                del self.page_stories_num[0]    
                return story    
    #真正的调出一个段子    
    def get_one_story(self):    
        story=self.getOneJoke()    
        #获取当前时间      
        writetime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')      
        #打印输出一条段子      
        #print u"第%d页第%s篇\t发布人:%s\t%s\n%s\n赞:%s  评论人数:%s\n" % (story[5],story[0],story[1],str(writetime),story[2],story[3],story[4])      
        #输出之后，将其写到文件中      
        content="第%d页第%s篇\t发布人:%s\t%s\n%s\n赞:%s  评论人数:%s\n" % (story[5],story[0],story[1],str(writetime),story[2],story[3],story[4])      
        self.filesymbol.write(content)      
        self.filesymbol.write('\n')      
        return content    
        
         
#清楚函数      
def clear():    
    textShow.delete(1.0, END)    
#显示函数    
def showContent():    
    textShow.delete(1.0, END)    
    content=qiubai.get_one_story()    
    textShow.insert(1.0,content)    
    #print "hellow world"    
      
    
                
    
if __name__ == '__main__':      
    author_content='''''   
        *****************************************************  
                welcome to spider of qiushibaike          
                     modify on 2017-05-11             
                     @author: Jimy_Fengqi                 
        *****************************************************  
        '''  
                
    #print author_content    
        
        
    qiubai=MyQiuBai()    
    root = Tk()    
    title = Label(root, text='qiubai_made_by_Jimy_Fengqi',justify=CENTER)    
    title.grid()    
        
    textShow = Text(root)      
    textShow.grid(row=1, column=0, columnspan=2)    
    textShow.insert(1.0,author_content)    
    nextButton = Button(root, text='Next', command=showContent)      
    nextButton.grid(row=2, column=0,columnspan=1)    
    clearButton = Button(root, text='Clear', command=clear)      
    clearButton.grid(row=2, column=1,columnspan=1)    
    root.mainloop()   