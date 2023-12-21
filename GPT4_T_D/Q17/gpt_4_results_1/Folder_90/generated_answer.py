
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for i in range(138, 425):
        if i >= len(lst):
            break
        if lst[i] % -863 == 0 and lst[i] % -329 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums
