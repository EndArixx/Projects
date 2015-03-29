package run

import scala.io.Source
import code.Dijkstras  //import algorithm
    
      //compile:    scalac *.scala
      // run:       scala run.test 


object test {
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
    
    //val start
    //val target 
    


      
    
    
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
    
    
    val test = List(
     
    
    
        //print out list
    //println(edges.mkString("\n"));
       //choose a specific element
    //println(edges apply 2);
    
          //test using muliple classes
    //println(new Dijkstras data)
    val dijk =  new Dijkstras("test" , "moretest", edges)
    //dijk.data()
	dijk.ShortestPath()
    
    

    
  }
}

