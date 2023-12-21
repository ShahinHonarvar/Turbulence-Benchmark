
def return_binary_or_hexa(nums):
    sum = 0
    for i in range(nums[0] + 1, nums[10] - 1):
        if i not in nums:
            sum += 1
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return bin(sum)[2:]
