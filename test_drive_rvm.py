"""

Let's try drive UE character by rvm output

"""

import socket
import json
from pprint import pprint

from llv.kokoframedata import KokoProps, KokoPersonData, Pos, RotationQuat
from llv.socketconn import SocketConn
import time
from alfred import logger
from lz4.frame import compress, decompress
from llv.retarget_mapper import retarget_poseai_koko
from llv.retarget_mapper import smpl_bone_index_map, smpl_to_koko_map
import sys


PORT_NUM = 54321
# PORT_NUM = 14045


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
    "HANDSHAKE": {
        "version": "1.2.5",
        "userName": "iPhone2Python",
        "sessionUUID": "8EF5BA6A-A73E-419A-9BDC-7E18759C180C",
        "deviceName": "iPhone13,4",
    },
    "version": "1.2.5",
    "userName": "iPhone2Python",
}


show_my_ip()

connections = {}

# socket_conn = SocketConn("127.0.0.1", port=8080)
socket_conn = SocketConn("127.0.0.1", port=54321)
socket_conn.send_json_encoded(json.dumps(handshake, ensure_ascii=False).encode("utf-8"))

# frames_content = json.load(open("data_clip1.json", "r"))
frames_content = json.load(open(sys.argv[1], "r"))
fps = 10

sleep_time = 1 / fps
version = 1.6

pprint(frames_content[0])


# for fc in frames_content:
#     sc = fc['scene']
#     for ac in sc['actors']:
#         bd = ac['body']
#         new_bd = dict()
#         for k,v in bd.items():
#             smpl_n = smpl_bone_index_map[int(k)]
#             koko_n = smpl_to_koko_map[smpl_n]
#             new_bd[koko_n] = v
#         ac['body'] = new_bd
# json.dump(frames_content, open('5_1-new.json', 'w'))


while True:
    for fc in frames_content:
        # print(fc)
        # socket_conn.send_json(fc)
        print(type(fc))
        print(fc['scene']['actors'][0]['body']['rightFoot'])

        fc['version'] = version

        fc_right_json = json.dumps(fc, ensure_ascii=False)

        cpress_bytes = compress(fc_right_json.encode("utf-8"))
        socket_conn.send_json_encoded(cpress_bytes)
        logger.info(f"Start sending frames of version {version} @{fps}fps ...")

        recover = decompress(cpress_bytes)
        # print(recover)
        time.sleep(sleep_time)
