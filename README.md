# real-time_chat
this is a real-time communication system, every connected system will see your messages and vice versa. encyption is not their currently(working in it).
## how to set up
- fork the repo
- currently the server ip is set to 0.0.0.0 which listen to all the connections.
- you have to install ngrok for connecting your local network to internet, ngrok work as a tunnel. after installing you have to sign up for authorisation token.
- start ngrok with the required protocol in our case it is tcp and port (we are using 5050).
- after starting ngrok it will give u an ip alongwith the port.
- send the client side code to all those with whom you want to communicate with the ip and port name provided by the ngrok. 
- start the server for all connections and client program for you to send messages 
