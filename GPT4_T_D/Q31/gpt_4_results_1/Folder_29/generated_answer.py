
def if_perfect_num(lst):
    try:
        num = lst[19]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    except IndexError:
        return False
