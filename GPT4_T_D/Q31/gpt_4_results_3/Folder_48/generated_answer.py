
def if_perfect_num(list_of_positive_integers):
    num = list_of_positive_integers[247]
    divisor_sum = sum([i for i in range(1,num) if num%i == 0])
    if divisor_sum == num:
        return True
    return False
