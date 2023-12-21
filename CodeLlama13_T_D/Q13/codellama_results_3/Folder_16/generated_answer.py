
def find_second_largest_num(my_list):
    # Find the second largest element in the list
    second_largest = None
    for i in range(33, 37):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    
    return second_largest
