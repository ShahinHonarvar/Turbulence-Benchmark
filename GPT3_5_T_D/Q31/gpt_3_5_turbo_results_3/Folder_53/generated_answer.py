
def if_perfect_num(nums):
    num = nums[72]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    divisor_sum = sum(divisors)
    return divisor_sum == num
