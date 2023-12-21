
def if_perfect_num(num_list):
    index_67 = num_list[67]
    divisors = [i for i in range(1, index_67) if index_67 % i == 0]
    if sum(divisors) == index_67:
        return True
    return False
