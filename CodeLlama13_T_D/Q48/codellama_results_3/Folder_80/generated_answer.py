
def return_binary_or_hexa(nums):
    a, b = nums[57], nums[84]
    sum = 0
    for i in range(a+1, b):
        if i not in nums:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum).upper()[2:]
