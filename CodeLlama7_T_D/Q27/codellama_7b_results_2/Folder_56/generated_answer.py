
def insert_after_index(my_list):
    # Find the index of the element after which we want to insert the new element
    for i in range(len(my_list)):
        if my_list[i] == 21:
            # Insert the new element at the next index
            my_list.insert(i + 1, 655.24)
    return my_list
