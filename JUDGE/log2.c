#include <stdio.h>
#include <stdlib.h>
#define OUT_LOG "/home/pushkar/XOdiaZips/XOdia_20140906_last_update/JUDGE/sachin.txt"
#define GRID_BOT "/home/pushkar/XOdiaZips/XOdia_20140906_last_update/JUDGE/grid.txt"
#define GRID_VAL "/home/pushkar/XOdiaZips/XOdia_20140906_last_update/JUDGE/grid_val.txt"
struct emp
{
char bot_name;
int old_absicca;
int old_ordinate;
int absicca ;
int ordinate ;
};
int main()
{
FILE *fp,*fp1,*fp2,*fp3;
char c ;
int x1,y1,x2,y2,i,j,k,winner;
char attack;
int gameboard [18][18];
int validboard[18][18][5];
fp1=fopen (GRID_BOT,"r+");
 for (i=0;i<18;i++)
	{
	  for (j=0;j<18;j++)
      {
            if ((c=(fgetc(fp1)))!=EOF)
             gameboard [i][j]=c;
             else
             break;
        }
      }
fclose ( fp1 ) ;
struct emp e ;
scanf ("%d %d %d %d %c",&x1,&y1,&x2,&y2,&attack);
	if (attack=='z' || attack=='Z')
	{
     fp = fopen ( OUT_LOG, "a+" ) ;
     if (x1==1)
     {
		fprintf (fp,"e.%d.1 ",y1);
		if (y1==2)
		winner=1;
		else
		winner=2;
		fprintf (fp,"#.%d",winner);
		fclose(fp);
		exit(0);
	 }
	 if (x1==2)
     {
		fprintf (fp,"e.%d.2 ",y1);
			if (y1==2)
		winner=1;
		else
		winner=2;
		fprintf (fp,"#.%d",winner);
		fclose(fp);
		exit(0);
	 }
	 if (x1==3)
     {
		fprintf (fp,"e.%d.3 ",y1);
			if (y1==2)
		winner=1;
		else
		winner=2;
		fprintf (fp,"#.%d",winner);
		fclose(fp);
		exit(0);
	 }
	 if (x1==4)
     {
		fprintf (fp,"e.%d.4 ",y1);
			if (y1==2)
		winner=1;
		else
		winner=2;
		fprintf (fp,"#.%d",winner);
		fclose(fp);
		exit(0);
	 }
	}
	if (attack=='w' || attack=='W')
	{
       fp = fopen ( OUT_LOG, "a+" );
       fprintf ( fp,"#.%d",x1);
       fclose(fp);
       exit(0);
	}
    if (attack=='k')
    {
		if (gameboard[y1][x1]!='h' && gameboard[y1][x1]!='H')
    {
       fp = fopen ( OUT_LOG, "a+" ) ;
       fprintf ( fp,"%c.%d.%d.20.20 ",gameboard[(y1+y2)/2][(x1+x2)/2],(x1+x2)/2,(y1+y2)/2);
       gameboard[(y1+y2)/2][(x1+x2)/2]=48;
       gameboard[y2][x2]=gameboard[y1][x1];
       gameboard[y1][x1]=48;
       e.bot_name=gameboard[y2][x2];
    e.old_absicca=x1;
    e.old_ordinate=y1;
    e.absicca=x2;
    e.ordinate=y2;
    fprintf ( fp,"%c.%d.%d.%d.%d ",e.bot_name,e.old_absicca,e.old_ordinate,e.absicca,e.ordinate);
    fclose (fp);
    }
    else
    {
		if ((x2==x1+3 || x2==x1+2) && y1==y2)
         {
         fp = fopen ( OUT_LOG, "a+" ) ;
          fprintf ( fp,"%c.%d.%d.20.20 ",gameboard[y1][x1+3],x1+3,y1);
          fprintf ( fp,"%c.%d.%d.20.20 ",gameboard[y1][x1+2],x1+2,y1);
         gameboard[y1][x1+3]=48;
         gameboard[y1][x1+2]=48;
          fclose (fp);
		 }
        else if ((x2==x1-3 || x2==x1-2) && y1==y2 )
         {
        fp = fopen ( OUT_LOG, "a+" ) ;
        fprintf ( fp,"%c.%d.%d.20.20 ",gameboard[y2][x1-2],x1-3,y1);
        fprintf ( fp,"%c.%d.%d.20.20 ",gameboard[y2][x1-3],x1-2,y1);
         gameboard[y2][x1-2]=48;
        gameboard[y2][x1-3]=48;
         fclose (fp);
		 }
		else if (x1==x2 && (y2==y1+3 || y2==y1+2))
		{
		gameboard [y1+3][x1]=48;
		gameboard [y1+2][x2]=48;
		fp = fopen ( OUT_LOG, "a+" ) ;
		fprintf ( fp,"%c.%d.%d.20.20 ",gameboard [y1+3][x1],x1,y1+3);
        fprintf ( fp,"%d.%d.20.20 ",x1,y1+2);
        fclose (fp);
		}
    }
}
else
{
   gameboard[y2][x2]=gameboard[y1][x1];
   gameboard[y1][x1]=48;
   e.bot_name=gameboard[y2][x2];
    e.old_absicca=x1;
    e.old_ordinate=y1;
    e.absicca=x2;
    e.ordinate=y2;
fp = fopen ( OUT_LOG, "a+" ) ;
fprintf ( fp,"%c.%d.%d.%d.%d ",e.bot_name,e.old_absicca,e.old_ordinate,e.absicca,e.ordinate);
fclose ( fp ) ;
}
fp2=fopen (GRID_BOT,"w");
 for (i=0;i<18;i++)
	{
	  for (j=0;j<18;j++)
      {
         if (gameboard [i][j]>=65 && gameboard [i][j]<=91)
         {
         gameboard [i][j]+=97-65;
         fprintf (fp2,"%c",gameboard [i][j]);
         }
         else if (gameboard [i][j]>=97 && gameboard [i][j]<=(97+26))
          {
         gameboard [i][j]-=97-65;
         fprintf (fp2,"%c",gameboard [i][j]);
         }
         else if(gameboard[i][j]==35){
          gameboard[i][j]=46;
          fprintf (fp2,"%c",gameboard [i][j]);
         }
         else if(gameboard[i][j]==46){
          gameboard[i][j]=35;
          fprintf (fp2,"%c",gameboard [i][j]);
         }
         else
         fprintf (fp2,"%c",gameboard [i][j]);
      }
    }
fclose(fp2);
fp3=fopen (GRID_VAL,"r");
  for (i=0;i<18;i++)
	{
	  for (j=0;j<18;j++)
      {
		for (k=0;k<5;k++)
		{

             if ((c=(fgetc(fp3)))!=EOF)
             {
                    if (c=='_')
                    {
                     if (k!=0)
                        {
                          k=0;
                          if (j==17)
                          {
								j=0;
								++i;
                          }
                        validboard[i][++j][k]=c;
					}
					else
                         validboard[i][j][k]=c;
						break;
                    }
                    else if (c=='b' || c=='k' || c=='h')
                    {
                       if (k!=0)
                        {
                          k=0;
                          if (j==17)
                          {
								j=0;
								++i;
                          }
                        validboard[i][++j][k]=c;
					}
					else
                         validboard[i][j][k]=c;

                    }
				 else if (c=='a' || c=='d' || c=='1' || c=='2' || c=='3' || c=='l' || c=='r' || c=='m')
               {
                   validboard[i][j][k]=c;
               }
         	 }
		}
  }
}
fclose (fp3);
fp3=fopen (GRID_VAL,"w");
 if (attack=='k')
    {
		if (validboard[y1][x1][0]!='h' && validboard[y1][x1][0]!='H')
    {
         for (k=0;k<5;k++)
        {
			if (k==0)
       validboard[(y1+y2)/2][(x1+x2)/2][k]='_';
			else
			 validboard[(y1+y2)/2][(x1+x2)/2][k]='0';
			}
      for (k=0;k<5;k++)
        {
          validboard[y2][x2][k]=validboard[y1][x1][k];
        }
        for (k=0;k<5;k++)
        {
	if (k==0)
      validboard[y1][x1][k]='_';
     else
         validboard[y1][x1][k]='0';
          }
    }
    else
    {
		if ((x2==x1+3 || x2==x1+2) && y1==y2)
         {
                 for (k=0;k<5;k++)
        {
			if (k==0)
       validboard[y1][x1+3][k]='_';
			else
			 validboard[y1][x1+3][k]='0';
			}
			   for (k=0;k<5;k++)
            {
			if (k==0)
       validboard[y1][x1+2][k]='_';
			else
			 validboard[y1][x1+2][k]='0';
			}
		 }
        else if ((x2==x1-3 || x2==x1-2) && y1==y2 )
         {
                 for (k=0;k<5;k++)
        {
			if (k==0)
       validboard[y2][x1-2][k]='_';
			else
			 validboard[y2][x1-2][k]='0';
			}
			 for (k=0;k<5;k++)
        {
			if (k==0)
       validboard[y2][x1-3][k]='_';
			else
			 validboard[y2][x1-3][k]='0';
			}
		 }
		else if (x1==x2 && (y2==y1+3 || y2==y1+2))
		{
             for (k=0;k<5;k++)
        {
			if (k==0)
       validboard[y1+3][x1][k]='_';
			else
			 validboard[y1+3][x1][k]='0';
			}
		   for (k=0;k<5;k++)
        {
			if (k==0)
       validboard[y1+2][x2][k]='_';
			else
			 validboard[y1+2][x2][k]='0';
			}
		}
    }
}
else
{
    for (k=0;k<5;k++)
{
validboard[y2][x2][k]=validboard[y1][x1][k];
}
   for (k=0;k<5;k++)
{
	if (k==0)
	validboard[y1][x1][k]='_';
	else
      validboard[y1][x1][k]='0';
}
}
 for (i=0;i<18;i++)
	{
	  for (j=0;j<18;j++)
      {
		for (k=0;k<5;k++)
		{
                if (validboard[i][j][k]=='a' || validboard[i][j][k]=='b' || validboard[i][j][k]=='h' || validboard[i][j][k]=='d' || validboard[i][j][k]=='k' || validboard[i][j][k]=='1' || validboard[i][j][k]=='2' || validboard[i][j][k]=='3' || validboard[i][j][k]=='l' || validboard[i][j][k]=='r' || validboard[i][j][k]=='_' || validboard[i][j][k]=='m' )
               {
			fprintf (fp3,"%c",validboard[i][j][k]);
}
else
break;
}
}
}
fclose(fp3);
fp3=fopen (GRID_VAL,"r");
return 0;
}



