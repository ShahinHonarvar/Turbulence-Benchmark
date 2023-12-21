
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 80):
        substring = s[i:i+81]
        if len(set(substring)) == 81 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
