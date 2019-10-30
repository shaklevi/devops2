import paramiko
import os


class CustomedSshClient:

    ssh = paramiko.SSHClient()
    user = 'ubuntu'
    password = 'root'

    def __init__(self, host_ip):
        # self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file(r'/home/ubuntu/net4ukey.pem')
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=host_ip, username=self.user, look_for_keys=True, pkey=key)

    def sendCommand(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        exit_status = stdout.channel.recv_exit_status()
        if exit_status == 0:
            print("Command Succeeded!")
        print(stdout.read().decode('ascii').strip("\n"))
        return stdout.read().decode('ascii').strip("\n")

    def closeCconnection(self):
        self.ssh.close()
