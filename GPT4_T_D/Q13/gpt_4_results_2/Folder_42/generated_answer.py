
def find_second_largest_num(num_list):
    if 29 <= len(num_list)-1 < 79:
        eligible_numbers = num_list[29:80]
    else:
        eligible_numbers = num_list[29:]
        
    if len(eligible_numbers) < 2:
        return None

    eligible_numbers.sort()
    return eligible_numbers[-2]
