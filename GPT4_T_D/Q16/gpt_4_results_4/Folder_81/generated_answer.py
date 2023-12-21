
def sum_even_ints_inclusive(int_list):
    relevant_subset = int_list[10:101]
    sum_evens = sum(i for i in relevant_subset if i % 2 == 0)
    return sum_evens
