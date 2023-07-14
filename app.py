from dash import Dash, dash_table
import paramiko
import pandas as pd

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

with ftp.open('D140245_20230301_0000.csv') as file:
    file.prefetch()
    df = pd.read_csv(file)

df = df.head(10)

app = Dash(__name__)

app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])

if __name__ == '__main__':
    app.run_server(debug=True)