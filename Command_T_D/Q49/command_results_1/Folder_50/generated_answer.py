import re
def if_decimal_is_divisible(s):
    return all(FIB[i] == '1' for i in range(len(FIB) - 1) if FIB[i] == s[i])
