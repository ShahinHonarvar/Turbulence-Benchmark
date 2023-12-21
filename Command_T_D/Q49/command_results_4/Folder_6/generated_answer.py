def if_decimal_is_divisible(binary):
    return (10**9+7 - binary.count("1")) % 1000000009 == 10**9+6
