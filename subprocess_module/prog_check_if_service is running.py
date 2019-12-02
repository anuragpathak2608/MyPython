'''
this program checks the running process of the system and give the output.
'''
import subprocess

srv = "sshd"
'''Subprocess.call() method runs the command on the shell it accepts list ["command", "args"] and returns status code 0 for success
and non zero for error.
'''

service_check = subprocess.call(["ps", "-C", srv])
print(service_check)
print()
if service_check == 0:
    print("Service is Running...")
else:
    print("Service is not Runnig...")
    '''Start the service if its stopped'''
    subprocess.call(["systemctl", "start", "ssh"])
