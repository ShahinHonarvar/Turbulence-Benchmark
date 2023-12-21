 def filter_chars(string):
    filtered_string = ""
    for i in range(35, 98 + 1):
        char = string[i]
        if char >= "A" and char <= "b":
            continue

        filtered_string += char

    return filtered_string
