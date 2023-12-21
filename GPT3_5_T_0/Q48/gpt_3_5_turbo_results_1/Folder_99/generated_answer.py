
def return_binary_or_hexa(nums):
    a = nums[427]
    b = nums[669]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in nums[427:670]:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
