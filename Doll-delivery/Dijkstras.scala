package code 

import scala.collection.mutable.Queue    

/**
* Dijkstra's Algorithm.
* 
* Implemented in Scala by John Stanley 
*/


class Dijkstras()//instart: String , intarget: String, inedges: List[scala.collection.immutable.Map[String,Any]])
{
  //note: List[scala.collection.immutable.Map[String,Any]
      //function Dijkstra(Graph, source):
  def ShortestPath(graph : Array[scala.collection.mutable.Queue[List[Int]]], source : Int, total : Int)
  {
    
		
    //Sudo code from Wikipedia
			//    http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

        //dist[source] ← 0                       // Distance from source to source
		val distance = new Array[Int](total)
    distance(source) = 0
		
		  //prev[source] ← undefined               // Previous node in optimal path initialization
		val previous = new Array[Int](total)  
		previous(source) = -1
    
    val Q = new Queue[Int]
    
        //for each vertex v in Graph:  // Initialization
    for(v <- 0 to total -1) //??
		{
			  //if v ≠ source            // Where v has not yet been removed from Q (unvisited nodes)
       if(v != source)
			 {
				      //dist[v] ← infinity             // Unknown distance function from source to v
              //prev[v] ← undefined            // Previous node in optimal path from source
           distance(v) = 99999999 //find max int
           previous(v) = -1
             //end if 
       }
            //add v to Q                     // All nodes initially in Q (unvisited nodes)
         Q += v
            //end for
     }
    
        //while Q is not empty:
    while(Q.length > 0)
    { 
            //u ← vertex in Q with min dist[u]  // Source node in first case
        val u = Q.dequeue
            //remove u from Q 
            
            //for each neighbor v of u:           // where v is still in Q.
        
                //alt ← dist[u] + length(u, v)
                //if alt < dist[v]:               // A shorter path to v has been found
                    //dist[v] ← alt 
                    //prev[v] ← u 
                //end if
            //end for
        //end while
     }
        //return dist[], prev[]
  
    //end function
	println("Finished");
  }
  
  
  
  
  
  /*def data() //testing 
  {
    println(instart + intarget)
    //println(edges.mkString("\n"));
    
    
      //Tests, learning to use maps
    println((edges apply 2)("distance"));
    var line1 = (edges apply 1)("startLocation")
    println(line1);
  }*/
  
  
  
  
}



