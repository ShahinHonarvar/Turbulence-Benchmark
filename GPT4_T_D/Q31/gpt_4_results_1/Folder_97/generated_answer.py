
def if_perfect_num(num_list):
    if len(num_list) > 132:
        num = num_list[132]
        divisors = [i for i in range(1,num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
