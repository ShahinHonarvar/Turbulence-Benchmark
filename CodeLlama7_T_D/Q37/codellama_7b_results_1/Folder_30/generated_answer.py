 def filter_chars(string):
    result = ""
    for i in range(len(string)):
        char = string[i]
        if (char >= 'K') and (char <= ']'):
            continue

        result += char

    return result
