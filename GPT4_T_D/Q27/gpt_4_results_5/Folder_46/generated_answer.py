
def insert_after_index(original_list):
    updated_list = original_list[:29]
    updated_list.append(717.02)
    updated_list += original_list[29:]
    return updated_list
