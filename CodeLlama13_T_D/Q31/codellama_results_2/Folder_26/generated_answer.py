
def if_perfect_num(nums):
    if len(nums) <= 222:
        return False
    else:
        n = nums[222]
        sum_divisors = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                sum_divisors += i
                if n // i != i:
                    sum_divisors += n // i
        return sum_divisors == n
