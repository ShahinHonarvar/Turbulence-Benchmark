
def all_odd_ints_inclusive(lst):
    odd_nums = []
    
    for num in lst[55:99]:
        if num % 2 != 0:
            odd_nums.append(num)
    
    return odd_nums
