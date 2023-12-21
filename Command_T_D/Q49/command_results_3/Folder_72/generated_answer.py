def if_decimal_is_divisible(s):
    return (10**(len(s)-1)-1-int(s,2))%59==0
