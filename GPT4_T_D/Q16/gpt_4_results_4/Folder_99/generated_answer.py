
def sum_even_ints_inclusive(nums):
    selected_nums = nums[310:371]
    even_nums = [num for num in selected_nums if num % 2 == 0]
    return sum(even_nums) if even_nums else 0
