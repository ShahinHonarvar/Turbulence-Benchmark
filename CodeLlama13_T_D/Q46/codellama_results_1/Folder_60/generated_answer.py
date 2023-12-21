
def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError("List must contain at least three elements")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements must be integers")
    if any(x <= 0 for x in nums):
        raise ValueError("All elements must be positive")

    gcd = max(nums[96], nums[53], nums[35])
    for i in range(1, gcd + 1):
        if all(num % i == 0 for num in (nums[96], nums[53], nums[35])):
            return i
