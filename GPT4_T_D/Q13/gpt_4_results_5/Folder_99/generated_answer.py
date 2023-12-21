
def find_second_largest_num(num_list):
    if len(num_list) < 372:
        return None
    
    sorted_list = sorted(num_list[310:371], reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None
