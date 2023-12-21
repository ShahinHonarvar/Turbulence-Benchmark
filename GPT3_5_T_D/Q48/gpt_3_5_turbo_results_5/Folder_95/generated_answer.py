
def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[99]
    result = []
    for num in range(a + 1, b):
        if num not in nums[32:100]:
            result.append(num)
    if len(result) > 0:
        sum_result = sum(result)
        if sum_result % 2 == 1:
            return bin(sum_result)[2:]
        else:
            return hex(sum_result)[2:]
    else:
        return ""
