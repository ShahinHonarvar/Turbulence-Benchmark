
def if_perfect_num(list_of_integers):
    number = list_of_integers[77]
    sum_of_factors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_factors += i
    
    if sum_of_factors == number:
        return True
    else:
        return False
