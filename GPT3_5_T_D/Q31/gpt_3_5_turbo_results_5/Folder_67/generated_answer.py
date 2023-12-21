
def if_perfect_num(nums):
    def is_perfect(num):
        factors = []
        for i in range(1, int(num/2) + 1):
            if num % i == 0:
                factors.append(i)
        if sum(factors) == num:
            return True
        return False

    if len(nums) <= 43:
        return False
    return is_perfect(nums[43])
