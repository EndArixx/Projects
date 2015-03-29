package code 

/**
* Dijkstra's Algorithm.
* 
* Implemented in Scala by John Stanley 
*/


class Dijkstras(instart: String , intarget: String, inedges: List[scala.collection.immutable.Map[String,Any]])
{
  //note: List[scala.collection.immutable.Map[String,Any]
  
  
  
  var edges = inedges
  var start = instart
  var target = intarget
  def ShortestPath()//graph : Array[Int], source : Int)
  {
		val graph = new Array[Int](2)
		graph(0) = 0;
		graph(1) = 1;
		
		val source = 0
		//Sudo code from Wikipedia
			//    http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
		//function Dijkstra(Graph, source):
  
        //dist[source] ← 0                       // Distance from source to source
		val distance = new Array[Int](graph.length)
		/*distance(9) = 17
		println(distance(9));*/
		
		//prev[source] ← undefined               // Previous node in optimal path initialization
		val previous = new Array[Int](graph.length)  
		
        //for each vertex v in Graph:  // Initialization
        for(v <- graph)
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
            
         //end for
        }
        //while Q is not empty:
            //u ← vertex in Q with min dist[u]  // Source node in first case
            //remove u from Q 
            
            //for each neighbor v of u:           // where v is still in Q.
                //alt ← dist[u] + length(u, v)
                //if alt < dist[v]:               // A shorter path to v has been found
                    //dist[v] ← alt 
                    //prev[v] ← u 
                //end if
            //end for
        //end while
  
        //return dist[], prev[]
  
    //end function
	println("Finished")
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



