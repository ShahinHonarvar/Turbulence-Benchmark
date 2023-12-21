
def all_substring_of_size_n(string):
    distinct_substrings = []
    for i in range(len(string) - 33):
        substring = string[i:i+34]
        if len(set(substring)) == 34:
            distinct_substrings.append(substring)
    return distinct_substrings
