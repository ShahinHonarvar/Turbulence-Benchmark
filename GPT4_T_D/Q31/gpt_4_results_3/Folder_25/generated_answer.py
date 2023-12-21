
def if_perfect_num(list_of_ints):
    num = list_of_ints[90]
    factors = [i for i in range(1, num) if num % i == 0]
    if sum(factors) == num:
        return True
    else:
        return False
