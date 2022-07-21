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
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True))

class RotationQuat:
    def __init__(self, x=1.0, y=2.0, z=3.0, w=4.0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True))


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
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True))


class KokoSuiteData:
    def __init__(self) -> None:
        self.name = ""
        self.timestamp = 0
        self.id = 1
        self.isLive = True
        self.hasBody = True
        self.hasFace = False
        self.hasGloves = False
        self.faceId = 1
        self.body: List[Dict] = []

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True))
