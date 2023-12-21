
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[79]

    if b - a < 2:
        return ""

    total = 0
    for i in range(a + 1, b):
        if i not in nums[10:80]:
            total += i

    if total % 2 == 1:
        return format(total, 'b')
    else:
        return format(total, 'X')
