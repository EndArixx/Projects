####################################################
#		  John Stanley			   #
#		   Asignment 4			   #
#		     Python			   #
#                    Bk-Tree			   #
####################################################


from itertools import imap, ifilter
import string
import random

#The BK Tree<><><><><><><><><><><><><><><><><><><><><
class BKTree:
			#constructor
    def __init__(self, levfunct, listofwords):
			#levfunc is a fuction that returns
			#the distance between 2 words
			#using the levenstien distance
        self.levfunct = levfunct
			#adds the iterable to it
        it = iter(listofwords)


			#get put the root in it
        root = it.next()
        self.tree = (root, {})
			#add all the nodes to it
        for i in it:
            self.addNode(self.tree, i)

			#search the node for words
			#that are n distance away
    def query(self, word, n):
			
			#setup parent rec
        def rec(parent):
            pword, children = parent

			#calc dist from current node 
			#	to inputed word
            d = self.levfunct(word, pword)

        		#setup results 
	    results = []

			#if: distance is less than or 
			#	at the allowable distance
			#then: add it
            if d <= n:
                results.append( (d, pword) )

                	#loops for range of alowable
            for i in range(d-n, d+n+1):

			#gets the next child                
		child = children.get(i)

			#if its valid add it
                if child is not None:
                    results.extend(rec(child))

			#spit out the results
            return results

        		#sort by distance
        return sorted(rec(self.tree))

			#add nodes to the tree 
    def addNode(self, parent, word):
        		#parent: the node the points to the 
			#	current node
			#word: the word we are adding
	pword, children = parent

			#calc distance from current node 
			#	to the inputed word
        d = self.levfunct(word, pword)
			
			#if if the spot is taken than this
			#	node becomes the new parent
        if d in children:
            self.addNode(children[d], word)
			
			#if it isnt taken then 
			#	add the new word        
	else:
            children[d] = (word, {})



#levenshtein<><><><><><><><><><><><><><><><><><><><><
#*see assignment 3*
def levfunc(s, t):
    m, n = len(s), len(t)
    d = [range(n+1)]
    d += [[i] for i in range(1,m+1)]
    for i in range(0,m):
        for j in range(0,n):
            cost = 1
            if s[i] == t[j]: cost = 0

            d[i+1].append( min(d[i][j+1]+1,
                               d[i+1][j]+1, 
                               d[i][j]+cost) 
                           )
    return d[m][n]
#<><><><><><><><><><><><><><><><><><><><><><><><><><>

#Brute force<><><><><><><><><><><><><><><><><><><><><
				#LINEAR SEARCH W00H00!!!
def brutus(word, listofwords, levfunct,n):
	return [i for i in listofwords if levfunct(i,word) <= n]
#<><><>><><><>><>><<>><>><><>><><>><><>><>><><>><><>>

if __name__ == "__main__":
				#create 2 random lists of words
				#1 of size 3 so small diff in data
				#1 from 2,4 so huge  diff in data
	
        #find database for actual words

	with open('american-english') as f:
		listofUSWords = f.read().splitlines()

	print ("Building BKTree of US Words");
	USWordTree = BKTree(levfunc,listofUSWords)
	
	targetword = raw_input('Enter a Word:') 
	while targetword != 'quit':
		i = 0;
		print ('searching for ' + targetword)
		output = USWordTree.query(str(targetword),i)
		while not output:
			i=i+1
			if i > 9:
				print "lev 9 not found, aborting"
				break
			print "not found with a lev distance of: " +str(i-1) + " trying: " + str(i)
			output = USWordTree.query(str(targetword),i)
		print output
		targetword = raw_input('Enter a Word or "quit": ')
	print('Shutting down')
	































