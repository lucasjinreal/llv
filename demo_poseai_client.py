"""

Hack on PoseAI's python schema

"""

import socket
import json
from pprint import pprint
from llv.socketconn import SocketConn


PORT_NUM = 8080


""" Prints your local IP address.  Configure this in the App.
  Make sure your router and firewall do not block the port """


def show_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    print("Connect the app to IP:", ip, "Port:", PORT_NUM)


handshake = {
    "version": "1.2.5",
    "userName": "iPhone2Python",
    "sessionUUID": "8EF5BA6A-A73E-419A-9BDC-7E18759C180C",
    "deviceName": "iPhone13,4",
}

show_my_ip()

connections = {}

socket_conn = SocketConn("127.0.0.1", port=8080)
socket_conn.send_json(handshake)

frames_content = json.load(open("data_clip1.json", "r"))

for fc in frames_content:
    socket_conn.send_json(fc)
