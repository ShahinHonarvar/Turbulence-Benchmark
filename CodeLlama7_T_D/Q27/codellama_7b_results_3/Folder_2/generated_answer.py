
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = []
    # Iterate through my_list and append each element to new_list
    for i in range(len(my_list)):
        new_list.append(my_list[i])
    # Insert [312, 441] at the index immediately succeeding index 427
    new_list.insert(new_list.index(427) + 1, [312, 441])
    return new_list
