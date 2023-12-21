
def return_binary_or_hexa(test_list):
    a, b = sorted(test_list)[32], sorted(test_list)[44]
    count = 0
    for i in range(a + 1, b - 1):
        if i not in test_list:
            count += 1
    if count % 2 == 1:
        return format(count, 'b')
    else:
        return format(count, 'x')
