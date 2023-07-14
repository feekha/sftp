import paramiko
import pandas as pd

#HOST_NAME = "us-securetransfer.dnv.com"
#USER_NAME = "measurementsne"
#PASSWORD = "yerD!Hvdt8n5ysh!t"
#PRIVATE_KEY_FILE = 'measurementsneprivate.pem'
#PORT = 22

HOST_NAME = "ftp.resourcepanorama.dnvgl.com"
USER_NAME = "lidardashboard"
PASSWORD = "fatten-^xChD-keW"
PORT = 22

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(HOST_NAME , username = USER_NAME , password = PASSWORD , port = PORT)

ftp = ssh.open_sftp()
ftp.chdir('HAW')
ftp.chdir('MAST')
files = ftp.listdir()

print(files)

with ftp.open('D140245_20230301_0000.csv') as file:
    file.prefetch()
    df = pd.read_csv(file)

print(df)

'''
transport = paramiko.Transport(HOST_NAME , PORT)
print(1, transport)
transport.start_client()
print(2 , transport)
transport.auth_password(USER_NAME, PASSWORD)
print(3 , transport)

transport
#pkey = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_FILE)
#transport.auth_publickey(USER_NAME, pkey)

'''
