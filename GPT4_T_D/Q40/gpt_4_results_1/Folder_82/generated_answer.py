
def return_n_smallest_chars(input_string):
    char_list = list(input_string)
    char_list.sort(key=ord)
      
    return char_list[:60]
