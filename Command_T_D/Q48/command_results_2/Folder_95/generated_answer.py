
def return_binary_or_hexa(test_list):
    a, b = 32, 99
    result = a + 1
    if result in test_list:
        return ''
    while result < b:
        if result not in test_list:
            result += 1
        else:
            break
    if result == b - 1:
        return str(result)
    return str(result)
