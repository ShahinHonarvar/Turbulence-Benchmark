
def filter_chars(s):
    result = ""
    for i in range(len(s)):
        if i < 51 or i > 77 or s[i] < "V" or s[i] > "Y":
            result += s[i]
    return result
