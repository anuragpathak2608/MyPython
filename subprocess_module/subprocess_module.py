import subprocess

'''this code is to demonstrate all about the subprocess module and its methods'''

#To run a command. call fun runs a commnad and returns the output to the stdout

output = subprocess.call(["ls", "-lart", "/homte/anurag"])
print(output)

#a 0 return code is for success and 1 to 255 are for anything else
if output == 0:
    print("Command executed successfully...")
else:
    print("Command Failed...")
print()
print()

subprocess.call(['df', '-h'])

# With shell being True, call() function treats this as command
subprocess.call('du -hs /home/anurag/pythonCode', shell=True)

#run function :           returns command and return code as a tupple
print(subprocess.run(["ls", "-lart"]))


#Python subprocess check_call() : it returns exception "CalledProcessError" if any error in running command
print(subprocess.check_call("ls -l /home", shell=True))
#print(subprocess.check_call("false"))

#Python subprocess check_output() : call function by default send the result to the stdout and return command execution status code
 #the output is bound to the parent process and is unretrievable for the calling program
 #check_output funcction is used to run the command and store output for the latter purpose.

out = subprocess.check_output("ls -lart", shell=True)
print(out)
print("this size of output is {} bytes".format(len(out)))

#popen function is used to create a child process
#stores the output into stdout and error into stderr
#pipe is used to store the result
# Communincate is used to read the output from the sub process.
a = subprocess.Popen("ls -lart", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=None)
stderr, stdout = a.communicate()


#refrence
'''
https://www.journaldev.com/17416/python-subprocess
https://www.pythonforbeginners.com/os/subprocess-for-system-administrators

'''