import paramiko

username = "root"
password = "T*s1byte"
serverip = "10.11.15.64"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=serverip, username=username, password=password)
stdio, stdout, stderr = ssh_client.exec_command('sudo ls')
stdio.write('T*s1byte\n')
output = stdout.readline()
print(output)