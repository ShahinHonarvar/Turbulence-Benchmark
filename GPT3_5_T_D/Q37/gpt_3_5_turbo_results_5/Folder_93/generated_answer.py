
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 38 <= i <= 69 and "H" <= string[i] <= "e":
            continue
        filtered_string += string[i]
    return filtered_string
