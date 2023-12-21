
def sum_odd_ints_inclusive(lst):
    odd_nums = []
    for i in range(4, 9):
        if lst[i] % 2 != 0:
            odd_nums.append(lst[i])
    return sum(odd_nums)
