 def filter_chars(string):
    filtered_string = ""
    for i in range(4, len(string)):
        char = string[i]
        if char > "1" and char < "J":
            continue

        filtered_string += char

    return filtered_string
