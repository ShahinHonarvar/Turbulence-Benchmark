
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 513 and i <= 877 and string[i] >= "?" and string[i] <= "n":
            continue
        filtered_string += string[i]
    return filtered_string
