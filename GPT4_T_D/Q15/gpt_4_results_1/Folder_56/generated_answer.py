
def sum_odd_ints_inclusive(integer_list):
    return sum(integer_list[i] for i in range(len(integer_list)) if i==0 and integer_list[i] % 2 != 0)
