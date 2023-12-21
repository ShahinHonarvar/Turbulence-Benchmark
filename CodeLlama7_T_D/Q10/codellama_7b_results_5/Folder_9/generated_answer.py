
def all_odd_ints_exclusive(my_list):
    # initialize an empty list to store the results
    result = []

    # loop through the list of integers, starting from index 70
    for i in range(70, len(my_list)):
        # check if the current element is odd
        if my_list[i] % 2 != 0:
            # if it is odd, add it to the result list
            result.append(my_list[i])

    # return the result list
    return result
