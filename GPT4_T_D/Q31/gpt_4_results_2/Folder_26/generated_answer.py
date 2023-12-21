
def if_perfect_num(int_list):
    if len(int_list) > 222:
        perfect_num_candidate = int_list[222]
        factors_list = [i for i in range(1, perfect_num_candidate) if perfect_num_candidate % i == 0]
        if sum(factors_list) == perfect_num_candidate:
            return True
    return False
