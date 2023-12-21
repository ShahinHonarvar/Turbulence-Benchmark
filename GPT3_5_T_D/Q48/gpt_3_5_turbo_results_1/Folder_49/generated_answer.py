
def return_binary_or_hexa(nums):
    a = nums[80]
    b = nums[200]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in nums[81:200]:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
