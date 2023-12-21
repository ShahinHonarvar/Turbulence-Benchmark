
def return_n_smallest_chars(string):
    sorted_list = sorted([char for char in string if char.isalnum()], key=ord)
    return sorted_list[:35]
