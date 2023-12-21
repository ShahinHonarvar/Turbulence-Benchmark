
def find_second_smallest_num(my_list):
    # find the smallest element in the list
    smallest = min(my_list)
    
    # find the second smallest element by filtering out the smallest element from the list and finding the minimum of what's left
    second_smallest = min(filter(lambda x: x != smallest, my_list))
    
    return second_smallest
