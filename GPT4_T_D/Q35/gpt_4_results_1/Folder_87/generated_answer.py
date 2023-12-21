
def remove_repeat_chars(s):
    freq = {}
    for i in range(21, 43):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for key, value in freq.items():
        if value > 1:
            s = s.replace(key, '')
    return s
