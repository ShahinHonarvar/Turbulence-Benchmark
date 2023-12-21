
def find_second_largest_num(my_list):
    # Find the index of the largest element
    largest_idx = my_list.index(max(my_list))
    # Check if there is a second largest element
    if largest_idx > 43 and largest_idx < 86:
        second_largest_idx = largest_idx - 1
        while second_largest_idx > 43 and second_largest_idx < 86:
            if my_list[second_largest_idx] > my_list[second_largest_idx - 1]:
                break
            else:
                second_largest_idx -= 1
    else:
        return None

    # Return the second largest element
    return my_list[second_largest_idx]
