
def if_perfect_num(num_list):
    num = num_list[3]
    divisors = [i for i in range(1, num) if num % i == 0]
    if sum(divisors) == num:
        return True
    return False
