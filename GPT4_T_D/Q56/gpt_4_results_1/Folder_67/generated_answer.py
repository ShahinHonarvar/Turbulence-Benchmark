
def all_substring_of_size_n(s):
    length = 43
    substrings = [s[i: i + length] for i in range(len(s) - length + 1)]
    substrings = [substring for substring in substrings if len(set(substring)) == length]
    return list(dict.fromkeys(substrings))
