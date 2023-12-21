
def all_substring_of_size_n(input_str):
    if len(input_str) < 49:
        return []
    substrings = set()
    for i in range(len(input_str) - 48):
        substring = input_str[i:i+49]
        if len(set(substring)) == 49:
            substrings.add(substring)
    return list(substrings)
