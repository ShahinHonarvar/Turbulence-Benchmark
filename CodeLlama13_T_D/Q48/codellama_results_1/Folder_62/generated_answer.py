
def return_binary_or_hexa(nums):
    a = nums[50] + 1
    b = nums[92] - 1
    result = []
    for i in range(a, b+1):
        if i not in nums:
            result.append(i)
    sum = 0
    for i in result:
        sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
