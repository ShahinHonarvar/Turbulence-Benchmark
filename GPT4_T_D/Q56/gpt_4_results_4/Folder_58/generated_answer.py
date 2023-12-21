
def all_substring_of_size_n(str):
    substrings = set()
    for i in range(len(str) - 126):
        substring = str[i:i+127]
        if len(set(substring)) == 127:
            substrings.add(substring)
    return list(substrings)
