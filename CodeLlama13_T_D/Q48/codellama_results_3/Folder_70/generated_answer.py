
def return_binary_or_hexa(nums):
    a = nums[43]
    b = nums[70]
    result = 0
    for i in range(a+1, b-1+1):
        if i not in nums:
            result += 1
    return "{:b}".format(result) if result % 2 else "{:x}".format(result).upper()
