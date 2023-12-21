 def filter_chars(s):
    filtered = ""
    for i in range(len(s)):
        c = s[i]
        if (25 <= i <= 97) and ('m' <= c <= 'w'):
            continue

        filtered += c

    return filtered
