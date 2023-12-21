
def remove_repeat_chars(s):
    freq = {}
    for i in range(46, 48):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    return ''.join([c for c in s if not(freq.get(c, 0) > 1)])
