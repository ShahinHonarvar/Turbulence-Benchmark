
def return_binary_or_hexa(nums):
    a, b = nums[56], nums[88]
    sum_of_ints = sum([i for i in range(a + 1, b) if i not in nums])
    if sum_of_ints % 2 == 0:
        return f"{sum_of_ints:x}"
    else:
        return bin(sum_of_ints)[2:]
