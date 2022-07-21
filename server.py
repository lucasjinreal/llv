from llv.socketconn import SocketConn


# socket_conn = SocketConn("127.0.0.1", port=8080)
socket_conn = SocketConn("127.0.0.1", port=54321, as_server=True)

while True:
    a = socket_conn.receive(10)
