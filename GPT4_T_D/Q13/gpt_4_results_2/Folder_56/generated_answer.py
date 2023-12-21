
def find_second_largest_num(numbers):
    num_list_upto_index_zero = numbers[0:1]
    if len(num_list_upto_index_zero) < 2:
        return None
    else:
        return sorted(num_list_upto_index_zero)[-2]
