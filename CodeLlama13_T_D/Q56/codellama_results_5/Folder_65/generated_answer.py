
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 81 + 1):
        substring = s[i:i+81]
        if len(set(substring)) == 81 and not any(''.join(substring[:j]) in substrings for j in range(i, i+81)):
            substrings.append(substring)
    return substrings
