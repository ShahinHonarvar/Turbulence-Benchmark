
def insert_after_index(input_list):
    index = 29 
    input_list = input_list[:index+1] + [28, 53] + input_list[index+1:]
    return input_list
