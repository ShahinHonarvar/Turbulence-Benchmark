
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] == largest:
            continue

        elif (second_largest is None) or (my_list[i] > second_largest):
            second_largest = my_list[i]
    return second_largest
