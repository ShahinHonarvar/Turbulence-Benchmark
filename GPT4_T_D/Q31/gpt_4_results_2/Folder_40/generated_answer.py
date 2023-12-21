
def if_perfect_num(integer_list):
    index_seven = integer_list[7]
    factors = [i for i in range(1, index_seven) if index_seven % i == 0]
    if sum(factors) == index_seven:
        return True
    else:
        return False
