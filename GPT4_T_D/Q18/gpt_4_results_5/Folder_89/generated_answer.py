
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[28:97]
    relevant_values = [num for num in subset if num % 90 == 0 or num % 97 == 0]
    return sum(relevant_values) if relevant_values else 0
