import socket

target_host="michaeldukehall.com"    #string DNS or IP
target_port=80                  #integer

#create TCP socket
#doc: https://docs.python.org/2/library/socket.html
#AF_INET is for Address Family; ipv4; AF_INET6 would be ipv6, etc
#SOCK_STREAM is default value, SOCK_DGRAM is for a data gram
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect socket
#doc: https://docs.python.org/2/library/socket.html?highlight=connect#socket.socket.connect
#send data to socket
#doc: https://docs.python.org/2/howto/sockets.html#socket-howto
client.connect((target_host,target_port))
client.send("GET / HTTP/1.0\r\n\r\n")

#receive data from socket
#parameter is buffer size; should be multiple of 2 and small.
response=client.recv(4096)
print response
