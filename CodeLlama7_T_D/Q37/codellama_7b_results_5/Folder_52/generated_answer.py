 def filter_chars(s):
    start = 54
    end = 83
    filtered = ""

    for i in range(start, end + 1):
        if s[i].islower() and s[i].isalpha():
            if s[i] >= 'j' and s[i] <= 'v':
                filtered += s[i]

    return filtered
