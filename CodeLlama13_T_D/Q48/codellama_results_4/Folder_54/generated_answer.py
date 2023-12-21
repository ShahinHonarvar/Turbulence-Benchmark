
def return_binary_or_hexa(nums):
    a = nums[35] + 1
    b = nums[64] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in nums:
            sum += i
    if sum % 2 == 0:
        return "{:x}".format(sum)
    else:
        return bin(sum)[2:]
