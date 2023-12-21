
def find_second_largest_num(num_list):
    if len(num_list) < 56:
        return None
    relevant_numbers = num_list[34:56]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[-2]
