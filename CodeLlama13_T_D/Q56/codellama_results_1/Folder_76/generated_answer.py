
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if j-i == 149:
                substring = s[i:j]
                if all(substring.count(c) == 1 for c in substring):
                    substrings.append(substring)
    return substrings
