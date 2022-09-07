"""
Imitation Rokoko livelink's frame data format


"""

import json
from datetime import datetime
from typing import Dict, List


"""
Defines the schema on how should we communicate with UE

"""


class Pos:
    def __init__(self, x=1.0, y=2.0, z=3.0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def toJSON(self):
        return json.loads(
            json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        )


class RotationQuat:
    def __init__(self, x=1.0, y=2.0, z=3.0, w=4.0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def toJSON(self):
        return json.loads(
            json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        )


class KokoProps:
    def __init__(self) -> None:
        self.name = ""
        self.id = 1
        self.color = [4, 5, 6]
        self.position: Pos = None
        self.rotation: RotationQuat = None
        self.isLive = True
        self.profile = None

    def toJSON(self):
        return json.loads(
            json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        )


class KokoPersonData:
    def __init__(self) -> None:
        self.name = ""
        self.timestamp = 0
        self.id = 1
        self.isLive = True
        self.hasBody = True
        self.hasFace = False
        self.hasGloves = False
        self.faceId = 1
        self.skeleton_type = 'smpl'
        self.root_trans: Pos = None
        self.body: List[Dict] = []

    def toJSON(self):
        return json.loads(
            json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        )


class KokoScene:

    def __init__(self) -> None:
        self.scene: Dict = None

    def toJSON(self):
        return json.loads(
            json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        )
    

def make_default_props():
    """
    props default contains 1 camera and 1 light, this normally not used
    return list of json str
    """
    props = []

    prop0 = KokoProps()
    prop0.name = "light0"
    prop0.id = 1
    prop0.position = Pos(1.2, 4, 4)
    prop0.rotation = RotationQuat(1.0, 1.2, 1.2, 1.0)

    prop1 = KokoProps()
    prop1.name = "camera0"
    prop1.id = 2
    prop1.position = Pos(1.2, 4, 4)
    prop1.rotation = RotationQuat(1.0, 1.2, 1.2, 1.0)
    return [prop0.toJSON(), prop1.toJSON()]
