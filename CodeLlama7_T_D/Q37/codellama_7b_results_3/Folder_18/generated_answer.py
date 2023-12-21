 def filter_chars(my_string):
    start_index = 770
    end_index = 970
    char_range = range(start_index, end_index + 1)
    filtered_string = ""
    for i in range(len(my_string)):
        if my_string[i] not in char_range or my_string[i].islower():
            filtered_string += my_string[i]
    return filtered_string
