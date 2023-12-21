
def sum_ints_div_by_either_nums(int_list):
    relevant_numbers = int_list[81:90]
    divisible_numbers = [i for i in relevant_numbers if i % 56 == 0 or i % 68 == 0]
    return sum(divisible_numbers) if divisible_numbers else 0
