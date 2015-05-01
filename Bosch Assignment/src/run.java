
public class run 
{
	void main() 
	{
		/*- create new thread for server (listen_thread)
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
		 }*/
		
		
		
	}
		
}
