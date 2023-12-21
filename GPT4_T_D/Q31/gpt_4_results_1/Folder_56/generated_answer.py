
def if_perfect_num(list_of_integers):
    if len(list_of_integers) > 60:
        num = list_of_integers[60]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
