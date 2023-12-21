
def if_perfect_num(nums):
    try:
        num = nums[733]
    except IndexError:
        return False

    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisor_sum == num
