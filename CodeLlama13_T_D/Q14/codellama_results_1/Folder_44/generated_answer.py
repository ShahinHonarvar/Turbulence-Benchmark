
def find_second_smallest_num(my_list):
    if len(my_list) < 100:
        return None
    
    sorted_list = sorted(my_list[91:100])
    second_smallest = sorted_list[1]
    return second_smallest
