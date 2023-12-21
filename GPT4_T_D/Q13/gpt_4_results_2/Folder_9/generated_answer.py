
def find_second_largest_num(input_list):
    if len(input_list[200:201]) < 1:
        return None
    else:
        return sorted(input_list[200:201], reverse=True)[0]
