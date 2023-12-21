
def if_perfect_num(num_list):
    try:
        target_num = num_list[34]
    except IndexError:
        return False

    divisors = [i for i in range(1, target_num) if target_num % i == 0]

    if sum(divisors) == target_num:
        return True
    else:
        return False
