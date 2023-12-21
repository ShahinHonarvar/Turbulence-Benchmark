
def return_binary_or_hexa(test_list):
    a, b = test_list[77], test_list[84]
    odd = True
    try:
        sum_range = a + 1
        if sum_range > b - 1:
            sum_range = b - 1
        if a + 1 in test_list[77:84] and b - 1 in test_list[77:84]:
            return ""
        elif sum_range in test_list[77:84]:
            odd = False
        else:
            sum_range = a + 1
            test_list[77:84].remove(sum_range)
            sum_range = b - 1
            test_list[77:84].remove(sum_range)
            if len(test_list[77:84]) % 2 == 0:
                odd = False
    except (TypeError, ValueError):
        odd = False
    if odd:
        return format(sum(test_list[77:84]), "b")
    else:
        return format(sum(test_list[77:84]), "x")
