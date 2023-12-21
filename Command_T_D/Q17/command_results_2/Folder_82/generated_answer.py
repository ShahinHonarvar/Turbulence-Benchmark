
def all_ints_div_by_both_two_nums(nums):
    lst = []
    for i in range(20, 200):
        if i % 20 == 0 and i % 200 == 0:
            lst.append(i)
    return lst
