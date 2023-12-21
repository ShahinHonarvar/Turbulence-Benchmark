
def all_odd_ints_exclusive(lst):
    odd_nums = []
    for num in lst[44:67]:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums
