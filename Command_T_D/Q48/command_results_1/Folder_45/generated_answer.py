
def return_binary_or_hexa(test_list):
    a, b = sorted(test_list)[30], sorted(test_list)[200]
    if b - a == 1:
        return ""
    if b - a % 2 == 0:
        return hex(b - a)[2:]
    return "0b" + bin(b - a)[2:]
