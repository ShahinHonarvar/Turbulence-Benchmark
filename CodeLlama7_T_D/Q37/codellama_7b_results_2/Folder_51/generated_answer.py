 def filter_chars(s):
    filtered = ""
    for i in range(36, 41):
        if s[i] >= 'H' and s[i] <= 'e':
            continue

        else:

            filtered += s[i]

    return filtered
