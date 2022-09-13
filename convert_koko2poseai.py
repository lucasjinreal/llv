'''
convert Koko recorded data to PoseAI format
'''
from llv.retarget_mapper import smpl_to_poseai_map
import json
import os


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


frames_content = json.load(open("5_1.json", "r"))
fps = 25

sleep_time = 1 / fps
version = 1.6

frames_content = construct_poseai_data(frames_content)

json.dump(frames_content, open('5_1-poseai.json', 'w'))