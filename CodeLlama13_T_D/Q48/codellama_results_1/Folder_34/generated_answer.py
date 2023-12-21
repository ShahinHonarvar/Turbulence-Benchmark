
def return_binary_or_hexa(nums):
    a, b = 60, 200
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in nums[a:b]:
            sum += 1
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return bin(sum)[2:]
