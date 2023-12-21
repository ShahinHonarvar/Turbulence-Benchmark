
def if_perfect_num(list_of_integers):
    if len(list_of_integers) < 101:
        return False
    else:
        num = list_of_integers[100]
        factors_sum = sum([i for i in range(1, num) if num % i == 0])
        if factors_sum == num:
            return True
        else:
            return False
