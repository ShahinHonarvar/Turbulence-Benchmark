
def if_perfect_num(lst):
    num = lst[90]
    factors = [i for i in range(1, num) if num % i == 0]
    return sum(factors) == num
