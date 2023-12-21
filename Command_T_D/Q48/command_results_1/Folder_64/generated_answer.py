
def return_binary_or_hexa(test_list):
    res = sum(range(test_list[0] + 1, test_list[5] - 1))
    if res % 2 == 1:
        return f"0b{res:b}"
    return f"0x{res:x}"
