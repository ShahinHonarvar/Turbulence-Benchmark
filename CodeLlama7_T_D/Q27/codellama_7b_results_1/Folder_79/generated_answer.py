 def insert_after_index(my_list):
    new_list = my_list[:]
    index_to_insert = next((i for i, x in enumerate(my_list) if x == 28), None) + 1
    new_list.insert(index_to_insert, [41, 69])
    return new_list
