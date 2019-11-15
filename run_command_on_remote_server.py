import paramiko

username = "YOURUSERNAME"
password = "YOURPASSWORD"
remote_server_ip = "YOURIP"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=remote_server_ip, username=username, password=password)

stdin, stdout, stderr = ssh_client.exec_command('ls -l')

output = stdout.readlines()

if output:
    print(output)
else:
    print(stderr)




