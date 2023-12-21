
def all_odd_ints_inclusive(nums):
    odd_ints = []
    for num in nums[5:8]:
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints
