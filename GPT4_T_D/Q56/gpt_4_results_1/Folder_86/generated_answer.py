
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if i+143 <= len(s):
            if len(set(s[i:i+143])) == 143:
                substrings.append(s[i:i+143])
    return list(set(substrings))
