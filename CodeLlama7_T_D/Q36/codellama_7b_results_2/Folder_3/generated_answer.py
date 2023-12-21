 def filter_chars(s):
    filtered_string = ""
    for i in range(42, 78):
        if s[i] > "!" and s[i] < "?":
            continue

        else:

            filtered_string += s[i]

    return filtered_string
