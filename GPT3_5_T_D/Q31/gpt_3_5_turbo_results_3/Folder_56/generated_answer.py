
def if_perfect_num(nums):
    return sum_of_factors(nums[60]) == nums[60]

def sum_of_factors(num):
    factors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return sum(factors) if num > 1 else 0
