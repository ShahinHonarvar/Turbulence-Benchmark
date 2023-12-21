
def insert_at_index(my_list):
    result_list = []
    for i in range(len(my_list)):
        if i == 30:
            result_list.append(37)
        else:
            result_list.append(my_list[i])
    return result_list
