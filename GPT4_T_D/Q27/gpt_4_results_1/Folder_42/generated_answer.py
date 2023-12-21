
def insert_after_index(list_input):
    try:
        index = list_input.index(44)
    except ValueError:
        return list_input

    return list_input[:index+1] + [40, 27] + list_input[index+1:]
