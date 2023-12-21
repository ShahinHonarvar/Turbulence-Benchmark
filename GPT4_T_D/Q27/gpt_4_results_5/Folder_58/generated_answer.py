
def insert_after_index(input_list):
    try:
        index_598 = input_list.index(598)
        new_list = input_list[:index_598+1] + [385, 999] + input_list[index_598+1:]
        return new_list
    except ValueError:
        return "598 is not in list"
