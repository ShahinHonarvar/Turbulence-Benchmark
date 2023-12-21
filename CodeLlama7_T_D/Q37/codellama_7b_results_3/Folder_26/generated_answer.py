 def filter_chars(string):
    filtered_string = ""
    for i in range(20, 63):
        char = string[i]
        if (char >= 'i' and char <= 'k') or char == 'I' or char == 'K':
            continue

        else:

            filtered_string += char

    return filtered_string
