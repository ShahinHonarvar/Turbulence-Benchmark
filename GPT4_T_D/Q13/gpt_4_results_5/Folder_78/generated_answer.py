
def find_second_largest_num(input_list):
    relevant_list = input_list[43:52]
    if not relevant_list:
        return None
    relevant_list.sort()
    return relevant_list[-2] if len(relevant_list) > 1 else None
