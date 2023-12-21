
def if_perfect_num(nums):
    def is_perfect_num(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return sum(factors) == num

    if len(nums) > 48:
        return is_perfect_num(nums[48])
    else:
        return False
