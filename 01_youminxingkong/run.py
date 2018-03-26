#!/usr/bin python  
#--*-- coding:utf-8 --*--  
import sys
import os 
import sys




def welcom_fun():
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

def get_python_version():
    print("sys.version is :"+sys.version.split(' ')[0]) 
    version = (sys.version.split('.')[0])
    if version == '3' :
        return True
    else:
        return False
        
if __name__ == "__main__":  
    if not get_python_version():
        import youminxingkong_for_python2
        youminxingkong_for_python2.run_for_python2()
    else:
        import youminxingkong_for_python3
        youminxingkong_for_python3.run_for_python3()
    
   
      
