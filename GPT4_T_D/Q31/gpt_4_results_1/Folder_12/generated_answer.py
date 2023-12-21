
def if_perfect_num(num_list):
    if len(num_list)<28:
        return False
    num = num_list[27]
    divisors = [i for i in range(1,num) if num%i==0]
    if sum(divisors)==num:
        return True
    else:
        return False
