inputfile = open('/home/anurag/Desktop/input.txt', 'r')
outputfile = open('/home/anurag/Desktop/output.txt', 'w')

for line in inputfile:
    if "{" not in line:
        outputfile.write(line.replace('http://10.11.15.32', ''))
inputfile.close()
outputfile.close()





