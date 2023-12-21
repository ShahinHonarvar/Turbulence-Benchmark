import re
def if_decimal_is_divisible(s):
    i = re.findall(r'0{1,2}1', s)[-1]
    return s[i-1:i+2] == '10'
