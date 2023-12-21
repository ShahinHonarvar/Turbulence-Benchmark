
def find_second_largest_num(my_list):
    # find the second largest element from index 28 to index 32, both inclusive
    second_largest = None
    for i in range(28, 33):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
