package Jstanley

import scala.io.Source
//import Jstanley.Dijkstras  //import algorithm
import scala.collection.mutable.Queue  
import scala.collection.mutable.Stack
import scala.collection.mutable
      //compile:    scalac *.scala
      // run:       scala Jstanley.run 


object run{
  def main(args: Array[String]) 
  {
      //Make this input
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
    
    
    
    var locations = mutable.Map.empty[String,Int]
    var counter = 0
       //build the List
    for(v <- edges)
    {
      
      if(!(locations.contains(""+v("startLocation"))))
      {
        locations(""+v("startLocation")) = (counter)
        counter += 1
      }
      if(!(locations.contains(""+v("endLocation"))))
      {
        locations(""+v("endLocation")) = (counter)
        counter += 1
      }
    }
    
    val start = locations("Kruthika's abode")
    val target = locations("Craig's haunt")
    
    val verts = new Queue[List[Int]]
    for(v <- edges)
    {
      var i : Int = v("distance").asInstanceOf[Int]
      
      verts += List( locations(""+v("startLocation")), locations(""+v("endLocation")),i)
    }
    
    val total = counter
    val graph = Array.ofDim[Queue[List[Int]]](total)
    for(i <- 0 to (total-1))
    {
      graph(i) = new Queue[List[Int]]
    }
    for(i <- verts)
    {
      graph(i(0)) += List((i(1)),i(2))
        //Two way graph
      graph(i(1)) += List((i(0)),i(2))
    }

     
   val dijk = new Dijkstras()
   println("Calling: ShortestPath");
	 val pathdata = dijk.ShortestPath(graph, start ,total)
   println("Calling: Get Path");
   val route = dijk.getPath(pathdata(1),start, target)
   
   
   var revloc = locations.map(_.swap)
   for(i <- route)
   {
     print("[" +revloc(i)+ "] ");
   }
   println();
  
  
  println("Closing Program");  
  }
}

