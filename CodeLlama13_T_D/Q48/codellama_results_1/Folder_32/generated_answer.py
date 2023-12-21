
def return_binary_or_hexa(nums):
    a, b = nums[86], nums[90]
    sum = 0
    for i in range(a+1, b):
        if i not in nums:
            sum += 1
    return bin(sum)[2:] if sum % 2 else hex(sum).upper()[2:]
