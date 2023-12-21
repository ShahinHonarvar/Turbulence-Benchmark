
def return_n_greatest_chars(input_str):
    char_list = list(input_str)
    char_list.sort(reverse=True, key=ord)
    greatest_chars = char_list[:58]
    greatest_chars.sort(key=ord)
    return greatest_chars
