
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Create a copy of the list without the largest element
    filtered_list = my_list.copy()
    filtered_list.remove(largest)

    # Find the second largest element in the remaining elements
    try:
        second_largest = max(filtered_list)
    except ValueError:
        return None

    # Return the second largest element
    return second_largest
