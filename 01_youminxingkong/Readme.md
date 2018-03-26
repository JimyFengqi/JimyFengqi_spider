
* Author:JimyFengqi
* 创作时间：2017-05-09
* 修改时间：2018-03-26


#python 入门级别爬虫
##目的：爬取游民星空的图片




		前两天在游民星空看到几张美图，然后就想把它保存下来，但是一个一个的右键保存<br>
---

		然后最近在学python，刚入门，然后就忍不住用python把图片都给抓下来了<br>

---

这个例子，其实是比较早就已经写出来了，最近重新整理一下，然后弄出来一个python2的版本和一个python3 的版本


			运行的时候，直接 python run.py 
			或者python3 run.py
			这次修改之后，会自动的适应python版本，应该算是比较完善了
后续想到什么再接着更新
		PS:   在创建一个库的时候，每次的提交可能都需要输入账号密码，因为是采用的http的模式来修改
			通过下面的修改可以不用每次都提交
			首先是需要把ssh key加到上面
			然后修改 创建的库下面的配置文件， .git/config 里面的内容
				
			[remote "origin"]
        		#url = https://github.com/JimyFengqi/JimyFengqi_spider.git
       		 	url = https://账号:密码@github.com/JimyFengqi/JimyFengqi_spider.git
       			
        		fetch = +refs/heads/*:refs/remotes/origin/*





(原文博客地址：)[https://blog.csdn.net/qiqiyingse/article/details/51801918 "show"]




