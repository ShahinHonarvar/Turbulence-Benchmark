def if_decimal_is_divisible(s):
    return (10**9 + 7) // 10**4 == sum(b == '1' for b in s[::-1]) % 2
