
def sum_even_ints_inclusive(int_list):
    relevant_nums = int_list[639:976]
    even_nums = [num for num in relevant_nums if num % 2 == 0]
    return sum(even_nums) if even_nums else 0
