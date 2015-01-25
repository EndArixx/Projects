####################################################
#		  John Stanley			   #
#		   Asignment 4			   #
#		     Python			   #
#                    Bk-Tree			   #
####################################################
import string
import random
import time
#BKTREE<><><><><><><><><><><><><><><><><><><><><><><><><><><><>
class Bktree:
	#Psudo code for BK Tree provided by
		#Nick Johnson 4/2/07 - blog.notdot.net
		#ahuup 2009 - github.com 
	#constructor
		# takes the thing that
		# 	gets the distance as distfunc
	def __init__(self,distfunc, listofwords):
				#set distfunc
		self.distfunc = distfunc
				#by making list of words
				#an iterable we can move
				#through it with the 
				#next command	
		listofwords = iter(listofwords)
				#grab the root from the
				#first spot in out list
				#of words
		rootnode = listofwords.next()
				#add it to the tree
		self.tree = (rootnode, {})
		
				#add the rest with the 
				#list adder
		self.addlist(listofwords)
#----------------------------------------------------------		
				#adds a list of items to
				#the bk tree and it can
				#be used after constructer
	def addlist(self, listofwords):
				#loop for the items
                        	#in out list
		for i in listofwords:
				#add each item to the tree
			self.addNode(i,self.tree)	
#-----------------------------------------------------------
	#add and inputed item to the node recursivly 
	def addNode(self, targetNode, parentNode):		
				#get current data
		currentdata, childNodes = parentNode
				#calc the distace
		distance = self.distfunc(targetNode,currentdata)
				#is this spot taken?
					#if yes keep looking
		if distance in childNodes:
				#recursion
			self.addNode(targetNode, childNodes[distance])
					#if no then use this spot 
		else:
			childNodes[distance] = (targetNode, {})
#-------------------------------------------------------------
	#searchs the tree and returns all words within the Maxdist
	def search(self,target, maxdist):
		def rec(parentNode):
				#get the currentdata
                	currentdata, childNodes = parentNode
				#calc the distance 
			distance = self.distfunc(target, currentdata)
				#prepare the output
			out = []
				#if distance is less then
				# or at maxdist
				#then put i in output
			if distance <= maxdist:
				out.append((distance,currentdata))
			
				#loop for for allowable range
			for i in range(distance-maxdist, distance+maxdist+1):
				#check each node
				node = childNodes.get(i)

				#if it isnt null 
				#then add
				if node is not None:
					out.extend(rec(node))
				#spit the data out
			return out
				#order it then respit
		return sorted(rec(self.tree))
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


#LENGTHOFDISTBETLINES<><><><><><><><><><><><><><><><><><><><><>
def retlen(a,b):
				#gets the length of each
	alen = len(a)
	blen = len(b)
				#calc the abs value of the 
				#distance between words
	
				#if a is bigger return a-b+1
	if alen > blen:	
		out = alen - blen
		out = out + 1
		return out
				#if b is bigger return b-1+1
	elif blen > alen:
		out = blen - alen
		out = out + 1
		return out
	else:			#if even return 1
		return 1
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> 



#BRUTEFORCESEARCH<><><><><><><><><><><><><><><><><><><><><><><>
	#uses a linear search to search the entire list
def brutus(target, listofwords, distfunc,n):
	return [i for i in listofwords if distfunc(i,target) <= n]
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> 

#TIMER><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#DOESNT WORK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def timer(func, *args):
				#record current time
	tyme = time.time()
				#run the function
	out = func(*args) 
				#print current time - start
	print "time taken:", (time,time() - tyme)
				#kick up whatever the 
				#func returns
	return out
#BAD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


#RANDOMLISTGENERATOR><><><><><><><><><><><><><><><><><><><><><> 
	#returns a random word list of size x
	#	with words ranging in size from
	#	a to b 
def radlist(a,b,size):
				#prepare outlist
	out = []
				#loop for size
	for i in range(size):
				#new random number from a to b
		rng = random.randint(a,b)
				#only allow letters
		allowed = string.ascii_letters
				#the following was provided by ziekfiguur
				#on http://ubuntuforums.org
		randstring = ''.join([allowed[random.randint(0, len(allowed) - 1)] for x in xrange(rng)])
				#return the new list
		out.append(randstring)
	return out
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> 

def test(list):
	tree = Bktree(retlen,list)
	tree.search("tri",1)

def test2(list):
	brutus("tri",list,retlen,1)

if __name__ == "__main__":
				#create 2 random lists of words
				#one with small diff in data
	list1 = radlist(1,10,500)
				#for testing ignore
	list2 = radlist(1,10,500)	
				#one with a larch diff in the data
	list3 = radlist(1,35,5000)
				
				#small list test data
	tyme = time.time()
	tree1 = Bktree(retlen,list1)
	print "\nsetup took :" , (time.time()- tyme)

	print "\nfind tri in small list"
	
	print "\n\nbktree:"
	tyme = time.time()
	print(tree1.search("tri",1))
	print "\nBK searchtook :" , (time.time() - tyme)


	print "\n\nbruteforce"
	tyme = time.time()	
	print(brutus("tri",list1,retlen,1))
	print "\nbrute search took:" , (time.time() - tyme)



				#big list test data
	tyme = time.time()
	tree2 = Bktree(retlen,list3)
	print "\nsetup took :" , (time.time()- tyme)

	print "\nfind tri in big list"
	
	print "\n\nbktree:"
	tyme = time.time()
	print(tree2.search("tri",1))
	print "\nBK searchtook :" , (time.time() - tyme)


	print "\n\nbruteforce"
	tyme = time.time()	
	print(brutus("tri",list3,retlen,1))
	print "\nbrute search took:" , (time.time() - tyme)













