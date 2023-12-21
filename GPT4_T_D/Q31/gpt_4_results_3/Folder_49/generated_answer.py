
def if_perfect_num(lst):
    index_val = lst[68]
    factors = [i for i in range(1, index_val) if index_val % i == 0]
    return sum(factors) == index_val
