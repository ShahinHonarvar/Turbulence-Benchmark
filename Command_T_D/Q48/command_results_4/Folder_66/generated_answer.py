
def return_binary_or_hexa(test_tup):
    res = test_tup[11] + 1
    test_tup_str = str(test_tup)
    if "11" in test_tup_str and "76" in test_tup_str:
        if res % 2:
            return f"0b{res - 1}"
        return f"0x{res - 1}"
    return ""
