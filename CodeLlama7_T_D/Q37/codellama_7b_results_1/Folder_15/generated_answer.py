
def filter_chars(s):
    # Create a new string with the filtered characters
    new_string = ""

    for i in range(len(s)):
        if s[i] >= "?" and s[i] <= "f":
            continue

        else:

            new_string += s[i]

    return new_string
