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
    for kf in kfs:
        print(kf.time)
        print(kf.joint_transform.keys())
        # print([i for i in kf.joint_transform.values()])
        one_frame_trans = kf.joint_transform.values()
    
    print(len(kfs))
    print(len(one_frame_trans))
    for i in one_frame_trans:
        print(i[0].shape)

    

if __name__ == "__main__":
    load_mixamodae_as_json(sys.argv[1])
