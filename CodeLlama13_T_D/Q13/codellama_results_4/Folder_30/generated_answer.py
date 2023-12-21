
def find_second_largest_num(my_list):
    # Sort the list in descending order
    my_list.sort(reverse=True)
    
    # Find the second largest element from index 55 to index 98, both inclusive
    second_largest = None
    for i in range(55, 99):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    
    return second_largest
