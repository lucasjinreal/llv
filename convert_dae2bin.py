'''
Convert list of frames dae animation file
into binary format

which contains almost same format as ARKit

'''
import gzip
import struct
from llv.converter.mixamodae2json import load_mixamodae_as_json
from llv.poseframe import PoseFrame
import sys


if __name__ == "__main__":
    kfs = load_mixamodae_as_json(sys.argv[1])

    with gzip.open('a.bin', "wb") as file:
        file.write(
            struct.pack(">B", PoseFrame.VERSION)
        )  # version of the binary protocol
        file.write(struct.pack(">L", len(kfs)))  # how many frames are in the recording?

        i = 0
        for kf in kfs:
            frame = PoseFrame()
            frame.version = 6
            frame.device_id = 'MY-GOD-DEVICE'
            frame.subject_name = 'llv_pose_default'
            print(kf.time)

            sub_frame = i * 0.000614 + 0.121
            frame.frame_time = {
                "frame_number": 1337 + i,
                "sub_frame": sub_frame,
                "numerator": 60,
                "denominator": 1,
            }

            # ft = {
            #     'frame_number': i,
            #     'sub_frame': 0,
            #     'numerator': int(str(kf.time).split('.')[0]),
            #     # 'denominator': int(str(kf.time).split('.')[1]),
            #     'denominator': 1+i,
            # }
            # print(ft)
            # frame.frame_time = ft
            frame.sktl_count = len(kf.joint_transform.keys())
            frame.sktl_anim_trans = kf.joint_transform.values()

            frame_packet = frame.encode()
            file.write(frame_packet)

            i+=1
        file.write(frame.data)
    
    
        
