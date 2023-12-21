
def find_second_largest_num(my_list):
    # Find the index of the second largest element in the list
    index_of_second_largest = None
    for i in range(75, 95):
        if my_list[i] > my_list[i-1]:
            index_of_second_largest = i
    # Return the second largest element from index 75 to index 94, both inclusive
    return my_list[index_of_second_largest] if index_of_second_largest else None
