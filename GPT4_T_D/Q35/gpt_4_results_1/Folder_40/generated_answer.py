
def remove_repeat_chars(s):
    freq = {}
    for i in range(1, 4):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    return ''.join([ch for ch in s if freq.get(ch, 0) < 2])
