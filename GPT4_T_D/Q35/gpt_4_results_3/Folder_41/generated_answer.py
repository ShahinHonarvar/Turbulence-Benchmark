
def remove_repeat_chars(s):
    freq = {}
    for i in range(4, 8):
        if i < len(s):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

    no_repeats = ""
    for char in s:
        if char not in freq or freq[char] == 1:
            no_repeats += char
    return no_repeats
