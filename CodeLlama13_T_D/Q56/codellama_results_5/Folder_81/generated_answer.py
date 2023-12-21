
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[j-i:j+1] not in substrings and len(s[j-i:j+1]) == 98:
                substrings.append(s[j-i:j+1])
    return substrings
