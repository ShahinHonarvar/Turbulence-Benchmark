 def filter_chars(string):
    start_index = 43
    end_index = 80
    filtered_string = ""

    for i in range(start_index, end_index + 1):
        if string[i].isalpha():
            continue

        elif string[i] == "=" or string[i] <= "E":
            filtered_string += string[i]

        else:
            continue

    return filtered_string
