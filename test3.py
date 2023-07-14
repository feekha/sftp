import pysftp
import paramiko
from base64 import decodebytes

HOST_NAME = "us-securetransfer.dnv.com"
USER_NAME = "measurementsne"
PASSWORD = "yerD!Hvdt8n5ysh!t"
PRIVATE_KEY_FILE = 'id-dsa'
PORT = 22

key = paramiko.RSAKey(PRIVATE_KEY_FILE)
cnopts = pysftp.CnOpts()
cnopts.hostkeys.add(HOST_NAME, 'ssh-rsa', key)


with pysftp.Connection(host=HOST_NAME, username=USER_NAME, password=PASSWORD, cnopts=cnopts) as sftp:
    print(sftp)