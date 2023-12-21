
def if_perfect_num(nums):
    try:
        num = nums[21]
        sum_factors = sum(i for i in range(1, num) if num % i == 0)
        return sum_factors == num
    except IndexError:
        return False
