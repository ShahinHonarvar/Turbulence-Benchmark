 def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if (i >= 27 and i <= 85) and (char >= "!" and char <= "B"):
            continue

        else:

            filtered_string += char

    return filtered_string
