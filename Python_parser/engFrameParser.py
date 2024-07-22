import constants
 
def parser_eng_frame(frame: str) -> dict:
    
    try:
        parsed_data: dict = {
            constants.EngFrameDataKey.IDU_QTY.value : int(frame[7 : 9], 16),
            constants.EngFrameDataKey.TSC_NEW.value : int(frame[27 : 31], 16),
            constants.EngFrameDataKey.ODU_MODE.value : int(frame[43]),
            constants.EngFrameDataKey.MASTER_CAP.value : constants.CAP_TO_DATA.get(frame[61]),
            constants.EngFrameDataKey.SLAVE1_CAP.value : constants.CAP_TO_DATA.get(frame[93]),
            constants.EngFrameDataKey.SLAVE2_CAP.value : constants.CAP_TO_DATA.get(frame[125]),
            constants.EngFrameDataKey.SLAVE3_CAP.value : constants.CAP_TO_DATA.get(frame[157]),
            constants.EngFrameDataKey.MASTER_ERR.value : frame[401 : 403],
            constants.EngFrameDataKey.SLAVE1_ERR.value : frame[470 : 472],
            constants.EngFrameDataKey.SLAVE2_ERR.value : frame[539 : 541],
            constants.EngFrameDataKey.SLAVE3_ERR.value : frame[608 : 610],
            constants.EngFrameDataKey.SID.value : int(frame[4781 : 4783], 16)
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

    # IDU
    parsed_data["idus"] = []
    for i in range(0, parsed_data[constants.EngFrameDataKey.IDU_QTY.value]):
        num = i * 65

        try:
            idu = {
                constants.EngFrameDataKey.MODE.value :  int(frame[751 + num]),
                constants.EngFrameDataKey.STATUS.value :  int(frame[752 + num]),
                constants.EngFrameDataKey.ERR.value : frame[753 + num : 755 + num],
                constants.EngFrameDataKey.C_TEMP.value : f"{int(frame[760 + num : 764 + num], 16) / 10}",
                constants.EngFrameDataKey.CAPACITY.value : constants.CAPACITY_TO_DATA.get(frame[768 + num]),
                constants.EngFrameDataKey.MODEL_NAME.value : frame[769 + num],
                constants.EngFrameDataKey.THERMOSTAT.value : int(frame[778 + num]),
                constants.EngFrameDataKey.FSPD.value : int(frame[780 + num]),
                constants.EngFrameDataKey.STEMP.value : f"{int(frame[781 + num : 783 + num], 16)}",
                constants.EngFrameDataKey.SWING.value : {
                    "value" : int(frame[785 + num]),
                    "pos" : int(frame[784 + num])
                },
                constants.EngFrameDataKey.EXV_STEP.value : f"{frame[786 + num]}{int(frame[787 + num : 791 + num], 16)}",
                constants.EngFrameDataKey.DELTA_TCOIL.value : f"{int(frame[791 + num : 795 + num], 16) / 10}",
                constants.EngFrameDataKey.ON_LOCK.value : int(frame[800 + num]),
                constants.EngFrameDataKey.OFF_LOCK.value : int(frame[801 + num]),
                constants.EngFrameDataKey.MODE_LOCK.value : int(frame[802 + num]),
                constants.EngFrameDataKey.TEMP_LOCK.value : int(frame[803 + num]),
                constants.EngFrameDataKey.SLEEP.value : int(frame[812 + num])
            }
            parsed_data["idus"].append(idu)
        except:
            continue

    return parsed_data

# Example
frame_1 = '*MDXXI00111C001C00900000000000000000000000020010112000900000030000000000500001470147000420000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001E01E00000000000000000000000000000001E01E00000000000000000000000000000001E01E00000000000000000000000000000001E01E00000000101002003004000000+19+190FA0FA000000000000000000+0FA+0FA+0FA+0FA+0FA0000000000000000000+00+00000000000000000000000000+000+000+000+000+0000000000000000000000+00+00000000000000000000000000+000+000+000+000+0000000000000000000000+00+00000000000000000000000000+000+000+000+000+00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000+005 0A8C 0000 0000 0000 00 00110000+32+0FA+0F012+000+0F505110001a01E0+00551117000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X01E031DBA#'
frame_2 = '*MDXXI00111C001C00900000000000000000000000022010112001000000030000000000700001470147000420000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001E01E06000000000000000000000000000001E01E00000000000000000000000000000001E01E00000000000000000000000000000001E01E00000000101002003004000000+19+190FA0FA000000000000000000+0FA+0FA+0FA+0FA+0FA0000000000000000000+00+00000000000000000000000000+000+000+000+000+0000000000000000000000+00+00000000000000000000000000+000+000+000+000+0000000000000000000000+00+00000000000000000000000000+000+000+000+000+00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000+005 0A8C 0000 0000 0000 00 00210064+5F+0FF+0F012+000+0F515410101a01E0+00540117000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X01E03F3F6#'
frame_3 = '*MDXXI00111C001C009001C001A001C001C001100112201011200120000003001C000000901001470147000420000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001101E01E00000000000000000000000000000001E01E00000000000000000000000000000001E01E00000000000000000000000000000001E01E00000000101002003004000000+19+190FA0FA000000000000000000+0FA+0FA+0FA+0FA+0FA0000000000000000000+00+00000000000000000000000000+000+000+000+000+0000000000000000000000+00+00000000000000000000000000+000+000+000+000+0000000000000000000000+00+00000000000000000000000000+000+000+000+000+00000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000+001 0AAA 0033 0000 0000 00 00210044+0F+0FF+0F012+000+0F515418101a0064+00440117000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X01E030716#'
frame_4 = '*MDXXI00111C001C009001C002A001C001C001C001C2201011200130000003001C000000901001470147000420000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001101E01E00000000000000000000000000000001E01E00000000000000000000000000000001E01E00000000000000000000000000000001E01E00000000101002003004000000+19+190FA0FA000000000000000000+0FA+0FA+0FA+0FA+0FA0000000000000000000+00+00000000000000000000000000+000+000+000+000+0000000000000000000000+00+00000000000000000000000000+000+000+000+000+0000000000000000000000+00+00000000000000000000000000+000+000+000+000+00000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000+001 0B09 0033 0000 0000 00 00210064+4B+0FF+0F012+000+0F515412101a0064+00540117000000000000100X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X000000+00+000+00001+000+00005000001a0000+00000000000000000000000X01E032274#'
frame_5 = '29384urjdjfojfodfof'
parsed_data = parser_eng_frame(frame_2)     
print(parsed_data)
