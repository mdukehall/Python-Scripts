import socket

target_host="127.0.0.1"         #string DNS or IP
target_port=80                  #integer

#create UDP socket
#doc: https://docs.python.org/2/library/socket.html
#AF_INET is for Address Family; ipv4; AF_INET6 would be ipv6, etc
#SOCK_STREAM is default value, SOCK_DGRAM is for a data gram
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send data to socket
#UDP is a connectionless protocol
#doc: https://docs.python.org/2/howto/sockets.html#socket-howto
client.sendto("SOMEDATA", (target_host,target_port))

#receive data from socket
#parameter is buffer size; should be multiple of 2 and small.
#doc: https://docs.python.org/2/library/socket.html
data,addr=client.recv(4096)
print data
