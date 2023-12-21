
def if_perfect_num(list_of_positive_integers):
    return list_of_positive_integers[702] in perfect_numbers(list_of_positive_integers)

def perfect_numbers(list_of_positive_integers):
    return [i for i in list_of_positive_integers if sum(divisors(i)) == 2*i]

def divisors(n):
    return [i for i in range(1, int(n**0.5)+1) if n % i == 0]
