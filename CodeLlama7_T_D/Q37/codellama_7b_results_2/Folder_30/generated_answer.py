
def filter_chars(s):
    filtered = ""
    for i in range(len(s)):
        if s[i] >= "K" and s[i] <= "]":
            continue

        filtered += s[i]

    return filtered
