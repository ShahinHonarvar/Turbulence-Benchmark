 def filter_chars(s):
    start = 41
    end = 56
    result = ""

    for i in range(len(s)):
        if not (start <= i < end) or s[i].islower():
            result += s[i]

    return result
