package Jstanley

import scala.collection.mutable.Queue    
import scala.collection.mutable.Stack
import scala.collection.mutable

/**
Dijkstra's Algorithm:
    Implemented by John Stanley



Function
(Make sure to import Jstanley.Dijkstras )  
  Call: 
    Jstanley.Dijkstras.run
    (
      String : Start Location
      String : Target Location 
      List[scala.collection.immutable.Map[String,Any]] : Edges
      format = Map("startLocation" -> "String", "endLocation" -> "String", "distance" -> Int)
    )


  Return:
    List[scala.collection.immutable.Map[String,Any]]
      "path"     = A string with the Path
      "distance" = An integer withe the distance
    
    (If "distance" is -1 then an error has happend and the "path" will inform you more about it.)
  

Test Run:

    Compile : scalac Dijkstras.scala

    Execute : scala Jstanley.run


for an example of its use please see the main() at the bottom of this file.
*/

object Dijkstras
{
  val debug = false;
  //----------------------------------------------------------------------------------------------------------OUTER SHELL
  def run(startloc : String,  targetloc : String , edges :  List[scala.collection.immutable.Map[String,Any]])
  : scala.collection.mutable.Map[String, Any] =
  {
        //If the target is the Start, then its already done
    if(targetloc == startloc)
    {
      val output =  mutable.Map.empty[String,Any]
         output("path") = "Path: " +startloc+ "";
         output("distance") = (0)
         return(output);
    }
    
    
    var locations = mutable.Map.empty[String,Int]
    var counter = 0
       
        //build the List
        //  This creates a Map that connectes every location to a number
    for(v <- edges)
    {
      try
      {   
        if(!(locations.contains(""+v("startLocation"))))
        {
          locations(""+v("startLocation")) = (counter)
          counter += 1
        }
      } catch {
      case e: Exception =>
         val output =  mutable.Map.empty[String,Any]
         output("path") = "Error in Graph \"startlocation\" not located in: \n    " + v;
         output("distance") = (-1)
         println("Error: Closing Program\n\n");  
         return(output);
      }
      
      try
      { 
        if(!(locations.contains(""+v("endLocation"))))
        {
          locations(""+v("endLocation")) = (counter)
          counter += 1
        }
      } catch {
      case e: Exception =>
         val output =  mutable.Map.empty[String,Any]
         output("path") = "Error in Graph \"endlocation\" not located in: \n    " + v;
         output("distance") = (-1)
         println("Error: Closing Program\n\n");  
         return(output);
      }
    }
    

  
    
    var start = 0
       //this checks to make sure that the Start point is located within the graph
    try
    {          
       start = locations(startloc)
    } catch {
      case e: Exception =>
         val output =  mutable.Map.empty[String,Any]
         output("path") = "Start: \"" +startloc+ "\" is not located in the Graph.";
         output("distance") = (-1)
         println("Error: Closing Program\n\n");  
         return(output);
    }
    
    var target = 0
      //this checks to make sure that the Start point is located within the graph
    try
    {          
       target = locations(targetloc)
    } catch {
      case e: Exception =>
         val output =  mutable.Map.empty[String,Any]
         output("path") = "Target: \"" +targetloc+ "\" is not located in the Graph.";
         output("distance") = (-1)
         println("Error: Closing Program\n\n");  
         return(output);
    }
    
    
    
    val verts = new Queue[List[Int]]
      //this goes through and addeds all the locations to a List of verticies
    for(v <- edges)
    {
        var i : Int = 0
        try
        {  
              //this wil catch a non integer put as a distance
            i = v("distance").asInstanceOf[Int]
            
        } catch {
           case e: java.lang.ClassCastException =>
           val output =  mutable.Map.empty[String,Any]
           output("path") = "Error: There is a Non-Integer \""+ v("distance")+ "\" listed as a distance in the Graph"
           output("distance") = (-1)
           println("Error: Closing Program\n\n");  
           return(output);
        }
        verts += List( locations(""+v("startLocation")), locations(""+v("endLocation")),i)
    }

    val total = counter
    val graph = Array.ofDim[Queue[List[Int]]](total)
      //This creates a graph that connects all the vertices there start point 
      /*example  1:-2-4-5
      *          2:-4-3    
      * */           
    
    for(i <- 0 to (total-1))
    {
        //add a spot for every node
      graph(i) = new Queue[List[Int]]
    }
    for(i <- verts)
    {
        //add the path to its node
      graph(i(0)) += List((i(1)),i(2))
        //Two way graph
      graph(i(1)) += List((i(0)),i(2))
    }

     
   if(debug) println("Calling: ShortestPath");
     //Run Dijkstra's Algorithm
   val pathdata = shortestPath(graph, start ,total)
   
   if(debug) println("Calling: Get Path");
     //get the Path
   val route = getPath(pathdata(1),start, target)

     //Error handling for an incomplete path
   if(route.top == -1)
   {
         val output =  mutable.Map.empty[String,Any]
         output("path") = "Target: \"" +targetloc+ "\" is not connected to \"" +startloc+ "\" in the Graph.";
         output("distance") = (-1)
         println("Error: Closing Program\n\n");  
         return(output);
   }
     //this reverses the map so that you can give it a number and get a name.
   var revloc = locations.map(_.swap)
   
     //build the output
   var outpath = ""
   for(i <- route)
   {
     outpath += (revloc(i));
     if(revloc(i) != targetloc)
     {
        outpath += " => "
     }
   }
   //println(outpath);
   val output =  mutable.Map.empty[String,Any]
   output("path") = outpath;
   output("distance") = (pathdata(0)(target))
   if(debug) println("Closing Program\n\n");  
     //return 
   return(output);
  }
  //----------------------------------------------------------------------------------------------------------GET PATH
      //function Dijkstra(Graph, source):
  def getPath(previous : Array[Int], start : Int, target : Int) : Stack[Int] =
  {
      //This goes through the Previous array and builds a path to the source
      //    this function puts everything on a stack so that it will be pulled off backwards
    if(debug) println("\n   Running: getPath");
    var output = new Stack[Int]
    var current = target
  
    while(current != start)
    {
      if(current < 0)
      {
            //This will trigger if there is no path to the source
        output.push(-1)
        return(output)
      }
      else
      {
            //put the next location on the stack
        output.push(current)
        current = previous(current)
      }
    }
    output.push(current)
    if(debug) println("   Finished\n");
    return(output)
  }
  
  
  
  
  
  //----------------------------------------------------------------------------------------------------------SHORTEST PATH
  def shortestPath(graph : Array[scala.collection.mutable.Queue[List[Int]]], source : Int, total : Int) :  List[Array[Int]] =
  {
    
		if(debug) println("\n   Running: Dijkstra's Shortest Path Algorithm")
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
    //end function
	if(debug) println("   Finished\n");

  
    //return dist[], prev[]
  val output = List[Array[Int]] (distance, previous)
  return(output)
  } 
}






  //This is for testing
object run
{ 
  //----------------------------------------------------------------------------------------------------------MAIN
  def main(args: Array[String]) 
  {
     
     
    val startloc = "Kruthika's abode"
    val targetloc = "Craig's haunt" 
    val edges = List(
      Map("startLocation" -> "Kruthika's abode", "endLocation" -> "Mark's crib", "distance" -> 9),
      Map("startLocation" -> "Kruthika's abode", "endLocation" -> "Greg's casa", "distance" -> 4),
      Map("startLocation" -> "Kruthika's abode", "endLocation" -> "Matt's pad", "distance" -> 18),
      Map("startLocation" -> "Kruthika's abode", "endLocation" -> "Brian's apartment", "distance" -> 8),
      Map("startLocation" -> "Brian's apartment", "endLocation" -> "Wesley's condo", "distance" -> 7),
      Map("startLocation" -> "Brian's apartment", "endLocation" -> "Cam's dwelling", "distance" -> 17),
      Map("startLocation" -> "Greg's casa", "endLocation" -> "Cam's dwelling", "distance" -> 13),
      Map("startLocation" -> "Greg's casa", "endLocation" -> "Mike's digs", "distance" -> 19),
      Map("startLocation" -> "Greg's casa", "endLocation" -> "Matt's pad", "distance" -> 14),
      Map("startLocation" -> "Wesley's condo", "endLocation" -> "Kirk's farm", "distance" -> 10),
      Map("startLocation" -> "Wesley's condo", "endLocation" -> "Nathan's flat", "distance" -> 11),
      Map("startLocation" -> "Wesley's condo", "endLocation" -> "Bryce's den", "distance" -> 6),
      Map("startLocation" -> "Matt's pad", "endLocation" -> "Mark's crib", "distance" -> 19),
      Map("startLocation" -> "Matt's pad", "endLocation" -> "Nathan's flat", "distance" -> 15),
      Map("startLocation" -> "Matt's pad", "endLocation" -> "Craig's haunt", "distance" -> 14),
      Map("startLocation" -> "Mark's crib", "endLocation" -> "Kirk's farm", "distance" -> 9),
      Map("startLocation" -> "Mark's crib", "endLocation" -> "Nathan's flat", "distance" -> 12),
      Map("startLocation" -> "Bryce's den", "endLocation" -> "Craig's haunt", "distance" -> 10),
      Map("startLocation" -> "Bryce's den", "endLocation" -> "Mike's digs", "distance" -> 9),
      Map("startLocation" -> "Mike's digs", "endLocation" -> "Cam's dwelling", "distance" -> 20),
      Map("startLocation" -> "Mike's digs", "endLocation" -> "Nathan's flat", "distance" -> 12),
      Map("startLocation" -> "Cam's dwelling", "endLocation" -> "Craig's haunt", "distance" -> 18),
      Map("startLocation" -> "Nathan's flat", "endLocation" -> "Kirk's farm", "distance" -> 3)
    )
        //This runs the actual algorithm 
    val result = Jstanley.Dijkstras.run(startloc, targetloc, edges)
    
    println("\nDistance: " + result("distance") +" \nPath: "+ result("path"))
  }
}



