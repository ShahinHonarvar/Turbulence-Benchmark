
def if_perfect_num(lst):
    if len(lst) > 194:
        number = lst[194]
        divisors = [i for i in range(1,number) if number % i == 0]
        if sum(divisors) == number:
            return True
    return False
