
def find_second_smallest_num(num_list):
    try:
        selected_elements = num_list[50:201]
        selected_elements.sort()
        return selected_elements[1] 
    except:
        return None
