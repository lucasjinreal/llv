import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 54321
BUFFER_SIZE = 1024
MESSAGE = '{"mything":[{"Type": "CharacterAnimation"},{"Location":[1,2,200],"Rotation":[0,0,0,1],"Scale":[1,1,1]}]}'

msg = {
    "PF": 0,
    "Rig": "UE4",
    "Body": {
        "Rotations": {
            "pelvis": [-0.24, -0.862, 0.08, 0.439],
            "spine_01": [-0.24, -0.862, 0.08, 0.439],
            "spine_02": [-0.05, -0.831, 0.039, 0.553],
            "spine_03": [0.038, -0.754, 0.016, 0.656],
            "neck_01": [-0.038, -0.798, 0.049, 0.599],
            "head": [0.116, -0.7, 0.159, 0.687],
            "clavicle_l": [-0.066, -0.395, 0.152, 0.904],
            "upperarm_l": [0.174, 0.263, -0.948, -0.053],
            "lowerarm_l": [0.456, 0.211, -0.864, 0.017],
            "clavicle_r": [0.944, 0.231, -0.137, 0.189],
            "upperarm_r": [0.678, -0.727, 0.106, -0.0],
            "lowerarm_r": [0.579, -0.791, -0.06, -0.188],
        },
        "Scalars": {
            "VisTorso": 1,
            "VisLegL": 0,
            "VisLegR": 0,
            "VisArmL": 0,
            "VisArmR": 1,
            "BodyHeight": 1.443,
            "StableFoot": 0.0,
            "ChestYaw": 0.01,
            "StanceYaw": 0.0,
            "HandZoneL": 6,
            "HandZoneR": 3,
            "IsCrouching": 0,
            "ShrugL": 0.0,
            "ShrugR": 0.0,
        },
        "Events": {
            "Footstep": {"Count": 0, "Magnitude": 0.0},
            "SidestepL": {"Count": 0, "Magnitude": 0.0},
            "SidestepR": {"Count": 0, "Magnitude": 0.0},
            "JumpCount": {"Count": 0, "Magnitude": 0.0},
            "FeetSplit": {"Count": 0, "Magnitude": 0.0},
            "ArmPump": {"Count": 137, "Magnitude": 0.0},
            "ArmFlex": {"Count": 0, "Magnitude": 0.0},
            "ArmGestureL": {"Count": 10, "Current": 53},
            "ArmGestureR": {"Count": 31, "Current": 7},
        },
        "Vectors": {
            "HipLean": [-0.115, 0.152],
            "HipScreen": [0.0, 0.0],
            "ChestScreen": [-0.007, -0.192],
        },
        "Loco": "AAAA",
        "Locomotion": "",
    },
    "LeftHand": {
        "Rotations": {
            "hand_l": [0.015, -0.093, -0.168, -0.981],
            "lowerarm_twist_01_l": [-0.559, 0.216, 0.562, 0.57],
            "index_01_l": [0.122, -0.138, -0.057, -0.981],
            "index_02_l": [0.03, -0.143, -0.041, -0.988],
            "index_03_l": [0.03, -0.143, -0.038, -0.988],
            "middle_01_l": [0.047, -0.198, -0.001, -0.979],
            "middle_02_l": [0.032, -0.198, 0.005, -0.979],
            "middle_03_l": [0.032, -0.198, 0.007, -0.979],
            "ring_01_l": [0.062, 0.175, -0.048, 0.981],
            "ring_02_l": [-0.147, 0.106, -0.708, 0.682],
            "ring_03_l": [-0.171, 0.058, -0.878, 0.442],
            "pinky_01_l": [0.098, 0.271, 0.036, 0.957],
            "pinky_02_l": [-0.039, 0.263, 0.071, 0.961],
            "pinky_03_l": [-0.039, 0.263, 0.068, 0.961],
            "thumb_01_l": [0.26, 0.749, 0.25, 0.555],
            "thumb_02_l": [0.366, 0.11, 0.032, 0.923],
            "thumb_03_l": [-0.332, 0.142, -0.023, -0.932],
        },
        "Vectors": {"PointScreen": [-0.062, -0.104]},
    },
    "RightHand": {
        "Rotations": {
            "hand_r": [0.173, -0.795, 0.572, 0.106],
            "lowerarm_twist_01_r": [-0.267, 0.911, 0.151, 0.276],
            "index_01_r": [0.578, -0.681, 0.287, 0.346],
            "index_02_r": [0.749, -0.482, 0.269, 0.367],
            "index_03_r": [0.81, -0.37, 0.213, 0.401],
            "middle_01_r": [0.564, -0.649, 0.394, 0.326],
            "middle_02_r": [0.762, -0.394, 0.262, 0.442],
            "middle_03_r": [0.809, -0.285, 0.199, 0.474],
            "ring_01_r": [-0.612, 0.601, -0.446, -0.257],
            "ring_02_r": [-0.751, 0.434, -0.274, -0.415],
            "ring_03_r": [-0.807, 0.316, -0.209, -0.452],
            "pinky_01_r": [0.606, -0.571, 0.496, 0.247],
            "pinky_02_r": [0.643, -0.556, 0.364, 0.381],
            "pinky_03_r": [0.683, -0.506, 0.334, 0.407],
            "thumb_01_r": [-0.001, -0.869, -0.25, 0.426],
            "thumb_02_r": [0.116, -0.759, -0.296, 0.568],
            "thumb_03_r": [-0.253, 0.64, 0.407, -0.601],
        },
        "Vectors": {"PointScreen": [-0.114, -0.095]},
    },
    "ModelLatency": 21,
    "Timestamp": 98062.66,
}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
s.close()
