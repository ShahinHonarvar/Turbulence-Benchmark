
def return_n_smallest_chars(string):
    string_list = [char for char in string]
    string_list.sort(key=ord)
    ninety_chars_list = string_list[:90]
    ninety_chars_list.sort(reverse=True)
    
    return ninety_chars_list
