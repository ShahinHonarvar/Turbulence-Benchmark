import re
    FIB.append(FIB[-1] + FIB[-2])
def if_decimal_is_divisible(s):
    return (s.count('1') + s.count('0') == MOD) and all(FIB[i] == 0 for i in range(MOD, 1, -1) if s[i-1] == '0')
