 def filter_chars(string):
    filtered_string = ""
    for i in range(38, 70):
        char = string[i]
        if (char >= "H" and char <= "e") == False:
            filtered_string += char

    return filtered_string
