
def filter_chars(s):
    filtered_string = ""
    for i in range(len(s)):
        char = s[i]
        if (char >= "!" and char <= "s") and (i >= 86 and i <= 92):
            continue

        filtered_string += char

    return filtered_string
