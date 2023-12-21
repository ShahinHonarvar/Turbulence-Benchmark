 def filter_chars(s):
    start = 31
    end = 38
    new_string = ""
    for i in range(len(s)):
        if (start <= i <= end) and (ord(s[i]) >= ord(';')) and (ord(s[i]) <= ord('g')):
            continue

        else:

            new_string += s[i]

    return new_string
