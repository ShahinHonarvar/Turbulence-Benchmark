
def if_perfect_num(nums):
    def is_perfect(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num

    if len(nums) > 38:
        return is_perfect(nums[38])
    else:
        return False
