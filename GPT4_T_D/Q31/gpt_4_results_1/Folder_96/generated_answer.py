
def if_perfect_num(lst):
    number = lst[47]
    divisors = [i for i in range(1, number) if number % i == 0]
    if sum(divisors) == number:
        return True
    return False
