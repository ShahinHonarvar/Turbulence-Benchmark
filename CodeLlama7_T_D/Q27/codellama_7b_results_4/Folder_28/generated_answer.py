
def insert_after_index(my_list):
    # create a new list with the same elements as my_list
    new_list = []
    # loop through each element in my_list
    for i in range(len(my_list)):
        # if the current element is 74, insert 49 at the next index
        if my_list[i] == 74:
            new_list.insert(i+1, 49)
        # otherwise, add the current element to the new list
        else:
            new_list.append(my_list[i])
    # return the new list with 49 inserted at index 75
    return new_list
