
def return_binary_or_hexa(test_list):
    lst_50_92 = list(range(test_list[50] + 1, test_list[92] - 1))
    if len(set(lst_50_92)) == len(lst_50_92):
        return ""
    if sum(lst_50_92) % 2 == 1:
        return bin(sum(lst_50_92))
    else:
        return hex(sum(lst_50_92))
