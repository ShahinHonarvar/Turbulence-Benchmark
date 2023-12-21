
def insert_after_index(my_list):
    # Find the index where we want to insert the new element
    for i in range(len(my_list)):
        if my_list[i] == 323:
            return my_list[:i+1] + [389, 303] + my_list[i+1:]
