
def gcf_three_nums(nums):
    return (x for x in range(1, 1 + min(nums)) if all(num % x == 0 for num in nums))
