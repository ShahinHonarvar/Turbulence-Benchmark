
def filter_chars(s):
    result = ""
    for i in range(10, 70):
        if s[i] >= "I" and s[i] <= "K":
            continue

        result += s[i]

    return result
