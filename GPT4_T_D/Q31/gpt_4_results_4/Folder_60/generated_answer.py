
def if_perfect_num(nums):
    try:
        num = nums[88]
        sum_divisors = sum(i for i in range(1, num) if num % i == 0)
        return sum_divisors == num
    except IndexError:
        return False
