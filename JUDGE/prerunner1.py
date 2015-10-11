
import os

a=raw_input()
#a=a.split()
b=a.split(".")
#print b
if(b[1]=='c'):
	print b
	os.system("gcc -o test1 "+a+"" )
elif(b[1]=='cpp'):
	print b
	os.system("g++ -o test1 "+a+"")
else:
	print("your code is ghatiya")

