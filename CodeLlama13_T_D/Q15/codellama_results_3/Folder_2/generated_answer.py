
def sum_odd_ints_inclusive(my_list):
    odd_ints = []
    for i in range(15, 40):
        if my_list[i] % 2 == 1:
            odd_ints.append(my_list[i])
    return sum(odd_ints) or 0
