
def all_substring_of_size_n(s):
    distinct_substrings = []
    for i in range(len(s)-143):
        substring = s[i:i+144]
        if len(set(substring)) == 144:
            distinct_substrings.append(substring)
    return distinct_substrings
