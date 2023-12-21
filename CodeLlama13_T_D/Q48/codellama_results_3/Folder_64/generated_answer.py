
def return_binary_or_hexa(nums):
    sum = 0
    for i in range(1, len(nums) - 1):
        if nums[i] not in nums[0:5]:
            sum += nums[i]
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
