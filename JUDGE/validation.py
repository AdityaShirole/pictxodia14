__author__ = 'Apoorv c'

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
    print(grid)
def same(a,b,a1,b1):
   if (a==a1) and (b==b1):
        return 1

def defense_occupied():
    global grid
    for b in range(2,6):
        for a in range(1,18):
            if(player==1):
                for i in p2:
                    if(grid[b-1][a-1]==i):
                        return 1

    for b in range(14,18):
        for a in range(1,18):
            if(player==2):
                for i in p1:
                    if(grid[b-1][a-1]==i):
                        return 1

    return 0


def out_of_grid(a,b):
    if (a < 1) or (a > 18) or (b < 1) or (b > 18):
        return 1
    else:
        return 0


def black_area(a,b):
     if ((b==18) or (b==1)):
        if((a!=9) and (a!=10)):
            return 1
        else:
            return 0

     elif(b==17) or (b==2):
        if (a==1) or(a==2) or(a==17) or (a==18):
            return 1
        else:
            return 0

     elif(b==16) or (b==3):
        if(a==1) or(a==18):
            return 1
        else:
            return 0


def occupied(a,b):
    global grid
    if(grid[b-1][a-1]!='_'):
        for i in range (0, 10):
            if(grid[b-1][a-1]==p1[i]):
                return 1
            elif(grid[b-1][a-1]==p2[i]):
                return 2
    else:
        return 0

def ba1lr_jumpkill(a,b,a1,b1):
    if(player==1):
        if(b1<14):    #attack area
            if(a<4):    #non lane area
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:
                    return 1
                elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==2 and occupied(a,b+2)==0:
                    return 1
                elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==2 and occupied(a+2,b)==0:
                    return 1
            elif(a==4)or (a==5):   #lane area
                if(b1==b+2) and (a1==a) and occupied(a,b+1)==2 and occupied(a,b+2)==0:
                    return 1
        elif(b==13):
            if(a==4) or (a==5):
                    if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:
                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2:

                        return 1

        elif(b==12):
            if(a==4):
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
            elif(a==5):
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1

        elif (b1>=14):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==14) or (b==15):
                     if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2:

                        return 1
                if (b==16):
                    if(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==2 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==2 and occupied(a+2,b)==0 :

                     return 1

def ba1lr(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if ba1lr_jumpkill(a,b,a1,b1)!=1:
        if(b1<14 and player==1):    #attack area
            if(a<4):    #non lane area
                if (((a1!=a) and (a1!=a+1)) or ((b1!=b) and (b1!=b+1))):
                    return 0
            elif(a==4)or (a==5):   #lane area
                if((a1!=4) and (a1!=5)) or ( (b1!=b+1)):
                    return 0

        elif (b1>=14 and player==1):    #defense area
             if (a>10):
                 if (((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b+1)) ):
                     return 0
             elif (a<9):
                 if (((a1!=a)  and (a1!=a+1)) or ((b1!=b) and (b1!=b+1)) ):
                     return 0
             elif(a==9 or a==10):
                    if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ( (b1!=b+1)) ):
                         return 0
        return 'm'
    else:
        return 'k'


def ba2lr_jumpkill(a,b,a1,b1):
    if(player==2):
        if(b1>5):    #attack area
            if(a<4):    #non lane area
                if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                    return 1
                elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

                    return 1
            elif(a==4)or (a==5):   #lane area
                if(b1==b-2) and (a1==a) and occupied(a,b-1)==1and occupied(a,b+2)==0:

                    return 1
        elif(b==6):
            if(a==4) or (a==5):
                    if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:

                        return 1

        elif(b==7):
            if(a==4):
                if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
            elif(a==5):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1

        elif (b1<=5):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==5) or (b==4):
                     if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:

                        return 1
                if (b==3):
                    if(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==1 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1

def ba2lr(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if ba2lr_jumpkill(a,b,a1,b1)!=1:
        if(b1>5 and player==2):    #attack area
            if(a<4):    #non lane area
                if (((a1!=a) and (a1!=a+1)) or ((b1!=b) and (b1!=b-1))):
                    return 0
            elif(a==4)or (a==5):   #lane area
                if((a1!=4) and (a1!=5)) or ( (b1!=b-1)):
                    return 0

        elif (b1<=5 and player==2):    #defense area
             if (a>10):
                 if (((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b-1)) ):
                     return 0
             elif (a<9):
                 if (((a1!=a)  and (a1!=a+1)) or ((b1!=b) and (b1!=b-1)) ):
                     return 0
             elif(a==9 or a==10):
                    if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ( (b1!=b-1)) ):
                         return 0
        return 'm'
    else:
        return 'k'

def ba1ll(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if ba1ll_jumpkill(a,b,a1,b1)!=1:
        if(b1<14 and player==1):    #attack area
            if(a>15):    #non lane area
                if (((a1!=a) and (a1!=a-1)) or ( (b1!=b+1))):
                    return 0
            elif(a==14)or (a==15):   #lane area
                if (((a1!=14) and (a1!=15))) or (( (b1!=b+1))):
                    return 0

        elif (b1>=14 and player==1):    #defense area
             if (a1>10):
                 if (((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b+1)) ):
                    return 0
             elif (a1<9):
                 if (((a1!=a)  and (a1!=a+1)) or ((b1!=b) and (b1!=b+1)) ):
                    return 0
             else:
                  if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b+1)) ):
                     return 0
        return 'm'
    else:
        return 'k'

def ba1ll_jumpkill(a,b,a1,b1):
      if(player==1):
        if(b1<14):    #attack area
            if(a>15):    #non lane area
                if(b1==b+2) and (a1==a-2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                    return 1
                elif(a1==a-2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

                    return 1
            elif(a==14)or (a==15):   #lane area
                if(b1==b+2) and (a1==a) and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                    return 1
        elif(b==13):
            if(a==14) or (a==15):
                    if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b+2) and (a1==a+2) and occupied(a+1,b+1)==1:

                        return 1

        elif(b==12):
            if(a==14):
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
            elif(a==15):
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1

        elif (b1>=14):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==14) or (b==15):
                     if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b+2) and (a1==a+2) and occupied(a+1,b+1)==1:

                        return 1
                elif (b==16):
                    if(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==1 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1

def ba2ll(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if ba2ll_jumpkill(a,b,a1,b1)!=1:
        if(b1>5 and player==2):    #attack area
            if(a>15):    #non lane area
                if (((a1!=a) and (a1!=a-1)) or ((b1!=b) and (b1!=b-1))):
                    return 0
            elif(a==14)or (a==15):   #lane area
                if (((a1!=14) and (a1!=15))) or (((b1!=b-1))):
                    return 0

        elif (b1<=5 and player==2):    #defense area
             if (a1>10):
                 if (((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b-1)) ):
                    return 0
             elif (a1<9):
                 if (((a1!=a)  and (a1!=a+1)) or ((b1!=b) and (b1!=b-1)) ):
                    return 0
             else:
                  if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b-1)) ):
                     return 0
        return 'm'
    else:
        return 'k'

def ba2ll_jumpkill(a,b,a1,b1):
      if(player==1):
        if(b1>5):    #attack area
            if(a>15):    #non lane area
                if(b1==b-2) and (a1==a-2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                    return 1
                elif(a1==a-2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

                    return 1
            elif(a==14)or (a==15):   #lane area
                if(b1==b-2) and (a1==a) and occupied(a,b-1)==1and occupied(a,b+2)==0:

                    return 1
        elif(b==6):
            if(a==14) or (a==15):
                    if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b+2) and (a1==a+2) and occupied(a+1,b+1)==1:

                        return 1

        elif(b==7):
            if(a==14):
                if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
            elif(a==15):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1

        elif (b1>=5):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==5) or (b==4):
                     if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:

                        return 1
                elif (b==3):
                    if(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==1 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1

def ka11_jumpkill(a,b,a1,b1):
    if(player==1):
        if(b1<14):    #attack area
            if(a>5):    #non lane area
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                    return 1
                elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==2 and occupied(a+2,b)==0:

                    return 1
            elif(a==4)or (a==5):   #lane area
                if(b1==b+2) and (a1==a) and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                    return 1
        elif(b==13):
            if(a==4) or (a==5):
                    if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2:

                        return 1

        elif(b==12):
            if(a==4):
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
            elif(a==5):
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1

        elif (b1>=14):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==14) or (b==15):
                     if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2:

                        return 1
                if (b==16):
                    if(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==2 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1



def ka11_canter(a,b,a1,b1):
    if(player==1):
        if(b1<14):    #attack area
            if(a>5):    #non lane area
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                    return 1
                elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==1 and occupied(a+2,b)==0:

                    return 1
            elif(a==4)or (a==5):   #lane area
                if(b1==b+2) and (a1==a) and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                    return 1
        elif(b==13):
            if(a==4) or (a==5):
                    if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b+2) and (a1==a+2) and occupied(a+1,b+1)==1:

                        return 1

        elif(b==12):
            if(a==4):
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
            elif(a==5):
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1

        elif (b1>=14):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==14) or (b==15):
                     if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b+2) and (a1==a+2) and occupied(a+1,b+1)==1:

                        return 1
                if (b==16):
                    if(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==1 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1


def ka11(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if ka11_jumpkill(a,b,a1,b1)==1:
        return 'k'
    elif ka11_canter(a,b,a1,b1)==1:
        return 'm'
    else:
        if(b1<14 and player==1):    #attack area
            if(a>5):    #non lane area
                if (((a1!=a) and (a1!=a-1)) or ((b1!=b) and (b1!=b+1))):
                    return 0
            elif(a==4)or (a==5):   #lane area
                if((a1!=4) and (a1!=5)) or ((b1!=b+1)):
                    return 0

        elif (b1>=14 and player==1):    #defense area
             if (a>10):
                 if (((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b+1)) ):
                     return 0
             elif (a<9):
                 if (((a1!=a)  and (a1!=a+1)) or ((b1!=b) and (b1!=b+1)) ):
                     return 0
             elif(a==9 or a==10):
                    if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b+1)) ):
                         return 0
        return 'm'

def ka21_jumpkill(a,b,a1,b1):
      if(player==2):
        if(b1>5):    #attack area
            if(a>5):    #non lane area
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                    return 1
                elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==1 and occupied(a+2,b)==0:

                    return 1
            elif(a==4)or (a==5):   #lane area
                if(b1==b-2) and (a1==a) and occupied(a,b-1)==1and occupied(a,b+2)==0:

                    return 1
        elif(b==6):
            if(a==4) or (a==5):
                    if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:

                        return 1

        elif(b==7):
            if(a==4):
                if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
            elif(a==5):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1

        elif (b1<=5):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==5) or (b==4):
                     if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:

                        return 1
                if (b==3):
                    if(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==1 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1

def ka21_canter(a,b,a1,b1):

 if(player==2):
        if(b1>5):    #attack area
            if(a>5):    #non lane area
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==2 and occupied(a+2,b-2)==0:

                    return 1
                elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==2 and occupied(a,b-2)==0:

                    return 1
                elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==2 and occupied(a+2,b)==0:

                    return 1
            elif(a==4)or (a==5):   #lane area
                if(b1==b-2) and (a1==a) and occupied(a,b-1)==2 and occupied(a,b-2)==0:

                    return 1
        elif(b==6):
            if(a==4) or (a==5):
                    if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==2 and occupied(a+2,b-2)==0:

                        return 1
                    elif(b1==b-2) and a1==a  and occupied(a,b-1)==2 and occupied(a,b-2)==0:

                        return 1
                    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==2:

                        return 1

        elif(b==7):
            if(a==4):
                if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==2 and occupied(a+2,b-2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==2 and occupied(a,b-2)==0:

                        return 1
            elif(a==5):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==2 and occupied(a+2,b-2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==2 and occupied(a,b-2)==0:

                        return 1

        elif (b1<=5):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==5) or (b==4):
                     if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==2 and occupied(a+2,b-2)==0:

                        return 1
                     elif(b1==b-2) and a1==a  and occupied(a,b-1)==2 and occupied(a,b-2)==0:

                        return 1
                     elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==2:

                        return 1
                if (b==3):
                    if(b1==b-2) and a1==a  and occupied(a,b-1)==2 and occupied(a,b-2)==0:

                        return 1
            if (a>10):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==2 and occupied(a+2,b-2)==0 :

                     return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==2 and occupied(a,b-2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==2 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0 :

                     return 1
                 elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1

def ka21(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if ka21_jumpkill(a,b,a1,b1)==1:
        return 'k'
    elif ka21_canter(a,b,a1,b1)==1:
        return 'm'
    else:
        if(b1>5 and player==2):    #attack area
            if(a>5):    #non lane area
                if (((a1!=a) and (a1!=a-1)) or ((b1!=b) and (b1!=b-1))):
                    return 0
            elif(a==4)or (a==5):   #lane area
                if((a1!=4) and (a1!=5)) or ((b1!=b-1)):
                    return 0

        elif (b1<=5 and player==2):    #defense area
             if (a>10):
                 if (((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b-1)) ):
                     return 0
             elif (a<9):
                 if (((a1!=a)  and (a1!=a+1)) or ((b1!=b) and (b1!=b-1)) ):
                     return 0
             elif(a==9 or a==10):
                    if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b-1)) ):
                         return 0
        return 'm'

def ka12_jumpkill(a,b,a1,b1):
    if(player==1):
        if(b1<14):    #attack area
            if(a<14):    #non lane area
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                    return 1
                elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==2 and occupied(a+2,b)==0:

                    return 1
            elif(a==14)or (a==15):   #lane area
                if(b1==b+2) and (a1==a) and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                    return 1
        elif(b==13):
            if(a==14) or (a==15):
                    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2:

                        return 1

        elif(b==12):
            if(a==14):
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
            elif(a==15):
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1

        elif (b1>=14):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==14) or (b==15):
                     if(b1==b+2) and (a1==a-2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2:

                        return 1
                if (b==16):
                    if(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b+2) and (a1==a-2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a+1,b)==2 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1

def ka12_canter(a,b,a1,b1):
     if(player==1):
        if(b1<14):    #attack area
            if(a<14):    #non lane area
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                    return 1
                elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

                    return 1
            elif(a==14)or (a==15):   #lane area
                if(b1==b+2) and (a1==a) and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                    return 1
        elif(b==13):
            if(a==14) or (a==15):
                    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b+2) and (a1==a+2) and occupied(a+1,b+1)==1:

                        return 1

        elif(b==12):
            if(a==14):
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
            elif(a==15):
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1

        elif (b1>=14):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==14) or (b==15):
                     if(b1==b+2) and (a1==a-2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b+2) and (a1==a+2) and occupied(a+1,b+1)==1:

                        return 1
                if (b==16):
                    if(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b+2) and (a1==a-2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1

def ka12(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if ka12_jumpkill(a,b,a1,b1)==1:
        return 'k'
    elif ka12_canter(a,b,a1,b1)==1:
        return 'm'
    else:
        if(b1<14 and player==1):    #attack area
            if(a<14):    #non lane area
                if (((a1!=a) and (a1!=a-1)) or ((b1!=b) and (b1!=b+1))):
                    return 0
            elif(a==14)or (a==15):   #lane area
                if((a1!=14) and (a1!=15)) or ((b1!=b+1)):
                    return 0

        elif (b1>=14 and player==1):    #defense area
             if (a>10):
                 if (((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b+1)) ):
                     return 0
             elif (a<9):
                 if (((a1!=a)  and (a1!=a+1)) or ((b1!=b) and (b1!=b+1)) ):
                     return 0
             elif(a==9 or a==10):
                    if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b+1)) ):
                         return 0
        return 'm'

def bd1123_jumpkill(a,b,a1,b1):
    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==2 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==2 and occupied(a+2,b+2)==0:

        return 1

    elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==2 and occupied(a,b+2)==0:

        return 1

    elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==2 and occupied(a+2,b)==0:

        return 1
    elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==2 and occupied(a+2,b)==0:

        return 1

def bd1123(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if(b1<14):
        return 0
    if(defense_occupied()==0):
        return 0
    if bd1123_jumpkill(a,b,a1,b1)!=1:
        if((a1!=a-1) or (a1!=a) or (a1!=a+1)) and ((b1!=b-1) or (b1!=b) or (b1!=b+1)):
            return 0
        return 'm'
    else:
        return 'k'

def bd2123_jumpkill(a,b,a1,b1):
    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

        return 1

    elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1and occupied(a,b+2)==0:

        return 1

    elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

        return 1
    elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==1 and occupied(a+2,b)==0:

        return 1

def bd2123(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if(b1<14):
        return 0
    if(defense_occupied()==0):
        return 0
    if bd2123_jumpkill(a,b,a1,b1)!=1:
        if((a1!=a-1) or (a1!=a) or (a1!=a+1)) and ((b1!=b-1) or (b1!=b) or (b1!=b+1)):
            return 0
        return 'm'
    else:
        return 'k'

def kd1_jumpkill(a,b,a1,b1):
    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==2 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==2 and occupied(a+2,b+2)==0:

        return 1

    elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==2 and occupied(a,b+2)==0:

        return 1

    elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==2 and occupied(a+2,b)==0:

        return 1
    elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==2 and occupied(a+2,b)==0:

        return 1

def kd1_canter(a,b,a1,b1):
    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

        return 1

    elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1and occupied(a,b+2)==0:

        return 1

    elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

        return 1
    elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==1 and occupied(a+2,b)==0:

        return 1

def kd1(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if(b1<14):
        return 0
    if(defense_occupied()==0):
        return 0
    if (kd1_jumpkill(a,b,a1,b1)!=1 and kd1_canter(a,b,a1,b1)):
        if((a1!=a-1) or (a1!=a) or (a1!=a+1)) and ((b1!=b-1) or (b1!=b) or (b1!=b+1)):
            return 0
        return 'm'
    else:
        return 'k'


def kd2_jumpkill(a,b,a1,b1):
    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==1 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

        return 1

    elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==1 and occupied(a,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1and occupied(a,b+2)==0:

        return 1

    elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

        return 1
    elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==1 and occupied(a+2,b)==0:

        return 1

def kd2_canter(a,b,a1,b1):
    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==2 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==2 and occupied(a+2,b+2)==0:

        return 1

    elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

        return 1
    elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==2 and occupied(a,b+2)==0:

        return 1

    elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==2 and occupied(a+2,b)==0:

        return 1
    elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==2 and occupied(a+2,b)==0:

        return 1

def kd2(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if(b1<14):
        return 0
    if(defense_occupied()==0):
        return 0
    if (kd2_jumpkill(a,b,a1,b1)!=1 and kd2_canter(a,b,a1,b1)!=1):
        if((a1!=a-1) or (a1!=a) or (a1!=a+1)) and ((b1!=b-1) or (b1!=b) or (b1!=b+1)):
            return 0
        return 'm'
    else:
        return 'k'


def ba1m_jumpkill(a,b,a1,b1):
    if(player==1):
        if(b1<14):  #attack area
            if(a==9 or 10):   #middle lane
                  if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                    return 1
                  elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                    return 1
                  elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==2 and occupied(a+2,b)==0:

                    return 1
                  elif(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2:

                      return 1
            elif(a>10):   # right to the middle lane area
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b+2) and (a1==a)  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                    return 1
                elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==2 and occupied(a+2,b)==0:

                    return 1
            elif(a<9): #left of the middle lane
                if(b1==b+2) and (a1==a)  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                    return 1
                elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==2 and occupied(a+2,b)==0:

                    return 1
                elif(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2:

                      return 1
        elif(a==14)or (a==15):   #right lane area
                if(b1==b+2) and (a1==a) and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                    return 1
        elif(a==4)or (a==5):   #left lane area
                if(b1==b+2) and (a1==a) and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                    return 1



        if(b==13):
                if(a==14) or (a==15):
                    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1

                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2:

                        return 1

        elif(b==12):
                if(a==14):
                    if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                elif(a==15):
                    if(b1==b+2) and (a1==a-2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
        if(b==13):
            if(a==4) or (a==5):
                    if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2:

                        return 1

        elif(b==12):
            if(a==4):
                if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
            elif(a==5):
                if(b1==b+2) and (a1==a-2)  and occupied(a-1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1



        elif (b1>=14):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==14) or (b==15):
                     if(b1==b+2) and (a1==a-2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==2:

                        return 1
                if (b==16):
                    if(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b+2) and (a1==a-2)  and occupied(a+1,b+1)==2 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b+2) and a1==a  and occupied(a,b+1)==2 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a+1,b)==2 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b+2) and (a1==a+2)  and occupied(a+1,b+1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b+2) and a1==a  and occupied(a,b+1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1
                 elif(a==4)or (a==5):   #lane area
                    if(b1==b+2) and (a1==a) and occupied(a,b+1)==2 and occupied(a,b+2)==0:

                     return 1
    return 0

def ba1m (a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0

    if ba1m_jumpkill(a,b,a1,b1)!=1:
        if(b1<14 and player==1):    #attack area
            if(a==9 or 10):    #middle lane area
                if (((a1!=a) and (a1!=a-1) and (a1!=a+1)) or ((b1!=b+1))):
                    return 0
            elif(a>10):   # right to the middle lane area
                if (((a1!=a) and (a1!=a+1))) or (((b1!=b)and(b1!=b+1))):
                    return 0
            elif(a<9): #left to the middle lane area
                if (((a1!=a) and (a1!=a-1))) or (((b1!=b)and(b1!=b+1))):
                    return 0
            elif(a==4)or (a==5):   # left lane area
                if((a1!=4) and (a1!=5)) or ((b1!=b+1)):
                    return 0
            elif(a==14)or (a==15):   # right lane area
                if((a1!=14) and (a1!=15)) or ((b1!=b+1)):
                    return 0


        elif (b1>=14 and player==1):    #defense area
             if (a1>10):
                if(((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b+1)) ):
                        return 0

             elif (a1<9):

                if (((a1!=a)  and  (a1!=a+1)) or ((b1!=b) and (b1!=b+1)) ):
                        return 0
             else:
                  if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b+1)) ):
                     return 0
        return 'm'
    else:
        return 'k'


def ba2m_jumpkill(a,b,a1,b1):
    if(player==1):
        if(b1>5):  #attack area
            if(a==9 or 10):   #middle lane
                  if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0:

                    return 1
                  elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                    return 1
                  elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

                    return 1
                  elif(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a-2,b-2)==0:

                      return 1
            elif(a>10):   # right to the middle lane area
                if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0:

                    return 1
                elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                    return 1
                elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

                    return 1
            elif(a<9): #left of the middle lane
                if(b1==b-2) and (a1==a)  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                    return 1
                elif(a1==a+2) and (b1==b)  and occupied(a+1,b)==1 and occupied(a+2,b)==0:

                    return 1
                elif(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a-2,b-2)==0:

                      return 1
        elif(a==14)or (a==15):   #right lane area
                if(b1==b-2) and (a1==a) and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                    return 1
        elif(a==4)or (a==5):   #left lane area
                if(b1==b-2) and (a1==a) and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                    return 1



        if(b==6):
                if(a==14) or (a==15):
                    if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1

                    elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
                    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a-2,b-2)==0:

                        return 1

        elif(b==7):
                if(a==14):
                    if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1
                    elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
                elif(a==15):
                    if(b1==b-2) and (a1==a-2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1
                    elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
        if(b==6):
            if(a==4) or (a==5):
                    if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1
                    elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
                    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2):

                        return 1

        elif(b==7):
            if(a==4):
                if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
            elif(a==5):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1



        elif (b1<=5):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==5) or (b==4):
                     if(b1==b-2) and (a1==a-2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1
                     elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
                     elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+1,b-2)==0:

                        return 1
                if (b==3):
                    if(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
            if (a>10):
                if(b1==b-2) and (a1==a-2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0 :

                     return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0 :

                     return 1
                 elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1
                 elif(a==4)or (a==5):   #lane area
                    if(b1==b-2) and (a1==a) and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                     return 1
    return 0

def ba2m (a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0

    if ba2m_jumpkill(a,b,a1,b1)!=1:
        if(b1>5 and player==2):    #attack area
            if(a==9 or 10):    #middle lane area
                if (((a1!=a) and (a1!=a-1) and (a1!=a+1)) or ((b1!=b-1))):
                    return 0
            elif(a>10):   # right to the middle lane area
                if (((a1!=a) and (a1!=a+1))) or (((b1!=b)and(b1!=b-1))):
                    return 0
            elif(a<9): #left to the middle lane area
                if (((a1!=a) and (a1!=a-1))) or (((b1!=b)and(b1!=b-1))):
                    return 0
            elif(a==4)or (a==5):   # left lane area
                if((a1!=4) and (a1!=5)) or ((b1!=b-1)):
                    return 0
            elif(a==14)or (a==15):   # right lane area
                if((a1!=14) and (a1!=15)) or ((b1!=b-1)):
                    return 0


        elif (b1<=5 and player==2):    #defense area
             if (a1>10):
                if(((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b-1)) ):
                        return 0

             elif (a1<9):

                if (((a1!=a)  and  (a1!=a+1)) or ((b1!=b) and (b1!=b-1)) ):
                        return 0
             else:
                  if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b-1)) ):
                     return 0
        return 'm'
    else:
        return 'k'


def ka22_jumpkill(a,b,a1,b1):
      if(player==2):
        if(b1>5):    #attack area
            if(a>5):    #non lane area
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                    return 1
                elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                    return 1
                elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==1 and occupied(a+2,b)==0:

                    return 1
            elif(a==4)or (a==5):   #lane area
                if(b1==b-2) and (a1==a) and occupied(a,b-1)==1and occupied(a,b+2)==0:

                    return 1
        elif(b==6):
            if(a==4) or (a==5):
                    if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                    elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
                    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:

                        return 1

        elif(b==7):
            if(a==4):
                if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
            elif(a==5):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1

        elif (b1<=5):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==5) or (b==4):
                     if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0:

                        return 1
                     elif(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
                     elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:

                        return 1
                if (b==3):
                    if(b1==b-2) and a1==a  and occupied(a,b-1)==1and occupied(a,b+2)==0:

                        return 1
            if (a>10):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b+2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==1 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b+2)==0 :

                     return 1
                 elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b+2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1

def ka22_canter(a,b,a1,b1):

 if(player==2):
        if(b1>5):    #attack area
            if(a>5):    #non lane area
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b-2)==0:

                    return 1
                elif(b1==b-2) and (a1==a)  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                    return 1
                elif(a1==a-2) and (b1==b)  and occupied(a-1,b)==1 and occupied(a+2,b)==0:

                    return 1
            elif(a==4)or (a==5):   #lane area
                if(b1==b-2) and (a1==a) and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                    return 1
        elif(b==6):
            if(a==4) or (a==5):
                    if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1
                    elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
                    elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:

                        return 1

        elif(b==7):
            if(a==4):
                if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:# :#and occupied(a+2,b-2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
            elif(a==5):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1

        elif (b1<=5):    #defense area
            if(a==9 or a==10): #throne lane
                if (b==5) or (b==4):
                     if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b-2)==0:

                        return 1
                     elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
                     elif(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1:

                        return 1
                if (b==3):
                    if(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0:

                        return 1
            if (a>10):
                if(b1==b-2) and (a1==a-2)  and occupied(a-1,b-1)==1 and occupied(a+2,b-2)==0 :

                     return 1
                elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0 :

                     return 1
                elif(a1==a-2) and b1==b  and occupied(a-1,b)==1 and occupied(a+2,b)==0 :

                     return 1
            if(a<9):
                 if(b1==b-2) and (a1==a+2)  and occupied(a+1,b-1)==1 and occupied(a+2,b-2)==0 :

                     return 1
                 elif(b1==b-2) and a1==a  and occupied(a,b-1)==1 and occupied(a,b-2)==0 :

                     return 1
                 elif(a1==a+2) and b1==b  and occupied(a+1,b)==1 and occupied(a+2,b)==0 :

                     return 1

def ka22(a,b,a1,b1):




    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
         return 0
    if ka21_jumpkill(a,b,a1,b1)==1:
        return 'k'
    elif ka21_canter(a,b,a1,b1)==1:
        return 'm'
    else:
        if(b1>5 and player==2):    #attack area
            if(a>5):    #non lane area
                if (((a1!=a) and (a1!=a-1)) or ((b1!=b) and (b1!=b-1))):
                    return 0
            elif(a==4)or (a==5):   #lane area
                if((a1!=4) and (a1!=5)) or ((b1!=b-1)):
                    return 0

        elif (b1<=5 and player==2):    #defense area
             if (a>10):
                 if (((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b-1)) ):
                     return 0
             elif (a<9):
                 if (((a1!=a)  and (a1!=a+1)) or ((b1!=b) and (b1!=b-1)) ):
                     return 0
             elif(a==9 or a==10):
                    if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b-1)) ):
                         return 0
        return 'm'


def dragon1_fly(a,b,a1,b1):
    a2=a
    b2=b

    if(player==1):
        if(b1<14):  #attack area

            if(a==9 or 10):   #middle lane
                  if(a1==a) and occupied(a,b+1)==1:
                      while occupied(a,b2+1)==1:
                          b2=b+1
                      b2=b2+1
                      if (b1==b2):
                          return 1


            if(a<9): #left of the middle lane
                if(a>5):
                    if(a1==a) and occupied(a,b+1)==1:
                          while occupied(a,b2+1)==1:
                              b2=b+1
                          b2=b2+1
                          if (b1==b2):
                              return 1
                    if(b1==b) and occupied(a-1,b)==1:
                        while occupied(a2-1,b)==1:
                            a2=a-1
                        a2=a2-1
                        if(a1==a2):
                            return 1


                if(a==4 or a==5):
                     if(a1==a) and occupied(a,b+1)==1:
                        while occupied(a,b2+1)==1:
                             b2=b+1
                        b2=b2+1
                        if (b1==b2):
                          return 1


                if(a<4):
                    if(a1==a) and occupied(a,b+1)==1:
                        while occupied(a,b2+1)==1:
                             b2=b+1
                        b2=b2+1
                        if (b1==b2):
                          return 1
                    if(b1==b) and occupied(a+1,b)==1:
                        while occupied(a2+1,b)==1:
                            a2=a+1
                        a2=a2+1
                        if(a1==a2):
                            return 1
            if(a>10):    # right of the middle lane
                if(a<14):
                    if(a1==a) and occupied(a,b+1)==1:
                        while occupied(a,b2+1)==1:
                             b2=b+1
                        b2=b2+1
                        if (b1==b2):
                          return 1
                    if(b1==b) and occupied(a+1,b)==1:
                        while occupied(a2+1,b)==1:
                            a2=a+1
                        a2=a2+1
                        if(a1==a2):
                            return 1
                if(a==14 or a==15):
                     if(a1==a) and occupied(a,b+1)==1:
                        while occupied(a,b2+1)==1:
                             b2=b+1
                        b2=b2+1
                        if (b1==b2):
                          return 1
                if(a>15):
                     if(a1==a) and occupied(a,b+1)==1:
                          while occupied(a,b2+1)==1:
                            b2=b+1
                          b2=b2+1
                          if (b1==b2):
                            return 1
                     if(b1==b) and occupied(a-1,b)==1:
                        while occupied(a2-1,b)==1:
                            a2=a-1
                        a2=a2-1
                        if(a1==a2):
                            return 1
        if(b1>=14):

                if(a<9): # left of the throne lane
                    if(a1==a) and occupied(a,b+1)==1:
                          while occupied(a,b2+1)==1:
                            b2=b+1
                          b2=b2+1
                          if (b1==b2):
                            return 1
                    elif(b1==b) and occupied(a+1,b)==1:
                        while occupied(a2+1,b)==1:
                            a2=a+1
                        a2=a2+1
                        if(a1==a2):
                            return 1
                elif(a>10): # right of the throne lane
                    if(a1==a) and occupied(a,b+1)==1:
                          while occupied(a,b2+1)==1:
                            b2=b+1
                          b2=b2+1
                          if (b1==b2):
                            return 1
                    elif(b1==b) and occupied(a-1,b)==1:
                        while occupied(a2-1,b)==1:
                            a2=a-1
                        a2=a2-1
                        if(a1==a2):
                            return 1
                elif(a==9 or a==10):
                     if(a1==a) and occupied(a,b+1)==1:
                          while occupied(a,b2+1)==1:
                            b2=b+1
                          b2=b2+1
                          if (b1==b2):
                              return 1




def dragon1_kill(a,b,a1,b1):
    if(player==1):
        if(b<14 and b1<14 ):#attack area
            if(a1==a and b1==b+3 and occupied(a,b+2)!=0 and occupied(a,b+3)!=0):
               return 2
        if(a<9):
            if(b1==b and a1==a+3 and occupied(a,b+2)!=0 and occupied(a,b+3)!=0):
                return 2
        elif(a==9 or a==10):
            if(a1==a and b1==b+3 and occupied(a,b+2)!=0 and occupied(a,b+3)!=0):
               return 2
        elif(a>10):
            if(b1==b and a1==a-3 and occupied(a,b+2)!=0 and occupied(a,b+3)!=0):
                 return 2

        if(b>=14 and player==1):
            if(b==14):
                if(a1==a and b1==b+3 and occupied(a,b+2)!=0 and occupied(a,b+3)!=0):
                    return 2


def dragon1 (a,b,a1,b1):

    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if dragon1_fly(a,b,a1,b1)!=1:
        if(player==1):
            if(b1<14):    #attack area
                if(a==9 or 10):    #middle lane area
                    if (((a1!=a) and (a1!=a-1) and (a1!=a+1))) or (((b1!=b+1))):
                        return 0
                elif(a>10):   # right to the middle lane area
                    if(a<14):

                        if (((a1!=a) and (a1!=a+1))) or (((b1!=b)and(b1!=b+1))):
                            return 0

                    elif(a==14)or (a==15):   # right lane area
                        if((a1!=14) and (a1!=15)) or ((b1!=b+1)):
                            return 0
                    elif(a>15):
                        if (((a1!=a) and (a1!=a-1))) or (((b1!=b)and(b1!=b+1))):
                            return 0


                elif(a<9): #left to the middle lane area
                    if(a>5):
                        if (((a1!=a) and (a1!=a-1))) or (((b1!=b)and(b1!=b+1))):
                            return 0
                    elif(a==4)or (a==5):   # left lane area
                        if((a1!=4) and (a1!=5)) or ((b1!=b+1)):
                            return 0
                    elif(a<4):
                        if (((a1!=a) and (a1!=a+1))) or (((b1!=b)and(b1!=b+1))):
                            return 0



            elif (b1>=14 and player==1):    #defense area

                     if (a1>10):
                        if(((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b+1)) ):
                                return 0

                     elif (a1<9):

                        if (((a1!=a)  and  (a1!=a+1)) or ((b1!=b) and (b1!=b+1)) ):
                                return 0
                     else:
                          if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b+1)) ):
                             return 0

            return 'm'
        elif(dragon1_kill(a,b,a1,b1)==2):
            return 'k'
        else:
            return 'm'
__author__ = 'Apoorv c'
#for player 2 dragon

def dragon2_fly(a,b,a1,b1):
    a2=a
    b2=b

    if(player==2):
        if(b1>5):  #attack area

            if(a==9 or 10):   #middle lane
                  if(a1==a) and occupied(a,b-1)==1:
                      while occupied(a,b2-1)==1:
                          b2=b-1
                      b2=b2-1
                      if (b1==b2):
                          return 1


            if(a<9): #left of the middle lane
                if(a>5):
                    if(a1==a) and occupied(a,b-1)==1:
                          while occupied(a,b2-1)==1:
                              b2=b-1
                          b2=b2-1
                          if (b1==b2):
                              return 1
                    if(b1==b) and occupied(a-1,b)==1:
                        while occupied(a2-1,b)==1:
                            a2=a-1
                        a2=a2-1
                        if(a1==a2):
                            return 1


                if(a==4 or a==5):
                     if(a1==a) and occupied(a,b-1)==1:
                        while occupied(a,b2-1)==1:
                             b2=b-1
                        b2=b2-1
                        if (b1==b2):
                          return 1


                if(a<4):
                    if(a1==a) and occupied(a,b-1)==1:
                        while occupied(a,b2-1)==1:
                             b2=b-1
                        b2=b2-1
                        if (b1==b2):
                          return 1
                    if(b1==b) and occupied(a+1,b)==1:
                        while occupied(a2+1,b)==1:
                            a2=a+1
                        a2=a2+1
                        if(a1==a2):
                            return 1
            if(a>10):    # right of the middle lane
                if(a<14):
                    if(a1==a) and occupied(a,b-1)==1:
                        while occupied(a,b2-1)==1:
                             b2=b-1
                        b2=b2-1
                        if (b1==b2):
                          return 1
                    if(b1==b) and occupied(a+1,b)==1:
                        while occupied(a2+1,b)==1:
                            a2=a+1
                        a2=a2+1
                        if(a1==a2):
                            return 1
                if(a==14 or a==15):
                     if(a1==a) and occupied(a,b-1)==1:
                        while occupied(a,b2-1)==1:
                             b2=b-1
                        b2=b2-1
                        if (b1==b2):
                          return 1
                if(a>15):
                     if(a1==a) and occupied(a,b-1)==1:
                          while occupied(a,b2-1)==1:
                            b2=b-1
                          b2=b2-1
                          if (b1==b2):
                            return 1
                     if(b1==b) and occupied(a-1,b)==1:
                        while occupied(a2-1,b)==1:
                            a2=a-1
                        a2=a2-1
                        if(a1==a2):
                            return 1
        if(b1<=5):

                if(a<9): # left of the throne lane
                    if(a1==a) and occupied(a,b-1)==1:
                          while occupied(a,b2-1)==1:
                            b2=b-1
                          b2=b2-1
                          if (b1==b2):
                            return 1
                    elif(b1==b) and occupied(a+1,b)==1:
                        while occupied(a2+1,b)==1:
                            a2=a+1
                        a2=a2+1
                        if(a1==a2):
                            return 1
                elif(a>10): # right of the throne lane
                    if(a1==a) and occupied(a,b-1)==1:
                          while occupied(a,b2-1)==1:
                            b2=b-1
                          b2=b2-1
                          if (b1==b2):
                            return 1
                    elif(b1==b) and occupied(a-1,b)==1:
                        while occupied(a2-1,b)==1:
                            a2=a-1
                        a2=a2-1
                        if(a1==a2):
                            return 1
                elif(a==9 or a==10):
                     if(a1==a) and occupied(a,b-1)==1:
                          while occupied(a,b2-1)==1:
                            b2=b-1
                          b2=b2-1
                          if (b1==b2):
                              return 1




def dragon2_kill(a,b,a1,b1):
    if(player==2):
        if(b1>5 and b>5):#attack area
            if(a1==a and b1==b-3 and occupied(a,b-2)!=0 and occupied(a,b-3)!=0):
               return 2
        if(a<9):
            if(b1==b and a1==a+3 and occupied(a,b-2)!=0 and occupied(a,b-3)!=0):
                return 2
        elif(a==9 or a==10):
            if(a1==a and b1==b-3 and occupied(a,b-2)!=0 and occupied(a,b-3)!=0):
               return 2
        elif(a>10):
            if(b1==b and a1==a-3 and occupied(a,b-2)!=0 and occupied(a,b-3)!=0):
                 return 2

        if(b<=5):
            if(b==5):
                if(a1==a and b1==b-3 and occupied(a,b-2)!=0 and occupied(a,b-3)!=0):
                    return 2


def dragon2 (a,b,a1,b1):

    if out_of_grid(a1,b1)==1:
        return 0
    if black_area(a1,b1)==1:
        return 0
    if same(a,b,a1,b1)==1:
        return 0
    if occupied(a1,b1)!=0:
        return 0
    if dragon2_fly(a,b,a1,b1)!=1:
        if(player==2):
            if(b1>5):    #attack area
                if(a==9 or 10):    #middle lane area
                    if (((a1!=a) and (a1!=a-1) and (a1!=a+1))) or (((b1!=b-1))):
                        return 0
                elif(a>10):   # right to the middle lane area
                    if(a<14):

                        if (((a1!=a) and (a1!=a+1))) or (((b1!=b)and(b1!=b-1))):
                            return 0

                    elif(a==14)or (a==15):   # right lane area
                        if((a1!=14) and (a1!=15)) or ((b1!=b-1)):
                            return 0
                    elif(a>15):
                        if (((a1!=a) and (a1!=a-1))) or (((b1!=b)and(b1!=b-1))):
                            return 0


                elif(a<9): #left to the middle lane area
                    if(a>5):
                        if (((a1!=a) and (a1!=a-1))) or (((b1!=b)and(b1!=b-1))):
                            return 0
                    elif(a==4)or (a==5):   # left lane area
                        if((a1!=4) and (a1!=5)) or ((b1!=b-1)):
                            return 0
                    elif(a<4):
                        if (((a1!=a) and (a1!=a+1))) or (((b1!=b)and(b1!=b-1))):
                            return 0



            elif (b1<=5):    #defense area

                     if (a1>10):
                        if(((a1!=a)  and (a1!=a-1)) or ((b1!=b) and (b1!=b-1)) ):
                                return 0

                     elif (a1<9):

                        if (((a1!=a)  and  (a1!=a+1)) or ((b1!=b) and (b1!=b-1)) ):
                                return 0
                     else:
                          if (((a1!=a)  and (a1!=a-1) and (a1!=a+1)) or ((b1!=b-1)) ):
                             return 0

            return 'm'
        elif(dragon2_kill(a,b,a1,b1)==2):
            return 'k'
        else:
            return 'm'






def grid_change(a,b,a1,b1):
    global grid
    grid[b1-1][a1-1]=grid[b-1][a-1]
    grid[b-1][a-1]='_'



def check_piece(a,b):
    global grid
    if player==1:
        for j in p1:
            if(grid[b-1][a-1]==j):
                return 1
    else:
        for i in p2:
            if(grid[b-1][a-1]==i):
                return 1


def piece_select(a,b):
    global grid
    count=0
    if player==1:
        for i in p1:
            if(grid[b-1][a-1]==i):
                return count
            count=count+1
    if player==2:
        for i in p2:
            if(grid[b-1][a-1]==i):
                return count
            count=count+1


#player=1
def main(a,b,a1,b1,pl):
    do()
    global grid
    pl=int(pl)
    global player
    player=pl
        #player=1
    a=int(a)
    b=int(b)
    a1=int(a1)
    b1=int(b1)



 #   print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in grid]))
   # a=int(input("enter x coordinate(1-18) of the piece "))
    #b=int(input("enter y coordinate(1-18) of the piece "))
    #print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in grid]))
    if(check_piece(a,b)!=1):
        return 0
    else:
       # print("enter the coordinates where the piece should move/attack")
     #   a1=int(input("enter x coordinate(1-18) of the piece "))
      #  b1=int(input("enter y coordinate(1-18) of the piece "))
        ch=piece_select(a,b)
        if(player==1):
            if(ch==0):
                finalreturn=dragon1(a,b,a1,b1)
                return finalreturn
            elif(ch==1 or ch==2 or ch==3):
                finalreturn=bd1123(a,b,a1,b1)
            elif(ch==4):
                finalreturn=ba1m(a,b,a1,b1)
                return finalreturn
            elif(ch==5):
                finalreturn=ba1lr(a,b,a1,b1)
                return finalreturn
            elif(ch==6):
                finalreturn=ba1ll(a,b,a1,b1)
                return finalreturn

            elif(ch==7):
                finalreturn=kd1(a,b,a1,b1)
                return finalreturn
            elif(ch==8):
                finalreturn=ka11(a,b,a1,b1)
                return finalreturn
            elif(ch==9):
                finalreturn=ka12(a,b,a1,b1)
                return finalreturn

        if(player==2):

            """ print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in grid]))
            a=int(input("enter x coordinate(1-18) of the piece "))
            b=int(input("enter y coordinate(1-18) of the piece "))
            #print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in grid]))"""
            if(check_piece(a,b)!=1):
                return 0
            else:
                """print("enter the coordinates where the piece should be moved")
                a1=int(input("enter x coordinate(1-18) of the piece "))
                b1=int(input("enter y coordinate(1-18) of the piece "))"""
                if(ch==0):
                    finalreturn=dragon2(a,b,a1,b1)
                    return finalreturn
                elif(ch==1 or ch==2 or ch==3):
                    finalreturn=bd2123(a,b,a1,b1)
                    return finalreturn
                elif(ch==4):
                    finalreturn=ba2m(a,b,a1,b1)
                    return finalreturn
                elif(ch==5):
                    finalreturn=ba2lr(a,b,a1,b1)
                    return finalreturn
                elif(ch==6):
                    finalreturn=ba2ll(a,b,a1,b1)
                    return finalreturn
                elif(ch==7):
                    finalreturn=kd2(a,b,a1,b1)
                    return finalreturn
                elif(ch==8):
                    finalreturn=ka21(a,b,a1,b1)
                    return finalreturn
                elif(ch==9):
                    finalreturn=ka22(a,b,a1,b1)
                    return finalreturn


p1=["h1","bd11","bd12","bd13","ba1m","ba1lr","ba1ll","kd1",'ka11','ka12']
p2=['h2','bd21','bd22','bd23','ba2m','ba2lr','ba2ll','kd2','ka21','ka22']
#verdict=main(7,6,7,7,1)
#call main() and pass arguments
#print(verdict)
