from enum import Enum

class Actions(Enum):
    Unknown = 0
    ACL_Add = 1
    ACL_Remove = 2
    ACL_Get = 3
    Wifi_Status = 4
    Wifi_Enable = 5
    Wifi_Disable = 6
    Wifi_Restart = 7
    