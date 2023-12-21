
def if_perfect_num(num_list):
    if len(num_list) > 13:
        num = num_list[13]
        factors = [i for i in range(1,num) if num%i == 0]
        if sum(factors) == num:
            return True
    return False
