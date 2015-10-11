import subprocess
import os
import validation
import win
from sys import argv
script,bot1,bot2=argv
#verd = 7
print argv
def err(verd,botno):
	if(verd==5):
		sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)
		output=str('1 '+str(botno)+' 2'+' 2'+' z')
		sac.communicate(output)
		exit(0)
	elif(verd==2):
		sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)
		output=str('2 '+str(botno)+' 2'+' 2'+' z')
		sac.communicate(output)
		exit(0)
	elif(result==0):
		sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)
		output=str('3 '+str(botno)+' 2'+' 2'+' z')
		sac.communicate(output)
		exit(0)



#vic=1
os.system('gcc log2.c')
compiler1=subprocess.Popen('python prerunner1.py',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
compiler1.communicate(bot1)
check=os.path.isfile('test1')	
if(check==False):
	botno=1
	sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)
	output=str('4 '+str(botno)+' 2'+' 2'+' z')
	sac.communicate(output)
	exit(0)
	

compiler2=subprocess.Popen('python prerunner2.py',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
compiler2.communicate(bot2)
check=os.path.isfile('test2')	
if(check==False):
	botno=2
	sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)
	output=str('4 '+str(botno)+' 2'+' 2'+' z')
	sac.communicate(output)
	exit(0)



x=0
flagwin=0
error=0
p=1
while(flagwin==0 and error==0):
	no=1
	proc1=subprocess.Popen('python runner1.py',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	[a,b]=proc1.communicate()
	verd=int(a[12])
	if (verd==5 or verd==2):
		if verd==5:
			#print "time limit exceeded,exiting"
			#exit()
			error=1
			botno=1
			
			
		if verd==2:
			#print "forking detected exiting"
			#exit()
			error=1
			botno=1
			

	list_a=a[26:-3]
	print list_a
	splita=list_a.split()
	

	output=splita
	print output
	result=validation.main(output[0],output[1],output[2],output[3],no)
	print result
	if(result==0):
		#print("test")
		print("%r disqualified"% bot1)
		error=1
		botno=1
		err(verd,botno)
		
	elif(result=='m') :
		sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)

		output[0]=int(output[0])-1
		output[1]=int(output[1])-1
		output[2]=int(output[2])-1
		output[3]=int(output[3])-1
		output=str(output[0])+' '+str(output[1])+' '+str(output[2])+' '+str(output[3])+' '+'m'
		print output
		sac.communicate(output)
	elif(result=='k'):
		sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)

		output[0]=int(output[0])-1
		output[1]=int(output[1])-1
		output[2]=int(output[2])-1
		output[3]=int(output[3])-1
		output=str(output[0])+' '+str(output[1])+' '+str(output[2])+' '+str(output[3])+' '+'k'
		sac.communicate(output)
		print output
	

	if(win.win(1)=='w'):
		flagwin=1
		vic=1

	#BOT 2 KA CODE
	else:
		no=2
		proc2=subprocess.Popen('python runner2.py',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		[a,b]=proc2.communicate()	
		verd=int(a[12])
		print verd
		if (verd==5 or verd==2):
			if verd==5:
				#print "time limit exceeded,exiting"
				#exit()			
				error=1
				botno=2
				

			if verd==2:
				#print "forking detected exiting"
				#exit()
				error=1
				botno=2
				
		list_a = a[26:-3]
		print list_a
		splita=list_a.split()
		#print splita
		#print list_a[0]
		output=splita
		print output
		result=validation.main(output[0],output[1],output[2],output[3],no)
		print result
		no=1
		if(result is 0):
			print("%r disqualified"% bot2)
			error=1
			botno=2	
			err(verd,botno)			
		elif(result is 'm') :
			sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)
			output[0]=int(output[0])-1
			output[1]=int(output[1])-1
			output[2]=int(output[2])-1
			output[3]=int(output[3])-1
			output=str(output[0])+' '+str(output[1])+' '+str(output[2])+' '+str(output[3])+' '+'m'			
			print output
			sac.communicate(output)

		elif(result is 'k'):
			sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)

			output[0]=int(output[0])-1
			output[1]=int(output[1])-1
			output[2]=int(output[2])-1
			output[3]=int(output[3])-1
			output=str(output[0])+' '+str(output[1])+' '+str(output[2])+' '+str(output[3])+' '+'k'
			sac.communicate(output)
			print output
	if(win.win(2)=='w'):			
		flagwin=2
		vic=1
		if(vic==1):
			sac=subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=None,stderr=subprocess.PIPE)
			output=str(str(flagwin)+' 2'+' 2'+' 2'+' w')
			sac.communicate(output)
			exit(0)