
def return_binary_or_hexa(test_list):
    list_sum = 0
    for i in range(20, 51):
        if test_list[i] not in test_list[20:51]:
            list_sum += test_list[i]
    if list_sum % 2:
        return f"0b{list_sum:b}"
    else:
        return f"0x{list_sum:x}"
