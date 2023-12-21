
def return_n_smallest_chars(char_string):
    if len(set(char_string)) != len(char_string):
        raise ValueError("Input string should contain distinct characters")
    chars_list = sorted(list(char_string))
    chars_list.sort(key=ord)
    return chars_list[:82][::-1]
