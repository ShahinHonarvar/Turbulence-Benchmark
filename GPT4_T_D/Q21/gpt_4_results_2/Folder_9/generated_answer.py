
def all_ints_div_by_num(lst):
    divisible_by_4 = []
    for i in range(20, min(201, len(lst))):
        if lst[i] % 4 == 0:
            divisible_by_4.append(lst[i])
    return divisible_by_4
