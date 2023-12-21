
def all_odd_ints_inclusive(lst):
    odd_nums = []
    for i in range(12, 93):
        if i % 2 != 0:
            odd_nums.append(lst[i])
    return odd_nums
