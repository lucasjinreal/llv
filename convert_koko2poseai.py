'''
convert Koko recorded data to PoseAI format
'''
from llv.retarget_mapper import smpl_to_poseai_map, smpl_bone_index_map
import json
import os
import time

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

def construct_poseai_data(frames_content):
    """
    assume frames content is a clear data contains
    every bones position and rotation in quaterion format
    """
    koko_data = []
    for fc in frames_content:
        one_koko_frame = {}
        one_koko_frame["PF"] = 0
        one_koko_frame["Rig"] = 'MetaHuman'

        sc = fc['scene']
        ac = sc['actors'][0]
        bd = ac['body']

        new_bd = dict()
        for k,v in bd.items():
            smpl_n = smpl_bone_index_map[int(k)]
            koko_n = smpl_to_poseai_map[smpl_n]
            new_bd[koko_n] = v
        one_koko_frame['Body']['Rotations'] = new_bd

        one_koko_frame["Scalars"] = {
            "VisTorso": 1,
            "VisLegL": 0,
            "VisLegR": 0,
            "VisArmL": 0,
            "VisArmR": 0,
            "BodyHeight": 3.125,
            "StableFoot": 0.0,
            "ChestYaw": -0.059,
            "StanceYaw": 0.0,
            "HandZoneL": 5,
            "HandZoneR": 3,
            "IsCrouching": 0,
            "ShrugL": 0.0,
            "ShrugR": 0.0
        }

        one_koko_frame["Events"] = {
            "Footstep": {
            "Count": 0,
            "Magnitude": 0.0
            },
            "SidestepL": {
            "Count": 0,
            "Magnitude": 0.0
            },
            "SidestepR": {
            "Count": 0,
            "Magnitude": 0.0
            },
            "JumpCount": {
            "Count": 0,
            "Magnitude": 0.0
            },
            "FeetSplit": {
            "Count": 0,
            "Magnitude": 0.0
            },
            "ArmPump": {
            "Count": 0,
            "Magnitude": 0.0
            },
            "ArmFlex": {
            "Count": 0,
            "Magnitude": 0.0
            },
            "ArmGestureL": {
            "Count": 1,
            "Current": 8
            },
            "ArmGestureR": {
            "Count": 10,
            "Current": 4
            }
        }
        one_koko_frame['Timestamp'] = time.time()
        koko_data.append(one_koko_frame)
    return koko_data


frames_content = json.load(open("5_1.json", "r"))
fps = 25

sleep_time = 1 / fps
version = 1.6

frames_content = construct_poseai_data(frames_content)

json.dump(frames_content, open('5_1-poseai.json', 'w'))