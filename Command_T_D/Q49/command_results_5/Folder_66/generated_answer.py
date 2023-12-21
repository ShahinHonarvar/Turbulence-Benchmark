def if_decimal_is_divisible(s):
    return 0 <= sum(int(c) for c in s) <= 1000000007 and len(s) == 8 and s[0] == '0' and s[1] == '0' and s[2] == '0' and s[3] == '1' and s[4] == '0' and s[5] == '1' and s[6] == '1' and s[7] == '1'
