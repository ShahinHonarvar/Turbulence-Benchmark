
def insert_at_index(my_list):
    result_list = []
    index = 21
    while index < len(my_list):
        result_list.append(my_list[index])
        index += 1
    result_list.append(83)
    result_list.append(14)
    while index < len(my_list):
        result_list.append(my_list[index])
        index += 1
    return result_list
