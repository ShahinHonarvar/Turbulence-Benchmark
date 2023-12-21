
def return_binary_or_hexa(test_list):
    a, b = test_list[13], test_list[76]
    num = a + 1
    if num <= b - 1:
        if num not in test_list[13:76]:
            return str(sum(test_list[13:76]) % 2)
        else:
            return str(sum(test_list[13:76]) % 2)
    else:
        return ""
