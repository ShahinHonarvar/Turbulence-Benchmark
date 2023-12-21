
def if_perfect_num(list_nums):
    if len(list_nums) > 247:
        num = list_nums[247]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
