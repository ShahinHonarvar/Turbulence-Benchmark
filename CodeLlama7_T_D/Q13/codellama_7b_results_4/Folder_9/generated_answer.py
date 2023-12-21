
def find_second_largest_num(my_list):
    # check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # check if the list has at least one element
    if len(my_list) == 0:
        raise ValueError("List cannot be empty")
    # find the second largest element in the list
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]
    return second_largest
