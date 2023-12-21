
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 18 <= i < 95 and "K" < string[i] < "a":
            continue
        filtered_string += string[i]
    return filtered_string
