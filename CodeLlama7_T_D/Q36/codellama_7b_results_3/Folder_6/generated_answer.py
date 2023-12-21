 def filter_chars(s):
    filtered = []
    for i in range(31, 70):
        if s[i] > 'B' and s[i] < 'v':
            continue

        else:

            filtered.append(s[i])

    return "".join(filtered)
