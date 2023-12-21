
def if_perfect_num(lst):
    num = lst[40]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num
