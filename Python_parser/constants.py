# Enums for EngFrameDataKey
from enum import Enum

class EngFrameDataKey(Enum):
    IDU_QTY = "idu_qty"
    TSC_NEW = "tsc_new"
    ODU_MODE = "odu_mode"
    MASTER_CAP = "master_cap"
    SLAVE1_CAP = "slave1_cap"
    SLAVE2_CAP = "slave2_cap"
    SLAVE3_CAP = "slave3_cap"
    MASTER_ERR = "master_err"
    SLAVE1_ERR = "slave1_err"
    SLAVE2_ERR = "slave2_err"
    SLAVE3_ERR = "slave3_err"
    SID = "sid"
    MODE = "mode"
    STATUS = "status"
    ERR = "err"
    C_TEMP = "c_temp"
    CAPACITY = "capacity"
    MODEL_NAME = "model_name"
    THERMOSTAT = "thermostat"
    FSPD = "fspd"
    STEMP = "stemp"
    SWING = "swing"
    EXV_STEP = "exv_step"
    DELTA_TCOIL = "delta_tcoil"
    ON_LOCK = "on_lock"
    OFF_LOCK = "off_lock"
    MODE_LOCK = "mode_lock"
    TEMP_LOCK = "temp_lock"
    SLEEP = "sleep"

# definig the maping 
CAP_TO_DATA = {
    "0" : "0",
    "1" : "7",
    "2" : "8",
    "3" : "10",
    "4" : "12",
    "5" : "14",
    "6" : "16",
    "7" : "18",
    "8" : "20",
    "9" : "22",
    "C" : "24",
    "D" : "26",
    "E" : "28",
    "F" : "4",
    "G" : "5",
    "H" : "6"
}

CAPACITY_TO_DATA = {
    "1" : "2.8",
    "2" : "3.5",
    "3" : "4.6",
    "4" : "5.3",
    "5" : "7.0",
    "6" : "7.7",
    "7" : "8.8",
    "8" : "10.5",
    "9" : "12.3",
    "@" : "14.1",
    "A" : "17.6",
    "B" : "19.3",
    "C" : "21.1",
    "D" : "23.9",
    "E" : "28.1",
    "F" : "35.2",
    "G" : "2.3",
    "H" : "6.0",
    "I" : "8.1",
    "J" : "10.0",
    "K" : "11.3",
    "L" : "44.0",
    "M" : "52.7",
    "N" : "70.3",
    "O" : "87.9",
    "P" : "105.5"
}

DATA_TO_CAPACITY = {
    "2.8" : "1",
    "3.5" : "2",
    "4.6" : "3",
    "5.3" : "4",
    "7.0" : "5",
    "7.7" : "6",
    "8.8" : "7",
    "10.5" : "8",
    "12.3" : "9",
    "14.1" : "@",
    "17.6" : "A",
    "19.3" : "B",
    "21.1" : "C",
    "23.9" : "D",
    "28.1" : "E",
    "35.2" : "F",
    "2.3" : "G",
    "6.0" : "H",
    "8.1" : "I",
    "10.0" : "J",
    "11.3" : "K",
    "44.0" : "L",
    "52.7" : "M",
    "70.3" : "N",
    "87.9" : "O",
    "105.5" : "P"
}