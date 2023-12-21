
def filter_chars(string):
    filtered_string = ""
    for i in range(51, 78):
        if string[i].isalpha() and string[i].isupper():
            if string[i] >= "V" and string[i] <= "Y":
                continue

        filtered_string += string[i]

    return filtered_string
