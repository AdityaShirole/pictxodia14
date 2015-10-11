import os

a=raw_input()
#a=a.split()
b=a.split(".")
#print b
if(b[1]=='c'):
	os.system("gcc -o test2 "+a+"" )
elif(b[1]==cpp):
	os.system("g++ -o test2"+a+"")
else:
	print("your code is ghatiya")