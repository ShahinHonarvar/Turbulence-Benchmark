
def filter_chars(my_string):
    filtered_chars = [char for char in my_string[27:86] if char >= 'c' and char <= 'i']
    for char in filtered_chars:
        my_string = my_string.replace(char, "")
    return my_string
