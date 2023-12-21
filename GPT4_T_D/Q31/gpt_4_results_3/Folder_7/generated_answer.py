
def if_perfect_num(nums):
    try:
        num = nums[851]
        factors = [i for i in range(1, num) if num % i == 0]
        if sum(factors) == num:
            return True
        else:
            return False
    except IndexError:
        return False
