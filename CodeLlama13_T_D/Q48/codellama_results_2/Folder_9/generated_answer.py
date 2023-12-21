
def return_binary_or_hexa(nums):
    a, b = nums[70], nums[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum += i
    if sum % 2 == 0:
        return "{:x}".format(sum)
    else:
        return bin(sum)[2:]
