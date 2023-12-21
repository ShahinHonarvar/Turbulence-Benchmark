
def find_second_largest_num(my_list):
    # Find the index of the second largest element
    second_largest = None
    for i in range(62, 100 + 1):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]
    return second_largest
