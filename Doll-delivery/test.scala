import scala.io.Source

object test {
  def main(args: Array[String]) {
    println("Wake up Neo!")
    
    val filename = "randomdata.txt"
    for(line <- Source.fromFile(filename).getLines())
    {
        println(line)
    }
  }
}

