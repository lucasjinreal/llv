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
