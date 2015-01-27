/* Command Line Interface 
 
    by John Mark Stanley 

	Written as an assignment for Dr Robert Trenary in Computer Science 2240 
		at Western Michigan University
			error.c and makeargv provided by Dr Trenary
		
	Assistance with Piping from Jonathan Leffler on stackoverflow.com

	ourhdr.h is from "Advanced Programming in the UNIX Enviroment"
		Written by W. Richard Stevens and Stephen A. Rago


	 
*/
		 


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <unistd.h>
#include "ourhdr.h"
 
extern int makeargv(char *, char * , char ***);

int main()  
{	
	char buf[80];
	pid_t pid;
	char * clrOnStrt[2];
	clrOnStrt[0] = "clear";
	clrOnStrt[1] = NULL;
	int fds;
	pid = fork();
	if (pid < 0)
	{
			err_sys("(@_@) ERROR - forkfailed");
	}
	if(pid == 0)
	{
		execvp(clrOnStrt[0],&clrOnStrt[0]);
		exit(1);	
	}
	waitpid(pid,NULL , 0);
 
	fflush(stdout);
	//printf("\n            <(^_^)> \n  Hello, \n I am Pickle and I am here to help you \n");
	printf("\n       <(^_^)> \nCommand Line interface\n     Created by\n John Mark Stanley\n\n");
	
	printf("Type: \"exit\" to close.\n");
	printf("Type: \"help\" for help.\n");
	fflush(stdout);
	write(1,"\n(>^_^)> ",8);
	while(strcmp(fgets(buf, 80, stdin), "exit\n")!=0 )
	{	
		char **argp;	
		int pnum;  
		int i; 
		int fdleft[2] = { -1, -1};
		int fdright[2] = {-1, -1};
		int ploc[16];
		int out = 0; 
		int in = 0;
		int outloc = 0;
		int const stanin = dup(0);
		int const stanout = dup(1);

			//makeargv was provided by Dr Trenary.
		int j=makeargv(buf," \n",&argp); 

  		pnum = 0;
		ploc[0] = 0;
		if (j > 16) j = 16;
		for (i=0;i<j;i++)
		{
			if ( strcmp(argp[i], "|") == 0)
			{
				argp[i]= NULL;
				ploc[pnum+1] = (i+1);
				pnum++;
			}
			else if (strcmp(argp[i], ">") == 0)
			{
				argp[i] = NULL;
				outloc = i+1;
				out = 1;
			}
			else if(strcmp(argp[i],"<") == 0)
			{
				in = 1;
				argp[i] = NULL;	
			}
			//printf("%s is on ploc:%d  pnum = %d\n",argp[i],i,pnum);
		
		} 
				
		//srand(time(NULL));	
        //rain = rand() % 10;
		if (strcmp(argp[0],"cd")== 0)
		{
			printf(" <('o')> changing directory!\n");
			changedirect(argp[1]);
			fflush(stdout);	
		}
		else if (strcmp(argp[0], "help") ==0)
		{
			printf("     (o_O) \n ----help----\n");
			printf(" some commands\n");
			printf("  use \"cd\" to Changes the directory\n");
			printf("  use \"ls\" to lists everything in the current directory\n");
			printf("  use \"exit\" to Close this program\n");
			printf(" redirection\n");
			printf("  to redirect stdout to a file use \"COMMANDS > FILE\"\n");
			printf("  to redirect stdin from a file use \"FILE < COMMANDS\"\n");

			fflush(stdout);
		}

		else
		{
		for (i = 0; i < (pnum+1); i++) 
		{	
			if(i != pnum && pnum > 0)
			{
					if(pipe(fdright) != 0)
						err_sys("<(@_@)> ERROR - Pipe");
			}
	
			if ((pid = fork()) < 0)
			{			
				err_sys("<(@_@)> ERROR - Forkfailed");
			}
			else if (pid ==0)
    		{	//we are now in child
				int targ;	
				if (i != pnum)
				{
					dup2(fdright[1],1);
					close(fdright[0]);
					close(fdright[1]);
				}
				else 
				{
					if(out)
					{
						freopen(argp[outloc],"w",stdout);
					}
					else 
					{
						fflush(stdout);
						dup2(stanout, 1);
					}
				}
				
				if ( i != 0)
				{
					dup2(fdleft[0],0);
					close(fdleft[0]);	
					close(fdleft[1]);
				}
				else 
				{
					if (in)	
					{	
						freopen(argp[0],"r",stdin);
						execvp(argp[i+2],&argp[i+2]);
						write(1," (@_@) I can't do that! \n",26);
						exit(1);

					}
					else 
					{
						fflush(stdin);
						dup2(stanin, 0); 
					}	
				}	
				targ =(ploc[i]);
				execvp(argp[targ],&argp[targ]);
				write(1," (@_@) I'm sorry that is impossible!\n  Type \"help\" for assistance.\n",66);
				exit(1);
			}
			if(i != 0)		
			{
				close (fdleft[0]);
				close (fdleft[1]);
			}
			fdleft[0] = (fdright[0]);
			fdleft[1] = (fdright[1]);	
		}
		
		close(fdleft[0]);
		close(fdleft[1]);
		//free(argp);


		int corpse;
		int status;
	
		waitpid(pid, NULL, 0);
		}
		write(1,"\n(>^_^)> ",8);
	}
	printf(" v(^o^)^ Closing!\n");
	
}
int changedirect(char* newdir)
{
	if (chdir(newdir) != 0)
	{
		printf(" (-_-) Im sorry the directory change has failed\n");
		return -1;
	}
	printf(" THE DIR HAS CHANGED (^_^)!");
	return 0;
}
