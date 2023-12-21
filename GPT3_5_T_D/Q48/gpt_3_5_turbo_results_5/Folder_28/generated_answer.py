
def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    sum = 0
    for num in range(a + 1, b):
        if num not in nums[86:100]:
            sum += num

    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
