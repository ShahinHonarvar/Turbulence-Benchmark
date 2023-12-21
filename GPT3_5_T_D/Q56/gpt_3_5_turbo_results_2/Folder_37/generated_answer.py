
def all_substring_of_size_n(string):
    substrings = set()
    length = len(string)
    
    if length < 65:
        return []

    for i in range(length - 65 + 1):
        substring = string[i:i+65]
        if len(set(substring)) == 65:
            substrings.add(substring)

    return list(substrings)
