
def if_perfect_num(list_of_nums):
    try:
        num = list_of_nums[714]
    except IndexError:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    if sum(divisors) == num:
        return True
    return False
