
def find_second_largest_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return None

    # Find the second largest element in the list
    # Initialize variables to keep track of the largest and second-largest elements
    largest = my_list[0]
    second_largest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif my_list[i] > second_largest and my_list[i] != largest:
            second_largest = my_list[i]
    # If the second-largest element is within the given range, return it
    if second_largest >= my_list[56] and second_largest <= my_list[82]:
        return second_largest

    # Otherwise, return None

    else:

        return None
