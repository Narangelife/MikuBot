#====================================================
# FileName: config.py
# Description: Configs for MikuBot
# Author: Narangelife
# Copyright: © Narange
#====================================================

# ふむ、なかなかに気持ち悪いコードである。

# system
import os
from dotenv import load_dotenv


# environment
load_dotenv()
MIKUBOT_ROLE_16 = os.getenv("MIKUBOT_ROLE_16")
MIKUBOT_ROLE_17 = os.getenv("MIKUBOT_ROLE_17")
MIKUBOT_ROLE_18 = os.getenv("MIKUBOT_ROLE_18")
MIKUBOT_ROLE_19 = os.getenv("MIKUBOT_ROLE_19")
MIKUBOT_ROLE_20 = os.getenv("MIKUBOT_ROLE_20")
MIKUBOT_ROLE_21 = os.getenv("MIKUBOT_ROLE_21")
MIKUBOT_ROLE_22 = os.getenv("MIKUBOT_ROLE_22")
MIKUBOT_ROLE_23 = os.getenv("MIKUBOT_ROLE_23")
MIKUBOT_ROLE_24 = os.getenv("MIKUBOT_ROLE_24")


role_ids = {
    16: MIKUBOT_ROLE_16,
    17: MIKUBOT_ROLE_17,
    18: MIKUBOT_ROLE_18,
    19: MIKUBOT_ROLE_19,
    20: MIKUBOT_ROLE_20,
    21: MIKUBOT_ROLE_21,
    22: MIKUBOT_ROLE_22,
    23: MIKUBOT_ROLE_23,
    24: MIKUBOT_ROLE_24,
}


#----------------------------------------------------
# Get role id for year role setting (Invalid result: -1)
def getRoleId(id: int) -> int:
    if id not in role_ids:
        return -1
    
    return int(role_ids[id])