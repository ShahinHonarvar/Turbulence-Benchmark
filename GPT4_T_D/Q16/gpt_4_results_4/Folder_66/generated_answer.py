
def sum_even_ints_inclusive(int_list):
    relevant_ints = int_list[50:55]
    return sum(i for i in relevant_ints if i % 2 == 0)
