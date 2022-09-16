# coding:utf-8
import paramiko
import time
import threading


class Ssh(object):
    __ssh = ""
    __ip = ""
    __usename = ""
    __password = ""
    __port = 22
    __sshfile = ""
    __sftp = ""
    __tload = ""
    __tdown = ""

    def __init__(self, ip, user='root', pwd='admin', port=22, timeout=5):
        try:
            self.__ip = ip
            self.__usename = user
            self.__password = pwd
            self.__port = port
            self.__ssh = paramiko.SSHClient()
            self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.__ssh.connect(hostname=self.__ip, port=self.__port, username=self.__usename, password=self.__password,
                               timeout=timeout)

            self.__sshfile = paramiko.Transport((self.__ip, self.__port))
            self.__sshfile.connect(username=self.__usename, password=self.__password)
            self.__sftp = paramiko.SFTPClient.from_transport(self.__sshfile)
        except Exception as e:
            print("connect %s failed......" % self.__ip)
            self.__ssh.close()
            self.__sshfile.close()
            self.ssh_state = False
        return

    def sftp_upload_file(self, local_path, server_path):
        if self.ssh_state == False:
            return False
        try:
            # 添加异步
            self.__tload = threading.Thread(target=self.__sftp.put, args=(local_path, server_path))
            # self.__tload.setDaemon(True)
            self.__tload.start()
        except Exception as e:
            print(e)
            return False

    def sftp_down_file(self, server_path, local_path):
        if self.ssh_state == False:
            return False
        try:
            # 添加异步
            self.__tdown = threading.Thread(target=self.__sftp.get, args=(server_path, local_path))
            self.__tdown.start()
        except Exception as e:
            print(e)
            return False

    def send_command(self, cmd):
        if self.ssh_state == False:
            return False
        try:
            stdin, stdout, stderr = self.__ssh.exec_command(cmd)
            time.sleep(0.1)
        except Exception as e:
            return stderr.read().decode("utf8")
        return stdout.read().decode("utf8")

    def close(self):
        """
        wait threat complete
        :return:
        """
        try:
            self.__tload.join()
            self.__tdown.join()
        except BaseException as e:
            print(e)
        self.__ssh.close()
        self.__sshfile.close()

    # 修饰方法，是方法可以像属性一样访问
    @property
    def ssh_state(self):
        return self.__ssh

    @ssh_state.setter
    def ssh_state(self, nstate):
        self.__ssh = nstate