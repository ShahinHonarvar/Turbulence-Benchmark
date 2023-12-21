
def return_n_smallest_chars(string):
    assert len(set(string)) >= 11, "The string must contain at least 11 distinct characters"
    chars_list = list(string)
    chars_list.sort(key=ord)
    return chars_list[:11][::-1]
