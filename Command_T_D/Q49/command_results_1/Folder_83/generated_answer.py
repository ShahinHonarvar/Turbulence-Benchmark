def if_decimal_is_divisible(s):
    n = 0
    for i in range(len(s)):
        n = n * 2 + (s[i] == '1')
    return n % (60 * (10**18 + 7)) == 0
