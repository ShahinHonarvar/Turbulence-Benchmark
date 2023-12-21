
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the index of the second largest element
    second_largest_idx = -1
    for i in range(30, 201):
        if my_list[i] > my_list[i-1] and my_list[i] > my_list[i+1]:
            second_largest_idx = i

    # Return the second largest element if found
    if second_largest_idx != -1:
        return my_list[second_largest_idx]

    # Otherwise, return None
    else:
        return None
