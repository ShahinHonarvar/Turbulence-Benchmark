
def find_second_largest_num(num_list):
    if len(num_list) < 201 or len(num_list[200:201]) < 2:
        return None
    else:
        sorted_list = sorted(num_list[200:201], reverse=True)
        return sorted_list[1]
