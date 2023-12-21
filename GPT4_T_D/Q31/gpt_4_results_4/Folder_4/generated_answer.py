
def if_perfect_num(list_of_nums):
    if len(list_of_nums) > 15:
        num = list_of_nums[15]
        sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_of_divisors == num
    return False
