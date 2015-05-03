import java.io.*;
import java.net.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;


/*
 * Java exercise on threading and socket programming
 * 
main() {
	- create new thread for server (listen_thread)
    - start server to listen on tcp port 9090
	- on every incoming request, move request to its own new thread, say request_handler thread, so listen_thread is back to listening
	- For incoming requests, the request_handler thread waits for a string to be sent terminated by newline, for eg. "Hello World!\n" and the server then responds with string "ACK:" plus the original message, for eg. "ACK:Hello World!"
	  
	- while (true) {
  		- create client and establish a tcp connection to server listening on port 9090 locally
		- Send a timestamp string of form "yyyy-MM-dd HH:mm:ss" followed by newline character
		- Print to console what was sent and response from server, on separate lines.
		- send a message to server of form "Request-XX" where XX should be a random number between 00 and 99
		- print what was sent and response from server, on separate lines.
		- close connection to server	
    }
  } */

/*
 * Testing
 * 
 * This program was written with Eclipse - Luna and tested on the following computers
 * 
 * Windows 7 Professional 
 * 		AMD FX(tm)-4100 Quad-Core Porcessor 3.60 GHz
 * 		8 GB of RAM
 * 
 * Ubuntu 14.04
 * 		dell studio 15 
 * 		Intel core i5 
 * 		8 GB of RAM
 * 	
 */
public class JStanleyPort
{
		//This is for debugging.
		//when set to true the program will print out useful information to the console. 
		//things like threads starting and closing
	public static boolean debug = true;
	
	class request_handler implements Runnable
	{
		private String name;
		private Thread thread;
		Socket socket;
		request_handler(String name, Socket socket )
		{		
				//although the name isn't required, it is very useful for testing and seeing which threads are doing what.
			this.name = name;
			this.socket = socket;
		}
		@Override
		public void run() 
		{
			/*- For incoming requests,									
		 	the request_handler thread waits for a string
		  	to be sent terminated by newline, 
		  	for eg. "Hello World!\n" and the server then 
		  	responds with string "ACK:" plus the original message,
		  	for eg. "ACK:Hello World!"
			 */
			try
			{	
				
					//set up I/O Steams 
					//	Input
				InputStreamReader inputstreamreader = new InputStreamReader(socket.getInputStream());
			    BufferedReader bufferedreader = new BufferedReader(inputstreamreader);
			      	//	Output
			    PrintWriter printwriter = new PrintWriter(socket.getOutputStream(),true);
			    
			    String line = "";
			     
			    	//as long as the input isn't null and still open.
			    while ((line = bufferedreader.readLine()) != null)
			    {
			    		//take what was provided and return it with "ACK:" on the front.
			    	printwriter.println("ACK:" + line);
			    }
			      
			      	//Close everything
			    if(debug){System.out.println("      Request_handler: "+name+" - Closing connection.");}
			    bufferedreader.close();
			    inputstreamreader.close();
			    printwriter.close();
			    socket.close();
			}
				//Error Handlers 
			catch(UnknownHostException unhe){System.out.println("request_handler - UnknownHostException: " + unhe.getMessage());}
			catch(InterruptedIOException intioe){System.out.println("request_handler - Timeout while attempting to establish socket connection.");}
			catch(IOException ioe){System.out.println("request_handler - IOException: " + ioe.getMessage());}
			finally
			{
		      try{
		    	  	//ensure it closes even if the program had an error
		        socket.close();
		      }
		      catch(IOException ioe){System.out.println("request_handler - IOException: " + ioe.getMessage());}
		    }
			
		}
		public void start() 
		{
		      if (thread == null)
		      {
		    	  if(debug){System.out.println("      Request_handler: "+name+" - starting");}
		         thread = new Thread (this, name);
		         thread.start ();
		      }
		}
		
	}
	
	class listen_thread implements Runnable
	{
		private String name;
		private Thread thread;
		listen_thread(String name)
		{
			this.name = name;
		}
		@Override
		public void run() 
		{
			/*- create new thread for server (listen_thread) 			
			- on every incoming request, move request to its			
			 own new thread, say request_handler thread,
			  so listen_thread is back to listening
			  */
			
				ServerSocket serversocket = null;
			    Socket socket = null;
			    int n = 0;
			    try
			    {
	    				//establish a server socket monitoring port 9090
			    	serversocket = new ServerSocket(9090);
			    	
			    	while(true)
			    	{
					      	//wait for client
					    if((socket = serversocket.accept()) != null)
					    {

				    		socket.setSoTimeout(1000);
			    				//this creates a new thread and gives that thread the socket
					    	new request_handler("r" + n, socket).start();
					    		//for testing reasons each handler thread is given a unique number so they can be identified.
					    	n++;
					    }
			    	}
			    }
			    	//Error Handlers
			    catch(UnknownHostException unhe){System.out.println("listen_thread - UnknownHostException: " + unhe.getMessage());}
			    catch(InterruptedIOException intioe){System.out.println("listen_thread - Timeout while attempting to establish socket connection.");}
			    catch(IOException ioe){System.out.println("listen_thread - IOException: " + ioe.getMessage());}
			    finally{
			      try
			      {
			    	  	//close everything thats still open.
			    	  if(debug){System.out.println("    Closing listen_thread: " +  name );}
			    	  socket.close();
			    	  serversocket.close();
			      }
			      catch(IOException ioe){System.out.println("listen_thread - IOException: " + ioe.getMessage());}
			    }
		}
		public void start ()
		{
			if(debug){System.out.println("    Starting listen_thread: " +  name );}
	      if (thread == null)
	      {
				//start the thread
	         thread = new Thread (this, name);
	         thread.start ();
	      }
		}

	}
	
		
	public static void main(String[] args) 
	{
		if(debug){System.out.println("  Starting Program");}
		JStanleyPort j1 = new JStanleyPort();
		
		
			//this will be the Listen Thread.
		listen_thread l1 = j1.new listen_thread("Listen Thread one");
		l1.start();
			
			//variables that will be needed
	    String line = "";
	    int number;
	    Random rn = new Random();
		Socket socket = null;

			//desired port
		int serverport = 9090;
		try 
		{
				//while(true)
				//	This is dangerous but the specifications asked for it.
				//  The program will run until closed external. 
				//	The psudo code never called for an exit condition. 
				//	This is dangerous because the program may have issues when it is closed externally, so use with caution.
				//	For testing I used "for(int i = 0; i < 1000000; i++)" The program successfully reached one million completions.
			while(true)
		    {
				
		    	long start = System.nanoTime();
		    		//This ensure that the sockets have enough time for the operation system to free the socket
		    		//It is currently set to 8 milliseconds.
		    	long wait = 8000000;
		    	
		    	
					//- create client and establish a tcp connection to server listening on port 9090 locally
		
					//try to open a socket on port 9090
					//InetAddress.getByName(null) is local
		    	if(debug){System.out.println("  Connecting to " + InetAddress.getByName(null) + " on port " + serverport);}
			    socket = new Socket(InetAddress.getByName(null),serverport);
			    
			    	//wait 10 seconds for the connection.
			    socket.setSoTimeout(10000);
			    if(debug){System.out.println("  Client Connected.");}
			    
			    	//Input Reader
			    	//	This will handle all the incoming data through the port.
			    InputStreamReader inputStreamReader = new InputStreamReader(socket.getInputStream());
			    BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
			    	//Output Writer 
			    	//	This will send data up through the port.
			    PrintWriter printWriter = new PrintWriter(socket.getOutputStream(),true);
			    
			    
	
			    	

			    	//Start listening to the port
			    
					//- Send a timestamp string of form "yyyy-MM-dd HH:mm:ss" followed by newline character
					//- Print to console what was sent and response from server, on separate lines.
			    DateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
			    Date date = new Date();
			    String timestamp = format.format(date);
			    	//send the date after formatting
			    printWriter.println(timestamp);
			    System.out.println(timestamp);
			    	//print what was returned by the server.
			    line = bufferedReader.readLine();
			    System.out.println(line);
			    
	
					//- send a message to server of form "Request-XX" where XX should be a random number between 00 and 99
					//- print what was sent and response from server, on separate lines.
			    
			    	//random number between 0 and 99
			    number = rn.nextInt(100);
			    	//sends the data up the stream
				printWriter.println("Request-" + number);
				System.out.println("Request-" + number);
					//prints what was returned by the server
				line = bufferedReader.readLine();
			    System.out.println(line);
			    			    
			    	//- close connection to server
			    	//	close all readers, writers and the socket.
			    if(debug){System.out.println("  Client Closing connection.");}
			    bufferedReader.close();
			    inputStreamReader.close();
			    printWriter.close();
			    socket.close();
			    
			    while(System.nanoTime() < start + wait)
			    {
			    	/*
			    	when testing on a Windows 7 AMD FX(tm)-4100 Quad-core processor 
			    	the program ran to quickly and the operating system could not free sockets 
			    	fast enough for the program. so it had to be slowed down.
			    	this was done by ensuring the program would always take at least 8 milliseconds.
			    	
			    	this problem is because the operating system doesnt instantly free up the socket's
			    	memory when it is closed so even though they have been closed the memory isn't ready for reuse quite yet
			    	
			   		This can be modified by changing the wait time to accommodate different operating systems.
			   		
			   		if they program is crashing with the following message:
			   		IOException: No buffer space available (maximum connections reached?)
			   		then it is running too fast and needs to be slowed down to match the operating system. 
			   		this can be done by increasing the wait time. 
			    	*/
			    }
		    }
		    
		}
			//Error Handlers
		catch(UnknownHostException unhe){System.out.println("Client - UnknownHostException: " + unhe.getMessage());}
		catch(InterruptedIOException intioe){System.out.println("Client - Timeout while attempting to establish socket connection.");}
		catch(IOException ioe){System.out.println("Client - IOException: " + ioe.getMessage());}
		finally
		{
	      try
	      {
	        socket.close();
	      }
	      catch(IOException ioe){System.out.println("Client - IOException: " + ioe.getMessage());}	
		}
		if(debug){System.out.println("Closing Program");}
			//ensure all threads close properly.
		System.exit(0);
	}
}

		
