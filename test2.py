'''
from paramiko import Transport, SFTPClient, RSAKey
import paramiko

c = paramiko.SSHClient()
print("connecting")
c.connect( hostname = "usftp.dnv.com", username = "ftpmeasurementsne", password='e7!xBJzST!KfU!Ljg',allow_agent=False,look_for_keys=False)
print("connected" , c)

_stdin, _stdout,_stderr = c.exec_command("ls -l")
output = _stdout.read()
print(output)
'''

import paramiko

HOST_NAME = "usftp.dnv.com"
USER_NAME = "ftpmeasurementsne"
PASSWORD = "e7!xBJzST!KfU!Ljg"
#PRIVATE_KEY_FILE = 'id-dsa'
PORT = 22

transport = paramiko.Transport(HOST_NAME , PORT)
print(1, transport)
transport.start_client()
print(2 , transport)
transport.auth_password(USER_NAME, PASSWORD)
print(3 , transport)
#pkey = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_FILE)
#transport.auth_publickey(USER_NAME, pkey)