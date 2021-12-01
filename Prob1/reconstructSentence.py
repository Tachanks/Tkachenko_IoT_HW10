# File name: reconstructSentence.py
# Created by Aleks Tkachenko
# 
# reads two text files and reconstructs/combines their contents to produce the complete output.


import sys

def f_read(filepath):
    with open(filepath, 'r') as f:
	f_content = f.read().split()
	f.close()
    return  f_content

def f_write(filepath, content):
    with open(filepath, 'w') as f:
	f.write(content)
	f.close()

def main():
	if len(sys.argv) != 3:
	   sys.exit(1)	

	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
	output_string = "output.txt"

	input1 = f_read(arg1)
	input2 = f_read(arg2)

	arg1_len = len(input1)
	arg2_len = len(input2)

	print "List 1:"
        print input1
        print "List 1 Length:"
        print arg1_len
        print
        print "List 2:"
        print input2
        print "List 2 Length:"
        print arg2_len
        print
	max_length = arg1_len
	if arg2_len > arg1_len:
           max_length = arg2_len

	out = []
	while max_length > 0:
	    if input1:
		out.append(input1.pop())
	    if input2:
		out.append(input2.pop())
	    max_length -= 1

	input1 = ' '.join(input1)
	input2 = ' '.join(input2)
	output = ' '.join(out)
	f_write(output_string, output)
	print "List Output is:"
	print output
	print
	print "Output written to:"
	print output_string
	print 
if __name__ == '__main__':
	main()




