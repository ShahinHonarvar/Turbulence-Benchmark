def if_decimal_is_divisible(binary):
    return binary.count("1") == 1 and len(binary) == 9 and binary[0] == "1" and binary[8] == "1"
