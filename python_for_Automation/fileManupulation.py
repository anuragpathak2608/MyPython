import time

#Opening raw input file
input_file = open('/home/anurag/pythonCode/MyPython/python_for_Automation/inputFile.txt', 'r')

#Opening file for writing failed tests
output_pass_file = open('/home/anurag/pythonCode/MyPython/python_for_Automation/output_pass.txt', 'w')

#Opening file for writing failed tests
output_fail_file = open('/home/anurag/pythonCode/MyPython/python_for_Automation/output_fail_file.txt', 'w')

#Reading whole file and printing on the console.
#print(input_file.read())


#Iterate throught the file
count = 1
for line in input_file:
    line_split = line.split()
    #.split function convert the line into list format
    # print(line_split)
    #print(str(count) + " " + line)

    #print only with pass test
    if line_split[2] == 'P':
        output_pass_file.write(line)
    else:
        output_fail_file.write(line)
    #time.sleep(2)
    count += 1

input_file.close()
output_fail_file.close()
output_pass_file.close()

