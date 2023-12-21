
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the second largest element in the list
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] > my_list[62] and my_list[i] < my_list[63]:
            if second_largest == None:
                second_largest = my_list[i]
            else:
                if my_list[i] > second_largest:
                    second_largest = my_list[i]

    # Return the second largest element
    return second_largest
