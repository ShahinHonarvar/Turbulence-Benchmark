
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Get the length of the list
    n = len(my_list)
    # Check if the list is empty
    if n == 0:
        return None

    # Initialize variables to keep track of the largest and second largest elements
    largest = my_list[0]
    second_largest = None

    # Iterate through the list and find the largest and second largest elements
    for i in range(1, n):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif (my_list[i] > second_largest) and (second_largest is not None):
            second_largest = my_list[i]

    # Return the second largest element if it exists, otherwise return 'None'
    if second_largest is not None:
        return second_largest

    else:

        return None
