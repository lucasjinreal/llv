import json

"""

e spine;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName ;
	extern const FName rightLeg;
	extern const FName rightFoot;
	extern const FName rightToe;
	extern const FName rightToeEnd;
	extern const FName leftThumbProximal;
	extern const FName leftThumbMedial;
	extern const FName leftThumbDistal;
	extern const FName leftThumbTip;
	extern const FName leftIndexProximal;
	extern const FName leftIndexMedial;
	extern const FName leftIndexDistal;
	extern const FName leftIndexTip;
	extern const FName leftMiddleProximal;
	extern const FName leftMiddleMedial;
	extern const FName leftMiddleDistal;
	extern const FName leftMiddleTip;
	extern const FName leftRingProximal;
	extern const FName leftRingMedial;
	extern const FName leftRingDistal;
	extern const FName leftRingTip;
	extern const FName leftLittleProximal;
	extern const FName leftLittleMedial;
	extern const FName leftLittleDistal;
	extern const FName leftLittleTip;
	extern const FName rightThumbProximal;
	extern const FName rightThumbMedial;
	extern const FName rightThumbDistal;
	extern const FName rightThumbTip;
	extern const FName rightIndexProximal;
	extern const FName rightIndexMedial;
	extern const FName rightIndexDistal;
	extern const FName rightIndexTip;
	extern const FName rightMiddleProximal;
	extern const FName rightMiddleMedial;
	extern const FName rightMiddleDistal;
	extern const FName rightMiddleTip;
	extern const FName rightRingProximal;
	extern const FName rightRingMedial;
	extern const FName rightRingDistal;
	extern const FName rightRingTip;
	extern const FName rightLittleProximal;
	extern const FName rightLittleMedial;
	extern const FName rightLittleDistal;
	extern const FName rightLittleTip;
"""

retarget_poseai_koko = {
    "pelvis": "hip",
    "spine_01": "chest",
    "neck_01": "neck",
    "head": "head",
    "clavicle_l": "leftShoulder",
    "upperarm_l": "leftUpperArm",
    "lowerarm_l": "leftLowerArm",
    "hand_l": "leftHand",
    "clavicle_r": "rightShoulder",
    "upperarm_r": "rightUpperArm",
    "lowerarm_r": "rightLowerArm",
    "hand_r": "rightHand",
    # "": "leftUpLeg",
    # "": "leftLeg",
    # "": "leftFoot",
    # "": "leftToe",
    # "": "leftToeEnd",
    # "": "rightUpLeg",
}

smpl_to_koko_map = {
    "Pelvis": "hip",
    "L_Hip": "leftUpLeg",
    "R_Hip": "rightUpLeg",
    "Spine1": "spine",
    "L_Knee": "leftLeg",
    "R_Knee": "rightLeg",
    "Spine2": "chest",
    "L_Ankle": "leftFoot",
    "R_Ankle": "rightFoot",
    "Spine3": "",
    "L_Foot": "leftToe",
    "R_Foot": "rightToe",
    "Neck": "neck",
    "L_Collar": "leftShoulder",
    "R_Collar": "rightShoulder",
    "Head": "head",
    "L_Shoulder": "leftUpperArm",
    "R_Shoulder": "rightUpperArm",
    "L_Elbow": "leftLowerArm",
    "R_Elbow": "rightLowerArm",
    "L_Wrist": "leftHand",
    "R_Wrist": "rightHand",
    "L_Hand": "leftIndexTip",
    "R_Hand": "rightIndexTip",
    "L_Hand": "leftMiddleTip",
    "R_Hand": "rightMiddleTip",
}


smpl_bone_index_map = {
    0: "Pelvis",
    1: "L_Hip",
    2: "R_Hip",
    3: "Spine1",
    4: "L_Knee",
    5: "R_Knee",
    6: "Spine2",
    7: "L_Ankle",
    8: "R_Ankle",
    9: "Spine3",
    10: "L_Foot",
    11: "R_Foot",
    12: "Neck",
    13: "L_Collar",
    14: "R_Collar",
    15: "Head",
    16: "L_Shoulder",
    17: "R_Shoulder",
    18: "L_Elbow",
    19: "R_Elbow",
    20: "L_Wrist",
    21: "R_Wrist",
    22: "L_Hand",
    23: "R_Hand",
}

mixamo_smpl_mapper = {
    "Hips": "Pelvis",
    "LeftUpLeg": "L_Hip",
    "RightUpLeg": "R_Hip",
    "Spine2": "Spine3",
    "Spine1": "Spine2",
    "Spine": "Spine1",
    "LeftLeg": "L_Knee",
    "RightLeg": "R_Knee",
    "LeftFoot": "L_Ankle",
    "RightFoot": "R_Ankle",
    "LeftToeBase": "L_Foot",
    "RightToeBase": "R_Foot",
    "Neck": "Neck",
    "LeftShoulder": "L_Collar",
    "RightShoulder": "R_Collar",
    "Head": "Head",
    "LeftArm": "L_Shoulder",
    "RightArm": "R_Shoulder",
    "LeftForeArm": "L_Elbow",
    "RightForeArm": "R_Elbow",
    "LeftHand": "L_Wrist",
    "RightHand": "R_Wrist",
    "LeftHandIndex1": "L_Hand",
    "LeftHandMiddle1": "L_Hand",
    "RightHandMiddle1": "R_Hand",
    "RightHandIndex1": "R_Hand",
}
