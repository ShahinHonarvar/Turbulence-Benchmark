
def return_binary_or_hexa(test_list):
    a = test_list[20]
    b = test_list[36]
    result = sum(x for x in range(a + 1, b - 1) if x not in test_list[20:36])
    return "0b{:b}".format(result) if result % 2 else "{:x}".format(result)
