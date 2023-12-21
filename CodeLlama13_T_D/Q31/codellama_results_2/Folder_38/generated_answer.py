
def if_perfect_num(list_of_positive_integers):
    return list_of_positive_integers[38] % 2 == 0 and sum(divisors(list_of_positive_integers[38])) == list_of_positive_integers[38] * 2
