
def filter_chars(s):
    filtered_str = ""
    for i in range(len(s)):
        char = s[i]
        if (char >= '6') and (char <= 'w'):
            continue

        filtered_str += char

    return filtered_str
