
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)-54):
        temp_substring = s[i:i+55]
        if len(set(temp_substring)) == 55:
            substrings.add(temp_substring)
    return list(substrings)
