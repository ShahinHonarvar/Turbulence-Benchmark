import fractions
def gcf_two_nums(nums):
    if len(nums) != 2:
        raise ValueError('gcf_two_nums() expects a list of 2 positive integers')
    return fractions.gcd(nums[0], nums[1])
