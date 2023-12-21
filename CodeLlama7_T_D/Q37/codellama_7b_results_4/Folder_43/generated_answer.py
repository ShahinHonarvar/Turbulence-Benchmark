
def filter_chars(my_string):
    start_index = 15
    end_index = 55
    filtered_string = ""
    for i in range(len(my_string)):
        if i >= start_index and i <= end_index:
            current_char = my_string[i]
            if current_char < "W" or current_char > "{":
                filtered_string += current_char

    return filtered_string
