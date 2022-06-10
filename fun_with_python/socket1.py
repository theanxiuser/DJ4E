# The world's simplest browser

import socket

# Making socket ie. making phone
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting socket to server ie. making phone call
mysock.connect(("data.pr4e.org", 80))

# command to send into server
# encode() converts unicode into utf-8
cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()

# sending the command to server
mysock.send(cmd)

# reading data
while True:
    data = mysock.recv(512)

    # if no data break the loop
    if len(data) < 1:
        break

    # display data by converting into unicode
    print(data.decode(), end="")

# terminate socket ie. close phone call
mysock.close()
