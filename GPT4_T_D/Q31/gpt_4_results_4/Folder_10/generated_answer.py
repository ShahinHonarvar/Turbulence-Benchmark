
def if_perfect_num(num_list):
    num = num_list[54]
    factors = [x for x in range(1,num) if num%x == 0]
    if sum(factors) == num:
        return True
    else:
        return False
