
def all_ints_div_by_both_two_nums(num_list):
    found_numbers = []
    for i in range(42, 88):
        if num_list[i] % -90 == 0 and num_list[i] % -74 == 0:
            found_numbers.append(num_list[i])
    return found_numbers
