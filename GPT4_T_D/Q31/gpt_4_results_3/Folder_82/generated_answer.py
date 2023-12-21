
def if_perfect_num(nums):
    def is_perfect(n):
        factors = [i for i in range(1, n) if n % i == 0]
        return sum(factors) == n

    if len(nums) > 83:
        return is_perfect(nums[83])
    else:
        return False
