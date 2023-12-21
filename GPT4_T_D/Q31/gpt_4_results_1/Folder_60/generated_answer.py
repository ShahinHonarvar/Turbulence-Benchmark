
def if_perfect_num(int_list):
    if len(int_list) > 88:
        num = int_list[88]
        factors = [i for i in range(1, num) if num % i == 0]
        if sum(factors) == num:
            return True
    return False
