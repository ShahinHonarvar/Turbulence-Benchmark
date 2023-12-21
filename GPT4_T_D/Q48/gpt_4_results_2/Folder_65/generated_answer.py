
def return_binary_or_hexa(input_tuple):
    a = input_tuple[51]
    b = input_tuple[76]
    current_set = set(input_tuple[52:76])
    sum_absent = sum(i for i in range(a + 1, b) if i not in current_set)
    if sum_absent == 0:
        return ""
    return bin(sum_absent)[2:] if sum_absent % 2 else hex(sum_absent)[2:].upper()
