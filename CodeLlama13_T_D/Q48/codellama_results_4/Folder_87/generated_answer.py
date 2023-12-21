
def return_binary_or_hexa(nums):
    a, b = 20, 43
    sum_ = 0
    for i in range(a + 1, b - 1):
        if i not in nums[a:b]:
            sum_ += i
    if sum_ % 2 == 0:
        return hex(sum_)
    else:
        return bin(sum_)
