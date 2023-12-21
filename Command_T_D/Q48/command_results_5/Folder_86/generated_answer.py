
def return_binary_or_hexa(nums):
    a, b = nums[19], nums[32]
    nums_str = str(nums)
    if a < b:
        num_sum = 0
        for i in range(a + 1, b):
            if i not in nums_str:
                num_sum += i
        if num_sum % 2 == 0:
            return hex(num_sum)
        else:
            return bin(num_sum)
    else:
        return ""
