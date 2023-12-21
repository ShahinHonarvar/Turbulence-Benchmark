
def if_perfect_num(lst):
    if len(lst) > 632:
        number = lst[632]
        divisors = [i for i in range(1, number) if number % i == 0]
        return sum(divisors) == number
    else:
        return False
