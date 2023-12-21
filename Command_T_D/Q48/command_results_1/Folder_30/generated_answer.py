
def return_binary_or_hexa(test_list):
    test_list = list(test_list)
    a, b = test_list[22], test_list[24]
    if a == b:
        return ""
    result = 0
    for i in range(a + 1, b - 1):
        if i not in test_list[22:]:
            result += i
    if result % 2 == 1:
        return f"0b{result:b}"
    else:
        return f"0x{result:x}"
