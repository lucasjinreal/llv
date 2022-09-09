"""

Hack on PoseAI's python schema

"""

import socket
import json
from pprint import pprint

from llv.kokoframedata import KokoProps, KokoSuiteData, Pos, RotationQuat
from llv.socketconn import SocketConn
import time
from alfred import logger
from lz4.frame import compress, decompress
from llv.retarget_mapper import retarget_poseai_koko


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


def construct_koko_data(frames_content):
    """
    assume frames content is a clear data contains
    every bones position and rotation in quaterion format
    """
    koko_data = []
    for fc in frames_content:
        one_koko_frame = {}
        one_koko_frame["version"] = 1

        # add props
        props = []
        prop1 = KokoProps()
        prop1.name = "camera"
        prop1.id = 1
        prop1.position = Pos(2.0, 3.0, 4.0)
        prop1.rotation = RotationQuat(1.2, 3., 2., 4)
        props.append(prop1.toJSON())

        prop1 = KokoProps()
        prop1.name = "light"
        prop1.id = 2
        prop1.position = Pos(2.0, 3.0, 4.0)
        prop1.rotation = RotationQuat(1.2, 3., 2., 4)
        props.append(prop1.toJSON())

        # add actors
        actors = []
        actor = KokoSuiteData()
        actor.name = "fuck suite actor"
        actor.faceId = 1
        actor.hasBody = True
        actor.timestamp = fc["Timestamp"]

        body = fc["Body"]
        body_dict = dict()
        if "Rotations" in body.keys():
            actor.hasBody = True
            for bn, bone_r in fc["Body"]["Rotations"].items():
                if bn in retarget_poseai_koko.keys():
                    bn = retarget_poseai_koko[bn]
                    body_dict[bn] = {}
                    body_dict[bn]['position'] = Pos(1.0, 2.0, 3,).toJSON()
                    body_dict[bn]['rotation'] = RotationQuat(*bone_r).toJSON()
        else:
            actor.hasBody = False
        actor.body = body_dict
        actors.append(actor.toJSON())

        one_koko_frame["scene"] = {}
        one_koko_frame["scene"]["props"] = props
        one_koko_frame["scene"]["actors"] = actors
        koko_data.append(one_koko_frame)

    return koko_data


show_my_ip()

connections = {}

socket_conn = SocketConn("127.0.0.1", port=8080)
# socket_conn = SocketConn("127.0.0.1", port=54321)
socket_conn.send_json_encoded(json.dumps(handshake, ensure_ascii=False).encode("utf-8"))

# frames_content = json.load(open("data_clip1.json", "r"))
frames_content = json.load(open("data.json", "r"))
fps = 25

sleep_time = 1 / fps
version = 1.6

frames_content = construct_koko_data(frames_content)

for fc in frames_content:
    # print(fc)
    # socket_conn.send_json(fc)
    print(type(fc))

    fc_right_json = json.dumps(fc, ensure_ascii=False)

    cpress_bytes = compress(fc_right_json.encode("utf-8"))
    socket_conn.send_json_encoded(cpress_bytes)
    logger.info(f"Start sending frames of version {version} @{fps}fps ...")

    recover = decompress(cpress_bytes)
    print(recover)
    time.sleep(sleep_time)
