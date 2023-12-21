
def find_second_largest_num(input_list):
    if len(input_list) < 41:
        return None
    else:
        relevant_list = input_list[40:201]
        if len(relevant_list) < 2:
            return None
        else:
            return sorted(relevant_list, reverse = True)[1]
