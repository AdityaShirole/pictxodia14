__author__ = 'apoorv'
grid=[]
def do():
    global grid
    for i in range(1,19):
        temp=['_' for j in range (1,19) ]
        grid.append(temp)
    grid_file=open("grid_val.txt","r")
    grid=[]
    for i in range(1,19):
        temp=['' for j in range (1,19) ]
        grid.append(temp)
    column=0
    row=0


    while(column<18) and (row<18):

        ch=grid_file.read(1)
        if(len(ch)==0):
            break
        if(ch!='_'):
             while(ch!='_') and len(ch)!=0 :
                grid[row][column]=grid[row][column]+ch
                ch=grid_file.read(1)
                if(len(ch)==0):
                    break
                if(ch=='b' or ch=='h' or ch=='k'):
                    if(column<17):
                        column=column+1
                    else:
                        column=0
                        if(row<17):
                            row=row+1
                        else:
                            break




             if(column<17):
                column=column+1


             else:
                 column=0
                 if(row<17):
                    row=row+1
                 else:
                     break
             grid[row][column]=ch
             if(column<17):
                column=column+1

             else:
                 column=0
                 if(row<17):
                    row=row+1
                 else:
                     break

        else:
            grid[row][column]=ch
            if(column<17):
                column=column+1
            else:
                column=0
                if(row<17):
                    row=row+1
                else:
                    break
    grid_file.close()

def win(player):
    do()
    global grid
    count=0
    piececount=0
    flag=0
    if (player==1):
        for oppiece in attack2:
            for yco in range(0,18):
                for xco in range(0,18):
                       if oppiece==grid[yco][xco]:
                           flag=1
                           break
                       else:
                           continue
        if flag==0:
            return 'w'
        if flag==1:
            for piece in attack1:
                if (piece==grid[17][8]) or (piece==grid[17][9]):
                    count=count+1
                    print(count)
                    if(count==2):
                        return 'w'
    if (player==2):
        for oppiece in attack1:
            for yco in range(0,18):
                for xco in range(0,18):
                       if oppiece==grid[yco][xco]:
                           flag=1
                           break
                       else:
                           continue
        if flag==0:
            return 'w'
        if flag==1:
            print('FINALLY')
            for piece in attack2:
                if (piece==grid[0][8]) or (piece==grid[0][9]):
                    count=count+1
                    if(count==2):
                        return 'w'


attack1=["h1","ba1m","ba1lr","ba1ll",'ka11','ka12']
attack2=['h2','ba2m','ba2lr','ba2ll','ka21','ka22']
#w=win(2)  #give player argument
#print(w)
#print(grid)
