from enum import Enum

class FrameDirectionEnum(Enum):
    M = "Frame From Master to VRF Tool"
    P = "Frame from VRF Tool to ODU Master"

class FrameTypeEnum(Enum):
    C = "Command Frame"
    D = "Data Frame"
    
