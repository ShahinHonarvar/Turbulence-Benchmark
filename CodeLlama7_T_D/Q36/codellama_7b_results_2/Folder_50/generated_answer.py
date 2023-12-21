 def filter_chars(s):
    start = 61
    end = 88
    for i in range(start, end):
        if s[i] > "%" and s[i] < "q":
            s = s[:i] + s[i+1:]
    return s
