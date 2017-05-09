#-*- coding:utf-8 -*-
import io
import string
import random
import os
import time
import paramiko

class createrandomfiles:
    
    def __init__(self):
        pass
    
    def create_floder_file(self,folderpath,num,num1,targetsize):
        filelist = [".doc",".mp4",".zip",".avi",".rmvb",".py"]
        for j in range(1,int(num)+1):
            fpath = folderpath + "\\testdata" + str(j)
            if os.path.exists(fpath):
                print ""
            else:
                os.makedirs(fpath)
                time.sleep(2)
            for i in range(1,int(num1)+1):
                x = random.randrange(len(filelist))
                localTime = time.strftime("%Y%m%d%H%M%S",time.localtime())
                filename = fpath + "\\" + localTime + "_" + str(i) + filelist[x]
                files = open(filename,'wb+')
                st = ""
                for z in range (1,random.randint(5,800)):
                    st = st.join(['',chr(33+random.randint(0,93))])
                content = string.join(localTime+"_"+st)
                files.seek(1024*(int(targetsize)))
                files.write(content)
                files.close

if __name__ == '__main__':
    crf = createrandomfiles()
    folderpath = raw_input("input dir(d:\\testdir):")
    num = raw_input("input folder numbers:")
    num1 = raw_input("input file numbers:")
    targetsize = raw_input("input file sizes (kb):")
    crf.create_floder_file(folderpath,num,num1,targetsize)
    print "It is over."
    time.sleep(3)