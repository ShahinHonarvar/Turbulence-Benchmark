
def return_binary_or_hexa(test_list):
    a = test_list[49]
    b = test_list[74]
    list_1 = list(range(a + 1, b))
    list_2 = list(range(a + 1, b - 1))
    list_3 = [x for x in list_2 if x not in list_1]
    sum_1 = sum(list_3)
    if sum_1 % 2:
        return format(sum_1, "b")
    else:
        return format(sum_1, "x")
