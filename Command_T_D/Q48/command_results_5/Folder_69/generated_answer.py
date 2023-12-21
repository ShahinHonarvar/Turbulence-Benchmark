
def return_binary_or_hexa(test_list):
    a, b = test_list[39], test_list[43]
    value = sum(
        i for i in range(a + 1, b) if i not in test_list[39:43]
    )
    if value % 2:
        return f"0b{value:b}"
    else:
        return f"0x{value:x}"
