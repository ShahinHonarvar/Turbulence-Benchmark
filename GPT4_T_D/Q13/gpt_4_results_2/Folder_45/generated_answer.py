
def find_second_largest_num(num_list):

    if len(num_list) < 32:
        return None

    num_list = num_list[30:201] if len(num_list) > 201 else num_list[30:]
    
    if len(num_list) < 2:
        return None

    num_list.sort(reverse=True)

    return num_list[1]
