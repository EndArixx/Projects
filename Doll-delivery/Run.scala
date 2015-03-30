package Jstanley

import scala.io.Source
//import Jstanley.Dijkstras  //import algorithm
import scala.collection.mutable.Queue  
import scala.collection.mutable.Stack

      //compile:    scalac *.scala
      // run:       scala Jstanley.run 


object run{
  def main(args: Array[String]) {
    //println("Wake up Neo!")
    
    //val input = readLine("TEST: ")
       
    /*
    val filename = input
    try 
    {
        for(line <- Source.fromFile(filename).getLines())
        {
          println(line)
          
        }
    }
    catch
    {
      case ex: Exception => println("Error: file \""+ input +"\" not found.")  
    }*/
    
    val start = 0;
    val target = 11;
    


      
    
    
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
    
    
    val total = 12 //John look into this
    
    val test = List(
        List(1,5,9),
        List(1,2,4),
        List(1,6,18),
        List(1,3,8),
        List(3,4,7),
        List(3,8,17),
        List(2,8,13),
        List(2,11,19),
        List(2,6,14),
        List(4,9,10),
        List(4,10,11),
        List(4,7,6),
        List(6,5,19),
        List(6,10,15),
        List(6,12,14),
        List(5,9,9),
        List(5,10,12),
        List(7,12,10),
        List(7,11,9),
        List(11,8,20),
        List(11,10,12),
        List(8,12,18),
        List(10,9,3)
        )
        
        val graph = Array.ofDim[Queue[List[Int]]](total)
        for(i <- 0 to (total-1))
        {
          graph(i) = new Queue[List[Int]]
        }
        for(i <- test)
        {
          graph(i(0)-1) += List((i(1)-1),i(2))
            //Two way graph
          graph(i(1)-1) += List((i(0)-1),i(2))
        }
        
        /* TESING
        for(i <- graph)
        {
          for(j <- i)
          {
            print(j)
          }
          println();
        }*/
        
        
        
      /*  OUT DATED
     val graph =Array.ofDim[Int](total,total)
     for( i <- 0 to total -1)
     {
       for(j <- 0 to total -1)
       {
         graph(i)(j) = -1
       }
     }
    
     for(i <- test)
     {
       graph(i(0)-1)(i(1)-1) = i(2)
       graph(i(1)-1)(i(0)-1) = i(2)
       println((i(0)-1) +" "+(i(1)-1) +" "+ i(2));
       
     }
     
     for( i <- 0 to total -1)
     {
       for(j <- 0 to total -1)
       {
             print("  " +graph(i)(j));
       }
       println();
     }*/

     
   val dijk = new Dijkstras()
   println("Calling: ShortestPath");
	 val pathdata = dijk.ShortestPath(graph, start ,total)
   println("Calling: Get Path");
   val route = dijk.getPath(pathdata(1),start, target)
   
   for(i <- route)
   {
     print("[" +i+ "]");
   }
   println();
   
    
    
  
  println("Closing Program");  
  }
}

