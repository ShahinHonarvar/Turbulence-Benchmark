
def return_n_greatest_chars(chars_string):
    chars_string = sorted(chars_string, reverse=True)
    greatest_chars_list = chars_string[:48]
    greatest_chars_list.sort()
    return greatest_chars_list
