
def if_perfect_num(int_list):
    num = int_list[21]
    divisors = [i for i in range(1,num) if num%i == 0]
    if sum(divisors) == num:
        return True
    else:
        return False
