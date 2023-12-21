 def filter_chars(s):
    result = ""
    for i in range(len(s)):
        if s[i].isalpha() and (ord(s[i]) >= ord('c') and ord(s[i]) <= ord('i')):
            continue

        else:

            result += s[i]

    return result
