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
          println(graph(u)(0));
            //for each neighbor v of u:           // where v is still in Q.
          for(v <- graph(u))
          {
              
                //alt ← dist[u] + length(u, v)
              val alt = distance(u) +  v(1)
                //if alt < dist[v]:               // A shorter path to v has been found
              if(alt < distance(v(0)))
              {
                    //dist[v] ← alt 
                    //prev[v] ← u
                  distance(v(0)) = alt
                  previous(v(0)) = u
              }
              //end if   
          //end for
          }
        //end while
     }
        //return dist[], prev[]
  for(i <- distance)
  {
    println(i)
  }
  for(i <- previous)
  {
    println(i)
  }
    //end function
	println("Finished");
  } 
  
  
}



