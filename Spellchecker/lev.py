'''
Created on Oct 8, 2012

@author: john stanley
'''
import sys
class MemoizeReset(object):
    #COMMENT
    def __init__(self,f):
                                #sets up cache,counter and object of levfunc
        self.f = f 
        self.counter = 0
        self.cache = {}
    def __call__(self, *args):
                                #counter++
        self.counter +=1
                                #if its already in the cache
        if args in self.cache:
                                #then just get the data
            return self.cache[args] , self.counter
                                #if that doesnt work perform the calculation(run levfunc) 
        else:
            self.cache[args] = self.f(*args) 
				#returns a touple with the first part being 
				# the number and the second being a counter
            return self.cache[args] , self.counter 
    def reset(self):
	self.counter = 0
	self.cache = {}

@MemoizeReset
def levfunc(a, b):
                                #int LevenshteinDistance(string s, string t)
                                #int len_s = length(s), len_t = length(t), cost = 0
    lenA = len(a)
    lenB = len(b)
    cost = 0
        
                                #if(len_s == 0) then      return len_t
    if lenA == 0:
        return lenB
                                # elseif(len_t == 0) then  return len_s
    elif lenB == 0:
        return lenA

				# if(s[0] == t[0]) then return (s[1..len_s], t[1..len_t])
    if a[0] == b[0]:
        return (levfunc(a[1:],b[1:])[0])
        
                                #LevenshteinDistance(s[1..len_s], t) + 1
                                #LevenshteinDistance(s, t[1..len_t]) + 1
                                #LevenshteinDistance(s[1..len_s], t[1..len_t]) + cost)
                                #minimum(^^ of that ^^)    
                                #lenA-=1 (from the front)
                                #lenB-=1 (from the front)
    outA = (levfunc(a[1:],b)[0]) + 1
    outB = (levfunc(a,b[1:])[0]) + 1	
    outC = (levfunc(a[1:],b[1:])[0]) + 1
    return min(outA, outB, outC)

	
if __name__ == '__main__':
    counter = 0
    if len(sys.argv) != 3:
        print "\n   I'm sorry you have the incorrect amount of Arguments"
    elif sys.argv[1] == "-f":
                                #this one uses a file
        gfile = True
        try:
            f = open(sys.argv[2])
        except IOError:
            print "\n   I'm sorry i couldn't find the file \"", sys.argv[2],"\""
            gfile =False 
                    #prepares data for levfunc
        if gfile:
            for line in f:
                line = line.split(',')
                                    #runs levfuc and outputs
                out = levfunc(line[0].strip(),line[1].strip())
		print line[0] , " ,\t " , line[1].strip() , " ,\t " , out[0] ," ,\t ", (out[1])
		#counter = out[1]
		levfunc.reset() 
      
    else:
                                #calcs two words inputed by the user
                                #runs levfuc and outputs
	out = levfunc(sys.argv[1],sys.argv[2])
        print sys.argv[1]," ,\t ",sys.argv[2] , " ,\t " , out[0] ," ,\t ", (out[1])
    pass





