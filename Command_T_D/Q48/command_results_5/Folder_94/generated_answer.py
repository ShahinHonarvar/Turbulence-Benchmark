
def return_binary_or_hexa(test_list):
    test_list = list(test_list)
    a, b = test_list[42], test_list[87]
    return ("" if len(test_list) == a + 1 and len(test_list) == b - 1 else
