
def if_perfect_num(num_list):
    index_40_num = num_list[40]
    factors = [i for i in range(1, index_40_num) if index_40_num % i == 0]
    return sum(factors) == index_40_num
