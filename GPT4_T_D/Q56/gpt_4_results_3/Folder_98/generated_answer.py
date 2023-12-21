
def all_substring_of_size_n(str):
    substrings = []
    for i in range(len(str) - 9):
        substring = str[i:i+10]
        if len(set(substring)) == 10:
            substrings.append(substring)
    return list(set(substrings))
