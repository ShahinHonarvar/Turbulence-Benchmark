
def insert_after_index(num_list):
    list_str = ""
    for i in range(len(num_list)):
        if num_list[i] == 89:
            list_str += '89'
            break
        list_str += str(num_list[i])
    list_str += '86'
    return list(map(int, list_str))
