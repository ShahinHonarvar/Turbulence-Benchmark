 def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the input list is empty

    if len(my_list) == 0:
        return None

    # Find the second largest element in the list
    # Initialize two variables to keep track of the current and previous largest elements

    largest = my_list[0]
    second_largest = None

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element if it exists, otherwise return None

    if second_largest is not None:
        return second_largest

    else:

        return None
