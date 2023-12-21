
def filter_chars(my_string):
    filtered_string = ""
    for i in range(len(my_string)):
        char = my_string[i]
        if char < '>' and char > 'A':
            continue

        filtered_string += char

    return filtered_string
