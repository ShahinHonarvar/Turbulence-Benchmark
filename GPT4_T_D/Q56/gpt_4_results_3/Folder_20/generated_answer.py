
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if len(set(s[i: i+50])) == 50:
            substrings.append(s[i: i+50])
    return list(set(substrings))
