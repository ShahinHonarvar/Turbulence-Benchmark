
def if_perfect_num(integer_list):
    num = integer_list[38]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    
    if sum(divisors) == num:
        return True
    else:
        return False
