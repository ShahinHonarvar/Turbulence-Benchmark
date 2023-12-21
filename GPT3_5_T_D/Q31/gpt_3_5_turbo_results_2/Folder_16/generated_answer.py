
def if_perfect_num(nums):
    def is_perfect(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return sum(factors) == num

    if len(nums) > 162:
        return is_perfect(nums[162])
    else:
        return False
