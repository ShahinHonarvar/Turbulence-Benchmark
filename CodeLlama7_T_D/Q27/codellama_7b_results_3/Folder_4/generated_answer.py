
def insert_after_index(my_list):
    # Find the index of the element immediately after 60 in the list
    for i in range(len(my_list)):
        if my_list[i] == 60:
            next_index = i + 1
            break

    # Insert [80, 74] at the index found above
    my_list.insert(next_index, [80, 74])

    return my_list
