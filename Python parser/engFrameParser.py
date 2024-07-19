# import binascii
import constants

def parse_frame(frame):
    parsed_data = {}
    
    # Type of data
    parsed_data['Type of Data'] = {}
    parsed_data['Type of Data']['Start of Frame'] = frame[0]
    parsed_data['Type of Data']['Frame Direction'] = constants.FrameDirectionEnum[frame[1]].value
    parsed_data['Type of Data']['Frame Type'] = constants.FrameTypeEnum[frame[2]].value
    parsed_data['Type of Data']['IVRF'] = frame[3:6]
    
    
    #System info
    parsed_data['System info'] = {}
    parsed_data['System info']['System 3min OFF'] = "ON" if int(frame[6]) else "Off"
    parsed_data['System info']['IDUqty'] = int(frame[7:9], 16)
    parsed_data['System info']['ΣODU'] = int(frame[9:12], 16)
   
    
    # crc_hex = frame[12:16]
    # parsed_data['CRC'] = crc_hex
    
    # parsed_data['End of Frame'] = frame[16]
    
    return parsed_data

# Example usage:
frame = '*MDXXI03A02340'
parsed_data = parse_frame(frame)
for key, value in parsed_data.items():
    print(f"{key}: {value}")
