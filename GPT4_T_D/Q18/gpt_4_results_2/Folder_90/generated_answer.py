
def sum_ints_div_by_either_nums(nums):
    sublist = nums[138:425]
    total = sum(num for num in sublist if num % -863 == 0 or num % -329 == 0)
    return total
