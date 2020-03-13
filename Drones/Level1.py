import socket
import math

PI = 3.1415926535
g = 9.80665


def getThrust(throttle):
    if throttle > 1.0 or throttle < 0.0:
        return False
    f = 3.2
    r_max = 10000
    c = 0.015
    c = c + math.pow((throttle * (r_max / 1000)), f)
    ro = 1.225
    d = 0.25
    t = math.pow(PI / 2 + math.pow(d, 2) * ro * math.pow(d, 2), 1 / 3)
    return t


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('0.0.0.0', 100)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

lines = 0
while lines < 3:
    data = sock.recv(256)
    lines_data = data.splitlines()
    for n in range(len(lines_data)):
        if lines == 0:
            splited_data = lines_data[n].split()
            x_min = float(splited_data[0])
            x_max = float(splited_data[1])
            y_min = float(splited_data[2])
            y_max = float(splited_data[3])
            limits = [[x_min, y_min], [x_max, y_max]]
            del x_min
            del x_max
            del y_min
            del y_max
            lines += 1
        elif lines == 1:
            n_drones = int(lines_data[n])
            lines += 1
        elif lines == 2:
            height = float(lines_data[n])
            lines += 1

message = 'STATUS 0'.encode()
sock.sendall(message)

while True:
    try:
        msg = sock.recv(4096)
    except socket.error, e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            sleep(1)
            print 'No data available'
            continue
        else:
            # a "real" error occurred
            print e
            sys.exit(1)
    else:
        # got a message, do something :)

print(status)

sock.close()
