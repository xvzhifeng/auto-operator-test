import paramiko

def start():
    ssh = paramiko.SSHClient()
    know_host = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(know_host)
    ssh.connect(hostname='15.119.6.139',
                port=22,
                username='root',
                password="root123")
    stdin, stdout, stderr = ssh.exec_command("ls -l")
    print(stdout.read().decode("utf8"))
    stdin, stdout, stderr = ssh.exec_command("cd /var/opt/cm/nfs/cmn/dat/csvbulk/alliance004/upload;pwd")
    print(stdout.read().decode("utf8"))
    stdin, stdout, stderr = ssh.exec_command("ls -l")
    print(stdout.read().decode("utf8"))



if __name__ == "__main__":
    print("start")
    start()