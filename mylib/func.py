#coding:utf-8

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
    
def get_python_version():
    import sys
    version = (sys.version.split('.')[0])
    if version == '3' :
        return True
    else:
        return False