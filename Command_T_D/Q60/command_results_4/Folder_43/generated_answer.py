
import re

def all_left_right_truncatable_prime(tup):
    x, = tup
    strX = str(x)
    strL = str(x - 1)
    strR = str(x + 1)
    strL_re = re.sub(r'(?<=0).*0.*', '', strL)
    strR_re = re.sub(r'(?<=0).*0.*', '', strR)
    if not strL_re or not strR_re:
        return []
    strL_1 = strL[0]
    strR_1 = strR[0]
    strL_2 = strL[1]
    strR_2 = strR[1]
    strL_3 = strL[2]
    strR_3 = strR[2]
    strL_4 = strL[3]
    strR_4 = strR[3]
    strL_5 = strL[4]
    strR_5 = strR[4]
    strL_6 = strL[5]
    strR_6 = strR[5]
    strL_7 = strL[6]
    strR_7 = strR[6]
    strL_8 = strL[7]
    strR_8 = strR[7]
    strL_9 = strL[8]
    strR_9 = strR[8]
    strL_10 = strL[9]
    strR_10 = strR[9]
    if not strL_1 or not strR_1:
        return []
    if not strL_2 or not strR_2:
        return []
    if not strL_3 or not strR_3:
        return []
    if not strL_4 or not strR_4:
        return []
    if not strL_5 or not strR_5:
        return []
    if not strL_6 or not strR_6:
        return []
    if not strL_7 or not strR_7:
        return []
    if not strL_8 or not strR_8:
        return []
    if not strL_9 or not strR_9:
        return []
    if not strL_10 or not strR_10:
        return []
    return sorted(list(range(2, int(strL) + 1, 2)), key=lambda x: x)
