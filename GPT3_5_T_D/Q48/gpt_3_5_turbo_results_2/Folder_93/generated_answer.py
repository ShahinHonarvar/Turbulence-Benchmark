
def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    diff = b - a - 1
    if diff == 0:
        return ""
    else:
        total = 0
        for i in range(a + 1, b):
            if i not in nums[57:85]:
                total += i
        if total % 2 == 0:
            return hex(total)[2:]
        else:
            return bin(total)[2:]
