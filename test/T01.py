import time
from aot_lib.lib_log import logger
from aot_lib.Ssh import *

cmd1 = """
        cd /var/opt/cm/nfs/cmn/dat/csvbulk/alliance004/upload
        pwd
        mv backup/320001001-01-220901-99999.* .
        ls -l
        """
cmd2 = """
        cd /var/opt/cm/nfs/cmn/dat/csvbulk/alliance004/upload
        ls -l
        """

local_file_path = r"C:\xzf\2022-9-support-project\data\it\再点新规营业\test.log"
remote_file_path = r"/var/opt/cm/nfs/cmn/dat/csvbulk/alliance004/upload/test.log"

if __name__ == "__main__":
    # ssh1 = Ssh(ip="15.119.6.139",
    #            user="root",
    #            pwd="root123")
    # print(ssh1.send_command(cmd1))
    #
    # ssh1.sftp_upload_file(local_file_path, remote_file_path)
    # print(ssh1.send_command(cmd2))
    logger.debug("test")
