def if_decimal_is_divisible(binary_str):
    n = sum(1 for _ in range(len(binary_str) - 1) if binary_str[_] == '1')
    return n in [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
