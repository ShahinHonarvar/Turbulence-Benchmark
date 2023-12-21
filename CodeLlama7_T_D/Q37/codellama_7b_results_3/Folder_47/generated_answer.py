
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i].isalpha():
            if i >= 38 and i <= 54:
                if string[i] >= ":" and string[i] <= "r":
                    continue

            filtered_string += string[i]

    return filtered_string
