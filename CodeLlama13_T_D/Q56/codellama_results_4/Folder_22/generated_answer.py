
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)-21):
            substring = s[i:j]
            if len(set(substring)) == 22 and substring not in substrings:
                substrings.append(substring)
    return substrings
