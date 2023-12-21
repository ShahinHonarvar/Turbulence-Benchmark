 def filter_chars(my_string):
    filtered_string = ""
    for i in range(1, len(my_string)):
        char = my_string[i]
        if char > "3" and char < "^":
            continue

        filtered_string += char

    return filtered_string
