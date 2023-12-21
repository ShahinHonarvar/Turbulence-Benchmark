
def sum_odd_ints_inclusive(my_list):
    odd_nums = []
    for i in range(43, 87):
        if my_list[i] % 2 == 1:
            odd_nums.append(my_list[i])
    return sum(odd_nums) or 0
