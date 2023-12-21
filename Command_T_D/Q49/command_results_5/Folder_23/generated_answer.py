def if_decimal_is_divisible(s):
    n = 0
    f = 1
    res = 0
    flag = 0
    for i in range(len(s)):
        n += int(s[i] - '0') * f
        f *= 2
        if n % 48 == 0:
            res = 1
            flag = 1
            break
    return res == 1 and flag == 1
