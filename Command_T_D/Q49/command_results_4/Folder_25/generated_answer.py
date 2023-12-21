def if_decimal_is_divisible(s):
    return str(10**18+9) in "".join(str(i) for i in range(10**18+1))
