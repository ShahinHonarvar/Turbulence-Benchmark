
def if_perfect_num(nums):
    if len(nums) > 459:
        divisors = [i for i in range(1, nums[459]) if nums[459] % i == 0]
        if sum(divisors) == nums[459]:
            return True
    return False
