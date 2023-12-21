 def filter_chars(s):
    result = ""
    for i in range(18, 64):
        if s[i] > "3" and s[i] < "B":
            continue

        else:

            result += s[i]

    return result
