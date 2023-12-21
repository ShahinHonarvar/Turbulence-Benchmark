
def return_binary_or_hexa(nums):
    a, b = nums[29], nums[53]
    if a < b:
        sum_ = 0
        for i in range(a + 1, b - 1):
            if i not in nums:
                sum_ += i
        if sum_ % 2:
            return bin(sum_)[2:-1]
        return hex(sum_[0])[2:-1]
