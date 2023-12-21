
def if_perfect_num(integer_list):
    if len(integer_list) > 8:
        num = integer_list[8]
        factors = [i for i in range(1, num) if num % i == 0]
        if sum(factors) == num:
            return True
    return False
