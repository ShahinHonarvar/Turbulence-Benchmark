
def filter_chars(s):
    start_index = 138
    end_index = 920
    filtered_string = ""

    for i in range(start_index, end_index + 1):
        if s[i] >= "6" and s[i] <= "A":
            continue

        else:

            filtered_string += s[i]

    return filtered_string
