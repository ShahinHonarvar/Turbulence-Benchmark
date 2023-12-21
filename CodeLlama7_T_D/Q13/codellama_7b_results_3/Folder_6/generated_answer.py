
def find_second_largest_num(my_list):
    # check if list is empty
    if len(my_list) == 0:
        return None

    # sort the list in ascending order
    my_list.sort()

    # initialize variables to keep track of the second largest element
    second_largest = None
    index = 10

    # loop through the list and find the second largest element
    for i in range(index, len(my_list)):
        if my_list[i] > my_list[i - 1]:
            second_largest = my_list[i]

    # return the second largest element or None if it doesn't exist
    return second_largest
