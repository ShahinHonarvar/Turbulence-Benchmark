
def if_perfect_num(num_list):
    if len(num_list) > 410:
        num = num_list[410]
        divisors = [i for i in range(1, num) if num % i == 0]
        if num == sum(divisors):
            return True
    return False
