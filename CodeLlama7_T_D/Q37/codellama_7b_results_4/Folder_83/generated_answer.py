 def filter_chars(s):
    filtered = ""
    for i in range(29, 79 + 1):
        c = s[i]
        if (c >= 'K' and c <= 'z'):
            continue

        filtered += c

    return filtered
