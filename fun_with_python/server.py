# The world's simplest web server

from socket import *


# Create the actual server
# it just returns Hello World! for every request
def createserver():
    # open socket for receiving request ie. phone call from client
    serversocket = socket(AF_INET, SOCK_STREAM)

    # use try - except statement
    try:
        # server runs on localhost and port 9000
        serversocket.bind(("localhost", 9000))
        serversocket.listen(5)

        # always ready for response to every request
        while True:
            (clientsocket, address) = serversocket.accept()

            # read the data
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces)

            data = "HTTP/1.1 200 OK\r\n"
            data += "content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World!</body></html>\r\n\r\n"

            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShuttig down...\n")

    except Exception as excp:
        print("Exception:")
        print(excp)

    # finally close the socket
    serversocket.close()


# Starting code goes here
print("Access http://localhost:9000")
createserver()
