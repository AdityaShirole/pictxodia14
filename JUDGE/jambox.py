'''
    VERDICTS:
    2 - Process spawned using SYS_fork, SYS_vfork, SYS_clone
    5 - Time Limit exceeded
    7 - Output received within Time Limit
'''

import sys
import os
from sandbox import *
 
 
def sand(program_path, input_path):

    f_wr = os.open("stdout.txt",os.O_TRUNC|os.O_RDWR|os.O_CREAT)
    #s = Sandbox(program_path, owner="nobody", stdin=open(input_path, "r"), stdout=f_wr)
    
    cookbook = {
        'args': program_path,               # targeted program
        'owner':"nobody",
        'stdin': open(input_path, "r"),             # input to targeted program
        'stdout': f_wr,           # output from targeted program
        #'stderr': sys.stderr,           # error from targeted program
        'quota': dict(wallclock=30000,  # 30 sec
                      cpu=2000,         # 2 sec
                      memory=8388608,   # 8 MB
                      disk=1048576)}    # 1 MB

    s = Sandbox(**cookbook)
    s.run()
    output = os.fdopen(f_wr)
    output.seek(0)
    verdict = {'stdout' : output.read() , 'verdict' : s.result}
    
    return verdict
