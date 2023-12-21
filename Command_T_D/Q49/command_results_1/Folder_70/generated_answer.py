def if_decimal_is_divisible(s):
    return (10 ** len(s) - 1) // 977 in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
