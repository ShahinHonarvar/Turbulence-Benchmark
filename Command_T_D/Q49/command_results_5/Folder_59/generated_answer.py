def if_decimal_is_divisible(s):
    return not any(s[i] == '1' for i in range(1, len(s) + 1)) and sum(s[i] == '1' for i in range(1, len(s) + 1)) == 1
