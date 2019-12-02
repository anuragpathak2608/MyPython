import subprocess
host = input("Enter the ip addess to ping")
ping = subprocess.Popen(["ping", "-c 10", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = ping.communicate()

if stderr:
    print(stderr)
else:
    print(stdout)

