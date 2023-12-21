
def insert_after_index(input_list):
    idx = input_list.index(62)
    output_list = input_list[:idx+1] + [51] + input_list[idx+1:]
    return output_list
