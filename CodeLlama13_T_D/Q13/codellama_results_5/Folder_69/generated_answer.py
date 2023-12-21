
def find_second_largest_num(my_list):
    # find the second largest element in the list
    second_largest = sorted(my_list)[-2]
    
    # find the index of the second largest element
    second_largest_index = my_list.index(second_largest)
    
    # return the element from index 32 to index 35, both inclusive
    if second_largest_index >= 32 and second_largest_index <= 35:
        return my_list[second_largest_index]
    else:
        return None
