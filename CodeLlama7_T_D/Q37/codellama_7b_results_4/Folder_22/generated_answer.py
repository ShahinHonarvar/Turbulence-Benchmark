
def filter_chars(s):
    start = 33
    end = 70

    for i in range(start, end + 1):
        if s[i].isalpha():
            if s[i] >= '7' and s[i] <= 'k':
                s = s.replace(s[i], '')



    return s
