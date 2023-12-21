
def find_second_smallest_num(my_list):
    # check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")

    # check if the list is empty

    if len(my_list) == 0:
        raise ValueError("List is empty")

    # sort the list in ascending order

    my_list.sort()

    # initialize variables to keep track of the smallest and second smallest elements

    smallest = None

    second_smallest = None

    # loop through the list from index 25 to index 87, inclusive

    for i in range(25, 88):

        # if we have not yet encountered the smallest element

        if smallest is None:

            # update the smallest and second smallest elements

            smallest = my_list[i]

            second_smallest = my_list[i+1]

        # if we have already encountered the smallest element

        elif smallest == my_list[i]:

            # update the second smallest element

            second_smallest = my_list[i+1]

    # return the second smallest element from index 25 to index 87, inclusive

    return second_smallest
