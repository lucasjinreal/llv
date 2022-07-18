"""
Parse collda file to json


pycollada
"""
import collada
import sys
import traceback
import numpy as np
from .daeloader import ColladaModel


def load_mixamodae_as_json(dae_f):
    col_model = ColladaModel(dae_f)

    kfs = col_model.keyframes
    one_frame_trans = None
    one_frame_anims = None
    for kf in kfs:
        print(kf.time)
        one_frame_anims = kf.joint_transform.keys()
        # print([i for i in kf.joint_transform.values()])
        one_frame_trans = kf.joint_transform.values()
    
    print(len(kfs))
    print(len(one_frame_trans))
    skl_names = []
    for i in one_frame_trans:
        print(i[0].shape)

    for i in one_frame_anims:
        skl_names.append(i.split('-')[0])
    print(skl_names)

    # return frame trans, 
    return kfs

    

if __name__ == "__main__":
    load_mixamodae_as_json(sys.argv[1])
