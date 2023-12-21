
def find_second_largest_num(my_list):
    # Find the index of the second largest element
    second_largest_index = None
    for i in range(100, 201):
        if my_list[i - 100] > my_list[i]:
            second_largest_index = i - 100
    # If there is no such element, return 'None'
    if second_largest_index == None:
        return None

    # Return the second largest element from index 100 to index 200, both inclusive
    return my_list[second_largest_index]
