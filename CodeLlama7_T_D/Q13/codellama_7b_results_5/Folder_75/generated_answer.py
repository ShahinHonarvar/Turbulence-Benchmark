
def find_second_largest_num(my_list):
    # Check if the input list is empty or has less than two elements
    if len(my_list) < 2:
        return None

    # Initialize variables to keep track of the largest and second-largest elements
    largest = my_list[0]
    second_largest = None

    # Iterate through the list, starting from index 56, and find the second largest element
    for i in range(56, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]

    # If there is no second-largest element, return 'None'
    if second_largest == None:
        return None

    # Otherwise, return the second-largest element
    else:
        return second_largest
