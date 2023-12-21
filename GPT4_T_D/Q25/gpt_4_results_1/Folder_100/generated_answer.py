
def insert_at_index(original_list):
    if len(original_list) >= 73:
        modified_list = original_list.copy()
        modified_list.insert(73, 418.88)
        return modified_list
    else:
        return "Error: List index out of range"
