
def if_perfect_num(list_of_integers):
    if len(list_of_integers) > 733:
        number = list_of_integers[733]
        sum_of_divisors = 0
        for i in range(1, number):
            if number % i == 0:
                sum_of_divisors += i
        if sum_of_divisors == number:
            return True
    return False
