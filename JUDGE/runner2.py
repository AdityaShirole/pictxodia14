'''
    Compiles < test.c > with < gcc > and creates a binary called < outfile >
    Calls sand( executable_path, input_path) from the file jambox.py.
    sand() returns the dictionary {verdict, stdout}
'''

import jambox
import os
a = jambox.sand("./test2","./grid.txt")
print (a)
