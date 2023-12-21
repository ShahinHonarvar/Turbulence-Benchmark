
def return_binary_or_hexa(test_list):
    a = 32
    b = 99
    counter = 0
    for item in test_list:
        if item == a or item == b:
            continue
        counter += 1
    if counter % 2 == 1:
        return format(sum(range(a + 1, b - 1)), 'b')
    else:
        return format(sum(range(a + 1, b - 1)), 'x')
