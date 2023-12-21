
def return_binary_or_hexa(nums):
    a, b = nums[32], nums[99]
    sum_ = 0
    for i in range(a+1, b-1):
        if i not in nums:
            sum_ += i
    return bin(sum_) if sum_ % 2 else hex(sum_)
