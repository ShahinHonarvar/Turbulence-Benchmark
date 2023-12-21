
def if_perfect_num(num_list):
    index_18 = num_list[18]

    factors = [i for i in range(1, index_18) if index_18 % i == 0]
    if sum(factors) == index_18:
        return True
    else:
        return False
