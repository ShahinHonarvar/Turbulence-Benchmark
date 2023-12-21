
def sum_even_ints_inclusive(int_list):
    relevant_ints = int_list[246:751]
    even_ints_sum = sum(i for i in relevant_ints if i % 2 == 0)
    return even_ints_sum
