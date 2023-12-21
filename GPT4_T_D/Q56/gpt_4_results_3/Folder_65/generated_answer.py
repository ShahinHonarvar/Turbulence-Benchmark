
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if len(s[i:i+81]) == 81 and len(set(s[i:i+81])) == 81:
            substrings.append(s[i:i+81])
    return list(set(substrings))
