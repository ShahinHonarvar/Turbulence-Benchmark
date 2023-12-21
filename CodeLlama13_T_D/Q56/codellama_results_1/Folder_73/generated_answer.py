
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 20 + 1):
        substring = s[i:i+20]
        if len(set(substring)) == 20 and all(ord('a') <= ord(c) <= ord('z') for c in substring):
            substrings.append(substring)
    return substrings
