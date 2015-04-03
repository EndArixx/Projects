Dijkstra's Algorithm:
    Implemented by John Stanley



Function
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
			"path" 	   = A string with the Path
			"distance" = An integer withe the distance
		
		(If "distance" is -1 then an error has happend and the "path" will inform you more about it.)
	

Test Run:

    Compile	: scalac Dijkstras.scala

    Execute	: scala Jstanley.run
