def if_decimal_is_divisible(s):
    n = 0
    for i in range(len(s)):
        n += int(s[i]) << (len(s) - i - 1)
    return n % 144 == 0
