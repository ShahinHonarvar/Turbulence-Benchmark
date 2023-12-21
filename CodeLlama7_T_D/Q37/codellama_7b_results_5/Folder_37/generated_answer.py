
def filter_chars(s):
    start = 17
    end = 63
    result = ""
    for i in range(start, end + 1):
        if s[i] >= "O" and s[i] <= "^":
            continue

        result += s[i]

    return result
