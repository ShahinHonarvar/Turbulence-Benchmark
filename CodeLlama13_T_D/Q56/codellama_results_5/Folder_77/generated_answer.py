
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 143):
        substring = s[i:i+144]
        if len(set(substring)) == 144 and not any(substring[j] == substring[j-1] for j in range(1, 144)):
            substrings.append(substring)
    return substrings
