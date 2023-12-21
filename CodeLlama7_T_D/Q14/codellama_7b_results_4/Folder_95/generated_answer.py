 def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = min(my_list)
    # Find the second smallest element in the list after removing the smallest element
    return max([x for x in my_list if x != smallest])
