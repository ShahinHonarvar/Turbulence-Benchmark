 def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
    # Initialize a variable to store the second smallest element
    second_smallest = None

    # Iterate through the list and find the second smallest element

    for i in range(len(my_list)):
        if my_list[i] > smallest and (second_smallest == None or my_list[i] < second_smallest):
            second_smallest = my_list[i]
    # Return the second smallest element

    return second_smallest
