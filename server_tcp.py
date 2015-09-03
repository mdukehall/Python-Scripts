import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#begin listening
#doc: https://docs.python.org/2/library/socket.html
server.bind((bind_ip,bind_port))

#set max backlog to 5
server.listen(5)

print "[*] listening on %s:%d" % (bind_ip, bind_port)

#thread: manage client
#perform a receive and respond.
def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "[*] received: %s" % request
    client_socket.send("message received captain")
    client_socket.close()

#begin infinite loop; "break" is how to break this in Python
while True:
    #accept a socket
    #doc: https://docs.python.org/2/library/socket.html
    #   return value is a pair (conn, address)
    #   conn is a new socket object usable to send and receive data on the connection
    client,addr = server.accept()
    print "[*] accepted connection from: %s:%d" % (addr[0],addr[1])

    #create a thread.
    #doc: https://docs.python.org/2/library/threading.html
    client_handler = threading.Thread(target=handle_client,args=(client,))
    #start the thread; can only be done once/thread.  Otherwise raises RuntimeError
    client_handler.start()

#TO TEST
#run script; then browse to 0.0.0.0:9999.  result should be "message received captain"
