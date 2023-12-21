
def if_perfect_num(num_list):
    if len(num_list) > 33:
        num = num_list[33]
        divisor_list = [i for i in range(1, num) if num % i == 0]
        if sum(divisor_list) == num:
            return True
    return False
