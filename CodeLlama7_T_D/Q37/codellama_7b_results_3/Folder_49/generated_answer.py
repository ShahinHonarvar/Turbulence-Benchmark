 def filter_chars(s):
    start = 42
    end = 97
    filtered = ""
    for i in range(len(s)):
        if start <= i <= end and s[i] >= '*' and s[i] <= 'b':
            continue

        else:

            filtered += s[i]

    return filtered
