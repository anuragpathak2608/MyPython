import paramiko

username = "YOURUSERNAME"
password = "YOURPASSWORD"
remote_server_ip = "YOURIP"

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=remote_server_ip, username= username, password=password)

sftp_client = ssh_client.open_sftp()
sftp_client.put('/home/anurag/testfile.txt', '/root/testfile.txt')
sftp_client.get('/root/testfile1.txt', '/home/anurag/testfile1.txt')

print("file trasfered")



#Refrence : https://medium.com/@keagileageek/paramiko-how-to-ssh-and-file-transfers-with-python-75766179de73
