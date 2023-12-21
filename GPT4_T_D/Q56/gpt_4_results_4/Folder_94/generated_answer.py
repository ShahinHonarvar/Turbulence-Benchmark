
def all_substring_of_size_n(s):
    substrings = []
    length = 70
    for i in range(len(s)):
        if i + length > len(s):
            break
        substr = s[i:i+length]
        if len(set(substr)) == len(substr):
            substrings.append(substr)
    return list(set(substrings))
