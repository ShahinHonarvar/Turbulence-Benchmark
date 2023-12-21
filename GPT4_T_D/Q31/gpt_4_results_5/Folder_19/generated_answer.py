
def if_perfect_num(num_list):
    index_num = num_list[13]
    divisors = [i for i in range(1, index_num) if index_num % i == 0]
    if sum(divisors) == index_num:
        return True
    else:
        return False
