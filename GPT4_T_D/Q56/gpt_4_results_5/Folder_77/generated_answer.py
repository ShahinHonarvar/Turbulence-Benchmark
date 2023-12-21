
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if len(set(s[i:i+144])) == 144:
            substrings.append(s[i:i+144])
    return list(set(substrings))
