
def return_binary_or_hexa(nums):
    a, b = 29, 53
    sum = 0
    for i in range(a+1, b-1):
        if nums[i] not in range(29, 54):
            sum += nums[i]
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return bin(sum)[2:]
