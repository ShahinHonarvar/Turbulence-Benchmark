
def filter_chars(string):
    filtered_string = ""
    for i in range(722, 833):
        if string[i] >= "K" and string[i] <= "m":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
