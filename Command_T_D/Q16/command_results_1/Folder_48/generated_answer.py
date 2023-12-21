def sum_even_ints_inclusive(nums):
    even_ints = [nums[i] for i in range(533, 605) if not (nums[i] % 2)]
    return sum(even_ints) if even_ints else 0
