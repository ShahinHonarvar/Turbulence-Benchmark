
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if len(set(s[i:j])) == 45:
                substrings.append(s[i:j])
    return list(set(substrings))
