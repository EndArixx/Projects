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

        list = []
	for i in range(2000):
		#rng = random.randint(5,6)
		size = 3
		allowed = string.ascii_letters
		randomstring = ''.join([allowed[random.randint(0, len(allowed) - 1)] for x in xrange(size)])
		#print randomstring
		list1.append(randomstring)
	list2 = []
	for i in range(2000):
		rng = random.randint(1,4)
		size = rng
		allowed = string.ascii_letters
		randomstring = ''.join([allowed[random.randint(0, len(allowed) - 1)] for x in xrange(size)])
		list2.append(randomstring)






	tree1 = BKTree(levfunc,list1)
	print "FIND tri"
	print tree1.query("tri",1)
	print brutus("tri",list1,levfunc,1)

	tree2 = BKTree(levfunc,list2)
	print "FIND bat"
	print tree2.query("bat",1)
	print brutus("bat",list2,levfunc,1)


































