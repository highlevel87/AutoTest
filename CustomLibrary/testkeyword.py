#-*- coding:utf-8 -*-
import paramiko
class test:
    """
    
    """
    def _init_(self):
        pass
    def linux_command(self,ip,user,pwd,command):
        """

        """
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=user, password=pwd, timeout=4)
        stdin, stdout, stderr = client.exec_command(command)
        return [stdout.read().strip(), stderr.read().strip()]
        #for std in stdout.readlines():
            #print std,
        client.close()
