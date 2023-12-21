 def filter_chars(string):
    filtered_string = ""
    for i in range(10, 53):
        char = string[i]
        if char >= '@' and char <= 'T':
            continue

        else:

            filtered_string += char

    return filtered_string
