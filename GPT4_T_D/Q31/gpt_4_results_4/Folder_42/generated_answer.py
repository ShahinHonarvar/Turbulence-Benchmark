
def if_perfect_num(nums):
    if len(nums) > 276:
        number = nums[276]
        factors = [i for i in range(1, number) if number % i == 0]
        if sum(factors) == number:
            return True
    return False
