import io
import paramiko

HOST_NAME = "us-securetransfer.dnv.com"
USER_NAME = "measurementsne"
PASSWORD = "yerD!Hvdt8n5ysh!t"
PRIVATE_KEY_FILE = 'measurementsneprivate.pem'
PORT = 22

client = paramiko.client.SSHClient()
print(1 , client)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print(2 , client)
pkey = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_FILE)
client.connect(HOST_NAME, username=USER_NAME, password=PASSWORD)
print(3 , client)
pkey = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_FILE)
client.connect(HOST_NAME, username=USER_NAME, pkey = pkey)
print(4 , client)


_stdin, _stdout,_stderr = client.exec_command("ls")
print(_stdout.read().decode())
client.close()