
def all_even_ints_exclusive(nums):
    even_ints = []
    for num in nums[11:76]:
        if num % 2 == 0:
            even_ints.append(num)
    return even_ints
