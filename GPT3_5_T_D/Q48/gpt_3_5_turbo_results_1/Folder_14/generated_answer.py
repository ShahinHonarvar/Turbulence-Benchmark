
def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[5]
    total = 0
    for i in range(a + 1, b):
        if i not in nums[2:5]:
            total += i
    
    if total == 0:
        return ""
    elif total%2 != 0:
        return format(total, 'b')
    else:
        return format(total, 'x')
