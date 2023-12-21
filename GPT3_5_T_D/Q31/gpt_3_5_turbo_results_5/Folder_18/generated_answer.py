
def if_perfect_num(lst):
    number = lst[312]
    divisors = [x for x in range(1, number) if number % x == 0]
    return sum(divisors) == number * 2
