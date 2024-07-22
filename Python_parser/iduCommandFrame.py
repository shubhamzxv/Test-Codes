import constants

def binary_to_hexadecimal(binary_str):
    decimal_countber = int(binary_str, 2)
    
    hex_countber = hex(decimal_countber)
    
    hex_countber = hex_countber[2:]
    
    return hex_countber.upper()

def frame_idu_command(command: dict) -> str:
    # prefix frame
    frame = "*PB4A9IP"

    # Idus selection
    idus_str = ""
    count = 1
    for i in range (0, 16):
        bi_str = ""
        for j in range (0, 4):
            if count in command["idus"] :
                bi_str += "1"
            else:
                bi_str += "0"
            
            count += 1
        
        idus_str += binary_to_hexadecimal(bi_str)

    # System selector
    # for i in range (1, 61):
    #     sys_str = f"S{i:02}"
    #     if i == command[constants.EngFrameDataKey.SID.value]:
    #         sys_str += idus_str
    #     else:
    #         sys_str += "0000000000000000"
        
    #     frame += sys_str

    # IDU identifier
    frame += "I"

    # IDU_MODE
    try:
        frame += f"{command[constants.EngFrameDataKey.MODE.value]}1"
    except KeyError:
        frame += "00"

    # tset   
    try:
        tset = command["tset"]
        frame += f"{tset:02X}1"
    except KeyError:
        frame += "000"

    # Tshift
    try:
        tshift = command["tshift"]
        frame += f"{tshift}1"
    except KeyError:
        frame += "00"

    # Fan speed
    try:
        fspd = command["fspd"]
        frame += f"{fspd}1"
    except KeyError:
        frame += "00"

    # Status
    try:
        status = command[constants.EngFrameDataKey.STATUS.value]
        frame += f"{status}1"
    except KeyError:
        frame += "00"

    # EXV
    try:
        exv = command["exv"]
        exv_int = int(exv[1:])
        frame += f"{exv[0]}{exv_int:04X}1"
    except KeyError:
        frame += "a00000"

    # idu capacity
    try:
        capacity = command["capacity"]
        frame += f"{constants.DATA_TO_CAPACITY[capacity]}1"
    except KeyError:
        frame += "00"   

    # swing
    # swing = command.get("swing", -1)
    # if swing == -1:
    #     frame += "00"
    # else:
    #     frame += f"{swing}1"

    # idu on lock
    # idu_on_lock = command.get("idu_on_lock", -1)
    # if idu_on_lock == -1:
    #     frame += "00"
    # else:
    #     frame += f"{idu_on_lock}1"

    # idu off lock
    # idu_off_lock = command.get("idu_off_lock", -1)
    # if idu_off_lock == -1:
    #     frame += "00"
    # else:
    #     frame += f"{idu_off_lock}1"

    # idu mode lock
    # idu_mode_lock = command.get("idu_mode_lock", -1)
    # if idu_mode_lock == -1:
    #     frame += "00"
    # else:
    #     frame += f"{idu_mode_lock}1"

    # idu temp lock
    # idu_temp_lock = command.get("idu_temp_lock", -1)
    # if idu_temp_lock == -1:
    #     frame += "00"
    # else:
    #     frame += f"{idu_temp_lock}1"

    # Start time
    # start_time = command.get("start_time", "-1")
    # if start_time == "-1":
    #     frame += "00000"
    # else:
    #     frame += f"{start_time}1"

    # end time
    # end_time = command.get("end_time", "-1")
    # if end_time == "-1":
    #     frame += "00000"
    # else:
    #     frame += f"{end_time}1"

    # Sleep mode
    # sleep_mode = command.get("sleep_mode", "-1")
    # if sleep_mode == "-1":
    #     frame += "00"
    # else:
    #     frame += f"{sleep_mode}1"

    # Future bytes
    # frame += "X"

    # Protocol Revision
    # protocol_revision = command.get("protocol_revision", -1)
    # if protocol_revision == -1:
    #     frame += "00"
    # else:
    #     frame += f"{protocol_revision:02X}"


    # crc

    # End of data
    # frame += "#"

    return frame

# Example
command1 = {
    constants.EngFrameDataKey.SID.value : 2,
    "idus" : [1, 2, 57, 58, 59, 60, 61, 62],
    # constants.EngFrameDataKey.STATUS.value: 1,
    constants.EngFrameDataKey.MODE.value : 3,
    "tset" : 10,
    "tshift" :"0",
    "fspd" : 3,
    # "capacity" : "105.5",
    "exv" : "a250",
    # "swing" : 5,
    # "idu_on_lock" : 1,
    # "idu_off_lock" : 0,
    # "idu_mode_lock" : 0,
    # "idu_temp_lock" :1,
    # "start_time" : "0223",
    # "end_time" : "0923",
    # "sleep_mode" :1,
    # "protocol_revision" : 255
}

frame = frame_idu_command(command1)

print(frame)
print(len(frame))