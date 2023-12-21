
def if_perfect_num(list_of_integers):
    num = list_of_integers[67]
    factors = [i for i in range(1, num) if num % i == 0]
    if sum(factors) == num:
        return True
    else:
        return False
