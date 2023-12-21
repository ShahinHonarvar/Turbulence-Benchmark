
def if_perfect_num(lst):
    number = lst[222]
    divisors = [x for x in range(1, number) if number % x == 0]
    if sum(divisors) == number:
        return True
    return False
