
def if_perfect_num(nums):
    number = nums[34]
    sum_divisors = sum(i for i in range(1, number) if number % i == 0)
    return sum_divisors == number
