
def all_substring_of_size_n(s):
    length = len(s)
    substrings_of_length_64 = set()
    for i in range(length):
        if i+64 <= length:
            substring = s[i:i+64]
            if len(set(substring)) == len(substring):
                substrings_of_length_64.add(substring)
    return list(substrings_of_length_64)
