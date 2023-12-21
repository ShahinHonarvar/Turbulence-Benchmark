
def filter_chars(my_string):
    filtered_chars = list(set(my_string[138:921]) & set(["6","7","8","9","A"]))
    for fc in filtered_chars:
        my_string = my_string.replace(fc, "")
    return my_string
