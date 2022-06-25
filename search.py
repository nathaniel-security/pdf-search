import os
import sys

length_of_argv = len(sys.argv)

filename_arg = 1
i = 3

con = True
command = 'pdfgrep -rin ' + '"' + sys.argv[2] + '" ' + str(sys.argv[1])
#print(str(length_of_argv))

while True:
	if(i == (length_of_argv)):
		break
	if(length_of_argv>3):
		if(con==False):
			print(command)
			break
		grep_command = "| grep --colour -iF " + sys.argv[i] + " "
		i = i+1
		command = command + grep_command

	else:
		break

#print(command)
os.system(command)
