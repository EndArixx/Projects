import java.io.*;
import java.net.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;


public class JStanleyPort
{
	public static boolean debug = false;
	
	class request_handler implements Runnable
	{
		private String name;
		private Thread thread;
		private PrintWriter pw;
		private BufferedReader br;
		Socket socket;
		request_handler(String name, Socket socket )
		{
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
				InputStreamReader inputstreamreader = new InputStreamReader(socket.getInputStream());
			    BufferedReader bufferedreader = new BufferedReader(inputstreamreader);
			      
			    PrintWriter printwriter = new PrintWriter(socket.getOutputStream(),true);
			 
			      
			      
			    String line = "";
			      
			    while ((line = bufferedreader.readLine()) != null)
			    {
			    	printwriter.println("ACK:" + line);
			    }
			      
			      	//Close everything
			    if(debug){System.out.println("      Request_handler: "+name+" - Closing connection.");}
			    bufferedreader.close();
			    inputstreamreader.close();
			    printwriter.close();
			    socket.close();
			}
			catch(UnknownHostException unhe){
		      System.out.println("UnknownHostException: " + unhe.getMessage());
		    }catch(InterruptedIOException intioe){
		      System.out.println("Timeout while attempting to establish socket connection.");
		    }catch(IOException ioe){
		      System.out.println("IOException: " + ioe.getMessage());
		    }finally{
		      try{
		        socket.close();
		      }catch(IOException ioe){
		    	  if(debug){System.out.println("IOException: " + ioe.getMessage());}
		      }
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
			    	long startTime = System.currentTimeMillis();
			    	long currentTime;
			    	while(true)
			    	{
			    		currentTime   = System.currentTimeMillis();
			    		if(currentTime - startTime >= 1000)
			    		{
			    			if(debug){System.out.println("[" + (currentTime - startTime) +"]");}
			    			break;
			    		}
					      	//wait for client
					    if((socket = serversocket.accept()) != null)
					    {
				    		socket.setSoTimeout(10000);
					    	new request_handler("r" + n, socket).start();
					    	n++;
					    }
			    	}
			    }catch(UnknownHostException unhe){
			      System.out.println("UnknownHostException: " + unhe.getMessage());
			    }catch(InterruptedIOException intioe){
			      System.out.println("Timeout while attempting to establish socket connection.");
			    }catch(IOException ioe){
			      System.out.println("IOException: " + ioe.getMessage());
			    }finally{
			      try{
			    	  if(debug){System.out.println("    Closing listen_thread: " +  name );}
			        socket.close();
			        serversocket.close();
			      }catch(IOException ioe){
			        System.out.println("IOException: " + ioe.getMessage());
			      }
			    }
		}
		public void start ()
		{
			if(debug){System.out.println("    Starting listen_thread: " +  name );}
	      if (thread == null)
	      {
	         thread = new Thread (this, name);
	         thread.start ();
	      }
		}

	}
	
		
	public static void main(String[] args) 
	{
		if(debug){System.out.println("  Starting Program");}
		JStanleyPort j1 = new JStanleyPort();
		
		listen_thread l1 = j1.new listen_thread("Thread one");
		l1.start();
		
		Socket socket = null;
		int serverport = 9090;
		try 
		{
		    for(int i = 0; i < 10; i++)
		    {
				//- create client and establish a tcp connection to server listening on port 9090 locally
		
				//try to open a socket on port 9090
				//InetAddress.getByName(null) is local
		    	if(debug){System.out.println("  Connecting to " + InetAddress.getByName(null) + " on port " + serverport);}
			    socket = new Socket(InetAddress.getByName(null),serverport);
			    
			    	//wait 10 seconds for the connection.
			    socket.setSoTimeout(10000);
			    if(debug){System.out.println("  Client Connected.");}
			    
			    	//Input Reader
			    InputStreamReader inputStreamReader = new InputStreamReader(socket.getInputStream());
			    BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
			    	//Output Writer 
			    PrintWriter printWriter = new PrintWriter(socket.getOutputStream(),true);
			    
			    
	
			    	
			    String line = "";
			    int number;
			    
			    	//Start listening to the port
			    
					//- Send a timestamp string of form "yyyy-MM-dd HH:mm:ss" followed by newline character
					//- Print to console what was sent and response from server, on separate lines.
			    DateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
			    Date date = new Date();
			    String timestamp = format.format(date);
			    
			    printWriter.println(timestamp);
			    System.out.println(timestamp);
			    line = bufferedReader.readLine();
			    System.out.println(line);
			    
	
					//- send a message to server of form "Request-XX" where XX should be a random number between 00 and 99
					//- print what was sent and response from server, on separate lines.
	
			    Random rn = new Random();
			    number = rn.nextInt(100);
				printWriter.println("Request-" + number);
				System.out.println("Request-" + number); 
				line = bufferedReader.readLine();
			    System.out.println(line);
			    
			    
			    //- close connection to server
			    if(debug){System.out.println("  Client Closing connection.");}
			    bufferedReader.close();
			    inputStreamReader.close();
			    printWriter.close();
			    socket.close();
		    }
		}
		catch(UnknownHostException unhe){
	      System.out.println("UnknownHostException: " + unhe.getMessage());
	    }catch(InterruptedIOException intioe){
	      System.out.println("Timeout while attempting to establish socket connection.");
	    }catch(IOException ioe){
	      System.out.println("IOException: " + ioe.getMessage());
		}finally{
	      try{
	        socket.close();
	      }catch(IOException ioe){
	        System.out.println("IOException: " + ioe.getMessage());
	      }
			
			
			
		}
		if(debug){System.out.println("Closing Program");}
		System.exit(0);
	}
}

		
