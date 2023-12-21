
def if_perfect_num(integer_list):
    num = integer_list[162]
    if num <= 0:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    if sum(divisors) == num:
        return True
    else:
        return False
