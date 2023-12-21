
def return_binary_or_hexa(test_list):
    list_test = sorted(test_list)
    if len(test_list) == 85:
        return ""
    a = list_test[57]
    b = list_test[85]
    odd = True
    if a % 2 == 1:
        odd = True
    else:
        odd = False
    if b % 2 == 1:
        odd = True
    else:
        odd = False
    sum_of_not_present = 0
    for i in range(a + 1, b - 1):
        if i not in test_list:
            sum_of_not_present += i
    if odd:
        return format(sum_of_not_present, "b")
    else:
        return format(sum_of_not_present, "x")
