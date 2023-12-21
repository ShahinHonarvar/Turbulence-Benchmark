def sum_even_ints_inclusive(nums):
    even_nums = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return sum(nums[even_num] for even_num in even_nums if even_num <= 7)
