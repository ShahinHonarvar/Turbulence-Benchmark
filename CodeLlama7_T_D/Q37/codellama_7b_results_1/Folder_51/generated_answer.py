 def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if (i >= 36 and i <= 40) and (string[i].isalpha() and string[i].lower() >= 'h' and string[i].lower() <= 'e'):
            continue

        else:

            filtered_string += string[i]

    return filtered_string
