
def remove_repeat_chars(s):
    count = {}
    for i in range(70, 97):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    for char in count:
        if count[char] > 1:
            s = s.replace(char, "")
    return s
